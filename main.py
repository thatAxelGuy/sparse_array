class SparseArray():

    def __init__(self, values: list[int]) -> None:
        self._length = len(values)
        self._data = {}

        for index, value in enumerate(values):
            if value != 0:
                self._data[index] = value

    def __str__(self) -> str:
        new_list = []
        for i in range(self._length):
            if i in self._data:
                new_list.append(self._data[i])
            else:
                new_list.append(0)
        return f"{new_list}"

    def __len__(self) -> int:
        return self._length


sa = SparseArray([1, 0, 1, 2, 0, 100, 0, 1])
print(sa)
print(len(sa))
print(type(sa))