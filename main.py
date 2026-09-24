class SparseArray:
    """A list-like array that stores only non-zero values."""

    def __init__(self, values: list[int]) -> None:
        """Initialize the sparse array from a sequence of integers."""
        self._length = len(values)
        self._data = {}

        for index, value in enumerate(values):
            if value != 0:
                self._data[index] = value


    def _to_list(self) -> list[int]:
        """Return the sparse array as a regular list."""
        new_list = []
        for i in range(self._length):
            if i in self._data:
                new_list.append(self._data[i])
            else:
                new_list.append(0)
        return new_list


    def _validate_index(self, index: int) -> int:
        """Normalize and validate index."""
        
        if index < 0:
                    index += self._length
        
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range.")

        return index

    def __str__(self) -> str:
        """Return a string representation of the array including zeros."""
        return f"{self._to_list()}"


    def __len__(self) -> int:
        """Return the virtual length of the sparse array."""
        return self._length


    def __getitem__(self, index: int) -> int:
        """Return the value at the given index, or zero if it is not stored."""

        index = self._validate_index(index)

        if index in self._data:
            return self._data[index]
        else:
            return 0


    def __setitem__(self, index: int, value: int) -> None:
        """Set the value at the given index, removing it from storage if zero."""

        index = self._validate_index(index)

        if value == 0:
            self._data.pop(index, None)
        else:
            self._data[index] = value

    def __delitem__(self, index: int) -> None:
        """Delete the value at the given index and reduce the array length."""
        index = self._validate_index(index)
        
        new_list = self._to_list()
        del new_list[index]
        self._length -= 1
        self._data.clear()
        for position, value in enumerate(new_list):
            if value != 0:
                self._data[position] = value



# Create a SparseArray
sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

# __str__
print("Array:", sa)

# __len__
print("Length:", len(sa))

# __getitem__ - regular indexes
print("sa[0]:", sa[0])
print("sa[2]:", sa[2])
print("sa[1] (stored as zero):", sa[1])

# __getitem__ - negative indexes
print("sa[-1]:", sa[-1])
print("sa[-6]:", sa[-6])
print("sa[-8]:", sa[-8])

# __setitem__ - update an existing value
sa[2] = 67
print("After sa[2] = 67:", sa)
print("sa[2]:", sa[2])

# __setitem__ - add a value where zero was stored
sa[1] = 42
print("After sa[1] = 42:", sa)
print("sa[1]:", sa[1])

# __setitem__ - setting a value to zero
sa[2] = 0
print("After sa[2] = 0:", sa)
print("sa[2]:", sa[2])

# __setitem__ - negative index
sa[-1] = 50
print("After sa[-1] = 50:", sa)
print("sa[-1]:", sa[-1])

# __delitem__ test
del sa[2]
print("After del sa[2]:", sa)
print("Length:", len(sa))

del sa[-1]
print("After del sa[-1]:", sa)
print("Length:", len(sa))

try:
    del sa[10]
except IndexError as error:
    print("Caught:", error)

# IndexError - positive index too large
try:
    print(sa[8])
except IndexError as error:
    print("Caught:", error)

# IndexError - negative index too small
try:
    print(sa[-9])
except IndexError as error:
    print("Caught:", error)

# __setitem__ IndexError - positive index too large
try:
    sa[8] = 10
except IndexError as error:
    print("Caught:", error)

# __setitem__ IndexError - negative index too small
try:
    sa[-9] = 10
except IndexError as error:
    print("Caught:", error)