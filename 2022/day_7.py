from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class File:
    name: str
    size: int

    @property
    def is_dir(self) -> bool:
        return False


@dataclass
class Directory:
    name: str
    parent: Directory = None
    contents: List = field(default_factory=list)

    @property
    def size(self) -> int:
        return sum([element.size for element in self.contents])

    @property
    def is_dir(self) -> bool:
        return True


def main():
    all_directories = list()
    context = list()

    with open("day7_input.txt") as f:
        for line in f.readlines():
            parts = line.split()
            if line.startswith("$"):
                if parts[1] == "cd":  # Command: change directory
                    dst = parts[2]
                    if dst == "/":
                        directory = Directory(name=dst)
                        all_directories.append(directory)
                        root_dir = directory
                    elif dst == "..":
                        directory = context.pop()
                    else:
                        context.append(directory)
                        directory = [d for d in directory.contents if d.name == dst and d.is_dir][0]
                else:  # Command: List directory
                    continue
            else:
                parts = line.split()
                try:
                    file = File(name=parts[1], size=int(parts[0]))
                    directory.contents.append(file)
                except ValueError:
                    new_folder = Directory(name=parts[1], parent=directory)
                    directory.contents.append(new_folder)
                    all_directories.append(new_folder)

    print(f"Part 1: {sum([directory.size for directory in all_directories if directory.size <= 100000])}")

    total_disk_space = 70000000
    space_needed = 30000000
    min_needed = space_needed - (total_disk_space - root_dir.size)
    print(f"Part 2: {min([directory.size for directory in all_directories if directory.size >= min_needed])}")


if __name__ == "__main__":
    main()
