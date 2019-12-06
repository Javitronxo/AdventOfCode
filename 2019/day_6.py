# https://adventofcode.com/2019/day/6


def read_input_file(file_name):
    output = list()
    with open(file_name) as f_in:
        for line in f_in.readlines():
            parts = line.strip().split(')')
            output.append(parts)
    return output


class Graph:
    def __init__(self):
        self.nodes = list()

    def add_node(self, new_node):
        for node in self.nodes:
            if node.name == new_node.parent:
                new_node.parent_node = node
            elif node.parent == new_node.name:
                node.parent_node = new_node
        self.nodes.append(new_node)

    def count_all_orbits(self):
        total_orbits = 0
        for node in self.nodes:
            tmp_node = node
            n_orbits = 1
            while tmp_node.parent_node:
                tmp_node = tmp_node.parent_node
                node.parents.append(tmp_node.parent)
                n_orbits += 1
            total_orbits += n_orbits
        return total_orbits

    @staticmethod
    def distance_between_nodes(node_1, node_2):
        """NOTE: Make sure the function count_all_orbits is called first to populate the parents lists"""
        nexus = None
        distance = -1
        for parent in node_1.parents:
            if parent in node_2.parents:
                nexus = parent
                break
        if nexus:
            distance = node_1.parents.index(nexus) + node_2.parents.index(nexus) + 2
        return distance


class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.parent_node = None
        self.parents = list()


def define_graph(input_map):
    graph = Graph()
    you_node, santa_node = None, None
    for parent, name in input_map:
        node = Node(name, parent)
        graph.add_node(node)
        if name == 'YOU':
            you_node = node
        elif name == 'SAN':
            santa_node = node
    return graph, you_node, santa_node


def main():
    input_map = read_input_file('day_6_input.txt')
    graph, you_node, santa_node = define_graph(input_map)

    result_first_part = graph.count_all_orbits()
    print("First part result: {}".format(result_first_part))
    result_second_part = graph.distance_between_nodes(you_node, santa_node)
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
