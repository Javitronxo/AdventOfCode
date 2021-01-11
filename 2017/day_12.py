from __future__ import annotations

from dataclasses import dataclass, field
from queue import Queue
from typing import Set


@dataclass
class Program:
    id: int
    connections: Set[Program] = field(default_factory=set)
    all_connections: Set[Program] = field(default_factory=set)

    def __hash__(self) -> int:
        return self.id

    def total_connections(self) -> int:
        queue = Queue()
        queue.put(self)
        visited = set()
        visited.add(self.id)
        while not queue.empty():
            current = queue.get()
            for connection in current.connections:
                if connection.id not in visited:
                    queue.put(connection)
                    self.all_connections.add(connection)
                    visited.add(connection.id)
        return len(visited)


def main():
    programs = list()
    with open("day_12_input.txt") as f:
        for line in f.read().splitlines():
            id_str, connected_ids = line.split(" <-> ")
            programs.append((Program(int(id_str)), connected_ids.split(", ")))

    for program, connected_ids in programs:
        for connected_id in connected_ids:
            connected_program = [p for p, _ in programs if p.id == int(connected_id)][0]
            program.connections.add(connected_program)
            connected_program.connections.add(program)
    programs = [p for p, _ in programs]

    program_zero = [program for program in programs if program.id == 0][0]
    print(f"Part 1: {program_zero.total_connections()}")

    groups = 0
    visited = set()
    for program in programs:
        if program not in visited:
            groups += 1
            program.total_connections()
            visited.update(program.all_connections)
    print(f"Part 2: {groups}")


if __name__ == "__main__":
    main()
