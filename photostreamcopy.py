#!/usr/bin/env python

import os
import sys
import shutil
import fnmatch
import time
import gntp.notifier

if (len(sys.argv) < 2):
    sys.exit("A target directory is needed")


image_types = ['.JPG', '.JPEG', '.PNG', '.GIF', '.TIFF']

ps_dir = os.environ['HOME'] + '/Library/Application Support/iLifeAssetManagement/assets'
target_dir = sys.argv[1]

total_files = 0


if (not target_dir.endswith("/")):
    target_dir = target_dir = target_dir + "/"

touchtime = "19020101.000000"  # Default timestamp to start. Making the assumption digital cameras were not around in 1902 ;)

for fname in os.listdir(target_dir):
    if fnmatch.fnmatch(fname, '?[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].[0-9][0-9][0-9][0-9][0-9][0-9]'):
        touchtime = fname[1:]

latestmtime = touchtime

for path, subdirs, files in os.walk(ps_dir):
    for name in files:
        filename = os.path.join(path, name)
        basename, ext = os.path.splitext(name)

        if any(ext.lower() == _ext.lower() for _ext in image_types):
            fmodtime = time.strftime("%Y%m%d.%H%M%S", time.localtime(os.path.getmtime(filename)))

            if (fmodtime > touchtime):
                target_file = target_dir + fmodtime + "-" + name.lower()
                shutil.copy2(filename, target_file)
                total_files += 1
                if (fmodtime > latestmtime):
                    latestmtime = fmodtime

orig_touchfile = target_dir + "." + touchtime
new_touchfile = target_dir + "." + latestmtime

if (os.path.isfile(orig_touchfile)):
    os.remove(orig_touchfile)
open(new_touchfile, "w").close()

gntp.notifier.mini("Photostream Copy C'est finis! It copied " + str(total_files) + " files")
