class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.next_node = None
        self.data = None
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        self.data = data
        new_data = Node(self.data, self.next_node)
        if self.top is None:
            self.top = new_data
        else:
            new_data.next_node = self.top
            self.top = new_data

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top:
            data = self.top.data
            self.top = self.top.next_node
            return data
        else:
            return None

