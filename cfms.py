import os
import sys
import requests
import json
from multiprocessing import Process

key_pressed = False


def display_seed(seed_data):
    print(f"Seed Found({seed_data['iso']}): {seed_data['seed']}")
    print(f"Signature: {seed_data['signature']}\n")


def run_seed(filter):
    resp = requests.get(f"http://fsg.gel.webfactional.com?filter={filter}")
    res_json = resp.json()
    sseed = res_json.get("struct")
    sclass = res_json.get("class")
    randbiome = res_json.get("randbiome")
    pref = res_json.get("pref")  # village and/or shipwreck preference
    cmd = f'./bh {sseed} {sclass} {randbiome} {pref}'
    seed = os.popen(cmd).read().strip()
    # Seed is None iff bh times out
    res_json["seed"] = int(seed) if seed != "" else None
    display_seed(res_json)


def start_run(max_processes):
    with open('filter.json') as filter_json:
        filter = json.load(filter_json)["filter"]
    processes = []
    for i in range(max_processes):
        processes.append(Process(target=run_seed, args=(filter,)))
        processes[-1].start()
    i = 0
    while True:
        to_remove = []
        for j in range(len(processes)):
            if not processes[j].is_alive():
                to_remove.append(j)
        for j in range(len(to_remove)):
            processes.pop(to_remove[j] - j)
        if len(processes) < max_processes and sys.stdin.readline() == '\n':
            to_add = max_processes - len(processes)
            for j in range(to_add):
                processes.append(Process(target=run_seed, args=(filter,)))
                processes[-1].start()
        i = (i + 1) % max_processes


if __name__ == '__main__':
    PROCESSES_COUNT = int(sys.argv[1]) if len(sys.argv) >= 2 else 4
    start_run(PROCESSES_COUNT)
