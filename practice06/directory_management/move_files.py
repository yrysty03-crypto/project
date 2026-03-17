import shutil

shutil.move("source/file.txt", "destination/file.txt")

print("File moved")

import shutil

shutil.move("file.txt", "backup/")

print("Moved to backup folder")

import shutil

shutil.copy("source/file.txt", "destination/file.txt")

print("File copied")

import shutil

shutil.copy2("source/file.txt", "destination/file.txt")

import shutil

shutil.copytree("source_folder", "destination_folder")

import os
import shutil

for file in os.listdir("source"):
    if file.endswith(".txt"):
        shutil.move(f"source/{file}", f"destination/{file}")

import os
import shutil

for file in os.listdir("source"):
    if file.endswith(".jpg"):
        shutil.copy(f"source/{file}", f"images/{file}")

from pathlib import Path
import shutil

src = Path("file.txt")
dst = Path("backup/file.txt")

shutil.move(src, dst)

import os
import shutil

src = "file.txt"
dst = "backup/file.txt"

if os.path.exists(src):
    shutil.move(src, dst)
    print("Moved safely")
else:
    print("File not found")