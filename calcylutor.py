class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.iterator)
        except StopIteration:
            # Если достигнут конец, перезапускаем итератор
            self.iterator = iter(self.iterable)
            return next(self.iterator)


# Проверка работы CyclicIterator
if __name__ == "__main__":
    # Пример с range
    print("Пример с range(3):")
    cyclic_range = CyclicIterator(range(3))
    for _ in range(5):
        print(next(cyclic_range), end=" ")  # 0 1 2 0 1

    # Пример с list
    print("\n\nПример с list ['a', 'b', 'c']:")
    cyclic_list = CyclicIterator(['a', 'b', 'c'])
    for _ in range(5):
        print(next(cyclic_list), end=" ")  # a b c a b

    # Пример с set
    print("\n\nПример с set {1, 2, 3}:")
    cyclic_set = CyclicIterator({1, 2, 3})
    for _ in range(5):
        print(next(cyclic_set), end=" ")  # Порядок может быть разным, но цикл будет работать