# Mod Update Checker
This python file is designed to index a text file of your mods, and automatically count which ones are:
1. Not updated
2. Replaced with another mod
3. No longer needed
4. An old version of the mod is used

## How to use:
First off, to get a text file containing all of your mods, I recommend to do this:
1. cd to your .minecraft/mods/ directory
2. Run the following command:
  ls mods >> mods.txt
3. Go through your mods.txt file, and use this to search for your mods on the interwebs to download and add to a /mods_updated/ folder.
4. Use this syntax while updating the mods
If mod is updated:
  Move to next mod
If mod is not updated:
    Append "[!]" to the front of the line.
    EX: [!] Fastload+1.18.2-1.19.4-3.3.7.jar
If mod has been replaced with another mod:
    Append "[R]" to the front of the line.
    EX: [R] litematica-fabric-1.19.3-0.13.2.jar
If mod is no longer needed:
    Append "[N]" to the front of the line.
    EX: [N] smoothboot-fabric-1.19-1.7.1.jar
If an old version of the mod has been used:
    Append "[/]" to the front of the line.
    EX: [/] completeconfig-2.3.0.jar
Save the file.
6. Remove the old /mods/ folder, and change the name of /mods_updated/ to /mods/
7. Run mod_update_checker.py to figure out which mods you will need to come back to later to update or otherwise change.
    python3 update_checker.py
    Please input the file path for your mod list (path/to/file.txt): /path/to/file.txt
    Results will be displayed.
