import os
import sys
import requests
import json
# from multiprocessing import Process
import subprocess
import queue
from subprocess import Popen, PIPE
import threading
import signal
import time

import socket

old_getaddrinfo = socket.getaddrinfo


def new_getaddrinfo(args, *kwargs):
    resps = old_getaddrinfo(args, *kwargs)
    return [resp for resp in resps if resp[0] == socket.AF_INET]


socket.getaddrinfo = new_getaddrinfo
done = False

def display_seed(verif_data, seed):
    global done
    print(f"Seed Found({verif_data['iso']}): {seed}")
    print(f"Temp Token: {verif_data}\n")
    done = True


def run_seed(filter, stopevent):
    seed = ""
    while seed == "":
        resp = requests.get(
            f"https://fsg.opalstacked.com/?filter={filter}")
        res_json = resp.json()
        sseed = res_json.get("struct")
        sclass = res_json.get("class")
        randbiome = res_json.get("randbiome")
        pref = res_json.get("pref")  # village and/or shipwreck preference
        cmd = f'biomehunt.exe {sseed} {sclass} {randbiome} {pref}'
        print(cmd)
        proc = Popen(cmd, shell=True, stdout=PIPE)
        for _ in range(10):
            try:
                stdout, _ = proc.communicate(timeout=0.2)
                seed = stdout.decode().strip()
                if seed != "":
                    display_seed(res_json, seed)
                    return
            except subprocess.TimeoutExpired:
                if stopevent.is_set():
                    print('detected stopevent, stopping')
                    # proc.terminate()
                    subprocess.run(f'taskkill /F /T /PID {proc.pid}', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    return
        subprocess.run(f'taskkill /F /T /PID {proc.pid}', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # proc.terminate()


def start_run():
    print("FindSeed has started...\n")
    with open('settings.json') as filter_json:
        read_json = json.load(filter_json)
        filter = read_json["filter"]
        num_processes = read_json["thread_count"]
    threads = []
    stopevents = []
    for i in range(num_processes):
        stopevent = threading.Event()
        t = threading.Thread(target=run_seed, args=(filter,stopevent))
        stopevents.append(stopevent)
        t.start()
        threads.append(t)
    
    while not done:
        time.sleep(0.05)
    print("Done")
    for stopevent in stopevents:
        stopevent.set()
    for thread in threads:
        thread.join()
    


if __name__ == '__main__':
    start_run()
