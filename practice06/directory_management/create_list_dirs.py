import os

path = "parent/child/grandchild"

os.makedirs(path, exist_ok=True)
print("Directories created")

from pathlib import Path

path = Path("parent/child/grandchild")
path.mkdir(parents=True, exist_ok=True)

print("Directories created")

import os

path = "."

for item in os.listdir(path):
    print(item)

import os

path = "."

for item in os.listdir(path):
    if os.path.isfile(item):
        print("File:", item)
    elif os.path.isdir(item):
        print("Folder:", item)

from pathlib import Path

path = Path(".")

for item in path.iterdir():
    if item.is_file():
        print("File:", item.name)
    elif item.is_dir():
        print("Folder:", item.name)

import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))

from pathlib import Path

for file in Path(".").rglob("*.txt"):
    print(file)

from pathlib import Path

# create nested directories
Path("data/logs/2026").mkdir(parents=True, exist_ok=True)

# list contents
for item in Path("data").iterdir():
    print(item)

# find all .log files
for file in Path("data").rglob("*.log"):
    print("Found:", file)