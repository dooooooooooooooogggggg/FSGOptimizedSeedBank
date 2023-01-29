This is a version of FSG built for windows with mingw64 so that wsl is no longer necessary.  Just run `findSeed.exe` (built with pyinstaller) or `python findSeed.py` in your macro.

We ran into issues until we converted 32 bit longs to 64 bit long longs.  We are both not very experienced at building C projects / porting to windows so it's possible this wasn't necessary and we were just missing compiler flags.

# To build on windows with mingw
gcc -fdiagnostics-color=always -g biomehunt.c -o biomehunt.exe -Iinclude -Llibs -lminecraft_nether_gen_rs -lcubiomes -lfsg -lgcrypt -lgpg-error -lws2_32 -luserenv -lbcrypt

Built cubiomes at this git commit https://github.com/Cubitect/cubiomes/commit/dd7e619

Built minecraft_nether_generation_rs at https://github.com/SeedFinding/minecraft_nether_generation_rs/commit/e0d69a449826a11b4cf396c00d1d0f05f7ccd0b9.  Make sure rustc is using mingw.

# FSGOptimizedSeedBank

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/specnr)

## Instructions

Setup:

Tutorial video: https://youtu.be/qwLJZ89vgq0

- Download the latest release zip from [the releases page](https://github.com/Specnr/FSGOptimizedSeedBank/releases)
- Download AutoHotkey from [their website](https://www.autohotkey.com/)
- Download WSL from [this link](https://ubuntu.com/wsl) & open it
- Run `sudo su` then `apt update`
- Run `apt install openjdk-11-jre-headless`
- Run `chmod +x bh`
- Play around on [Andy's website](https://seedbankcustom.andynovo.repl.co/) to find a filter that works for you, and copy the filter code (should look something like this `000A000A00000000000A000A00000000000A000A00000000000A000A000000000`)
- Open settings.json and replace the current code with your own, as well as the number of threads you want to allocate
- Open ahk and update the minecraft saves folder

Running:

- Run the FSG_Macro.ahk, load into Minecraft and press F10. Latest verification details will be found in fsg_seed_token.txt

NOTE: If lagging too much run Slower_FSG_Macro.ahk

## Credit

- @AndyNovo the code behind the actual logic https://github.com/AndyNovo/fsgsrc
- @Specnr the code behind efficiently executing the seedfinding code (findSeed.py && multiSeed.py)
- @PodX12 the single-click AHK script
