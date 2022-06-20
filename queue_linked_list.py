from Classes.node import Node
from math import pow
from math import sqrt


class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def push_node(self, node):
        if self.first is None:
            self.first = node
            self.last = node
            return
        self.last.next = node
        self.last = node

    def remove_node_by_key(self, key):
        if self.first.value == key:
            self.first = self.first.next
            return
        temp = self.first
        while temp.next is not None:
            if temp.next.value == key:
                break
            temp = temp.next

        if temp.next is None:
            print("Node not found in the list (Do not exist already)")
        else:
            temp.next = temp.next.next
        return

    def pop_front_node(self) -> Node:
        node_to_return = self.first
        self.first = self.first.next
        return node_to_return

    def find_length_from_front_to_rear(self) -> float:
        return sqrt(
            pow((self.last.value[0] - self.first.value[0]), 2) +
            pow((self.last.value[1] - self.first.value[1]), 2)
        )

    def find_node_by_value(self, key) -> Node:
        temp = self.first
        while temp.next is not None:
            if temp.next.value == key:
                print("Node found in the list ", end="")
                return temp.next.value
            temp = temp.next
        if temp.next is None:
            print("Node not found in the queue (Do not exist)")

    def find_node_by_value_by_x(self, key) -> Node:
        temp = self.first
        while temp.next is not None:
            if temp.next.value[0] == key:
                print(f"Node found in the list with X = {key} ->", end="")
                return temp.next.value
            temp = temp.next
        if temp.next is None:
            print("Node not found in the queue (Do not exist)")

    def find_node_by_value_by_y(self, key) -> Node:
        temp = self.first
        while temp.next is not None:
            if temp.next.value[1] == key:
                print(f"Node found in the list with Y = {key} ->", end="")
                return temp.next.value
            temp = temp.next
        if temp.next is None:
            print("Node not found in the queue (Do not exist)")

    def find_length_of_queue(self):
        temp = self.first
        if self.first is None:
            return 0
        length_of_list = 1
        while temp.next is not None:
            length_of_list += 1
            temp = temp.next
        return length_of_list

    def print_linked_list(self):
        temp = self.first
        while temp:
            if temp.next is not None:
                print(temp.value, " -> ", end="")
            else:
                print(temp.value, end="\n")
            temp = temp.next
        return

    def find_position_in_queue(self, key):
        temp = self.first
        position_from_first = 0
        while temp is not None:
            position_from_first += 1
            if temp.value == key:
                print(f"Index of Node is {position_from_first}")
                return position_from_first
            temp = temp.next
        if temp is None:
            print("Node/index not found in the queue (Do not exist)")

    def delete_linked_list(self):
        self.first = None
        print("Linked list deleted successfully")
        return