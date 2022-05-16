#!/usr/bin/env python3

import traceback
import urllib.request
import os
import zipfile

def download(fn):
    """
    Downloads a file and installs it into Ren'Py.
    """

    dn = os.path.dirname(fn)
    if not os.path.exists(dn):
        print("For {}, the directory doesn't exist, not doing anything.".format(fn))
        return

    basename = os.path.basename(fn)

    url = "https://raw.githubusercontent.com/renpy/steam-deck-guide/master/files/" + basename

    print("Downloading", url, "to", fn + ".")

    with urllib.request.urlopen(url) as response:
        data = response.read().decode("utf-8")

    with open(fn, "w", encoding="utf-8") as f:
        f.write(data)

# The path to steamworks_sdk.zip
steamworks_zip = ""

def find_steamworks_zip():
    global steamworks_zip

    steamworks_zips = [
        i for i in os.listdir(".")
        if i.lower().startswith("steamworks_sdk") and i.lower().endswith(".zip") ]

    steamworks_zips.sort()

    if steamworks_zips:
        steamworks_zip = steamworks_zips[-1]
        print("Found steamworks at", steamworks_zip + ".")
    else:
        print("Could not find steamworks.")
        raise SystemExit()

def steamworks(src, dst):
    """
    Unpacks a steamworks file from `src` to `dst` if required.
    """

    # Add a prefix to src, to save typing.
    src = "sdk/redistributable_bin/" + src
    dst = dst + "/" + os.path.basename(src)

    dn = os.path.dirname(dst)
    if not os.path.exists(dn):
        print("For {}, the directory doesn't exist, not doing anything.".format(dst))
        return

    with zipfile.ZipFile(steamworks_zip) as zf:
        with zf.open(src) as f:
            data = f.read()

    with open(dst, "wb") as f:
        f.write(data)

    print("Unpacked {}.".format(dst))


def main():

    # Change to the directory containing this file.
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    if not os.path.exists("renpy/common"):
        print("This file is not inside a Ren'Py SDK or Game.")
        return
    else:
        print("Ren'Py found.")

    # Find steamworks.
    find_steamworks_zip()

    # Download the Ren'Py files.

    print()
    print("Downloading Ren'Py files:")
    print()

    download("renpy/common/00achievement.rpy")
    download("renpy/common/00steam.rpy")
    download("lib/python2.7/steamapi.py")
    download("lib/pythonlib2.7/steamapi.py")

    print()
    print("Unpacking steamworks:")
    print()

    steamworks("linux32/libsteam_api.so", "lib/linux-i686")
    steamworks("linux64/libsteam_api.so", "lib/linux-x86_64")
    steamworks("osx/libsteam_api.dylib", "lib/darwin-x86_64")
    steamworks("osx/libsteam_api.dylib", "lib/mac-x86_64")
    steamworks("steam_api.dll", "lib/windows-i686")
    steamworks("win64/steam_api64.dll", "lib/windows-x86_64")


    print()
    print("The Steam API was updated. You can delete this file and {}.".format(steamworks_zip))
    print("I'm making a note here, huge success.")
    print()


if __name__ == "__main__":
    try:
        main()
    except:
        traceback.print_exc()

    print("")
    print("")
    input("Press enter to end this program.")
