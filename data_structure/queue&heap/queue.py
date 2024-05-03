from typing import Any


class Queue:
    def __init__(self, *args: Any):
        self.__items: list[Any] = list(args)
        self.__size: int = len(self.__items)

    # Queue에 item을 추가
    def enqueue(self, item: Any):
        self.__items.append(item)
        self.__size += 1
    
    # Queue에서 pop 명령, 선입선출이므로 가장 먼저 들어간 0번째 item이 pop된다.
    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        item: Any = self.__items.pop(0)
        self.__size -= 1
        return item

    # Queue가 비어있는지 확인
    def empty(self):
        return not self.__size
    
    # Queue의 사이즈 반환
    def __len__(self):
        return self.__size

    def __iter__(self):
        if self.empty():
            return None
        for item in self.__items:
            yield item
