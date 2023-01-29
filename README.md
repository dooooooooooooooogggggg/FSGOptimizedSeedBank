# FSGOptimizedSeedBank for Windows

This is a version of FSG built for windows with mingw64 so that wsl is no longer necessary.

## Instructions

- Go to [releases](https://github.com/pmaccamp/FSGOptimizedSeedBank/releases) and download the latest source code (zip) and unzip
- Download AutoHotkey from [their website](https://www.autohotkey.com/)
- Play around on [Andy's website](https://seedbankcustom.andynovo.repl.co/) to find a filter that works for you, and copy the filter code (should look something like this `000A000A00000000000A000A00000000000A000A00000000000A000A000000000`)
- Open settings.json and replace the current code with your own, as well as the number of threads you want to allocate
- Edit FSG_Atum_Macro Faster.ahk to and change the SavesDirectory to your FSG instance. Optionally change the reset hotkey at the bottom (default reset key PgDn).
- Finally, launch minecraft and run the FSG_Atum_Macro Faster.ahk. 

For macro developers: Just run `findSeed.exe` (built with pyinstaller) or `py findSeed.py` in your macro.

Disclaimer: We ran into issues until we converted 32 bit longs to 64 bit long longs.  We are both not very experienced at building C projects / porting to windows so it's possible this wasn't necessary and we were just missing compiler flags.

## To build on windows with mingw

gcc -fdiagnostics-color=always -g biomehunt.c -o biomehunt.exe -Iinclude -Llibs -lminecraft_nether_gen_rs -lcubiomes -lfsg -lgcrypt -lgpg-error -lws2_32 -luserenv -lbcrypt

Built cubiomes at this git commit https://github.com/Cubitect/cubiomes/commit/dd7e619

Built minecraft_nether_generation_rs at https://github.com/SeedFinding/minecraft_nether_generation_rs/commit/e0d69a449826a11b4cf396c00d1d0f05f7ccd0b9.  Make sure rustc is using mingw.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/specnr)
