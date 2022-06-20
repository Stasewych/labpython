class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __str__(self):
        return f"X = {self.value[0]}, Y = {self.value[1]}  "