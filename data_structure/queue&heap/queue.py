from typing import Any


class Queue:
    def __init__(self, *args: Any):
        self.__items: list[Any] = list(args)
        self.__size: int = len(self.__items)

    def enqueue(self, item: Any):
        self.__items.append(item)
        self.__size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        item: Any = self.__items.pop(0)
        self.__size -= 1
        return item

    def empty(self):
        return not self.__size

    def __len__(self):
        return self.__size

    def __iter__(self):
        if self.empty():
            return None
        for item in self.__items:
            yield item
