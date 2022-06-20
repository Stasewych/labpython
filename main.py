from Classes.node import Node
from Classes.queue_linked_list import QueueLinkedList


def main():
    linked_list = QueueLinkedList()
    linked_list.push_node(Node(value=[0, 0]))
    linked_list.push_node(Node(value=[2, 2]))
    linked_list.push_node(Node(value=[3, 3]))
    linked_list.push_node(Node(value=[4, 4]))
    linked_list.push_node(Node(value=[5, 5]))
    linked_list.push_node(Node(value=[6, 6]))
    linked_list.push_node(Node(value=[7, 7]))
    linked_list.push_node(Node(value=[8, 8]))
    linked_list.push_node(Node(value=[9, 9]))
    linked_list.push_node(Node(value=[10, 10]))
    print("Length of queue ->", linked_list.find_length_of_queue())
    linked_list.print_linked_list()
    print(linked_list.find_node_by_value([5, 5]))
    linked_list.find_position_in_queue([10,11])
    print(linked_list.find_node_by_value_by_x(10))
    print(linked_list.find_node_by_value_by_y(7))
    print("Length from the first point to last -> ", linked_list.find_length_from_front_to_rear())
    linked_list.remove_node_by_key(key=[2, 2])
    linked_list.print_linked_list()
    print("First element pop ->",linked_list.pop_front_node().value)
    linked_list.print_linked_list()
    linked_list.delete_linked_list()
    linked_list.print_linked_list()


if __name__ == '__main__':
    main()