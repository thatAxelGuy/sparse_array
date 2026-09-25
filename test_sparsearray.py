import pytest

from main import SparseArray

# --- Constructor / string representation ---

def test_constructor_and_str():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    assert str(sa) == "[1, 0, 99, 2, 0, 100, 0, 1]"


# --- Length ---

def test_len():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    assert len(sa) == 8


# --- Get item ---

def test_getitem_existing_value():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    assert sa[0] == 1
    assert sa[2] == 99


def test_getitem_stored_zero():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    assert sa[1] == 0


def test_getitem_negative_index():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    assert sa[-1] == 1
    assert sa[-6] == 99
    assert sa[-8] == 1


# --- Set item ---

def test_setitem_updates_existing_value():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    sa[2] = 67

    assert sa[2] == 67
    assert str(sa) == "[1, 0, 67, 2, 0, 100, 0, 1]"


def test_setitem_adds_value_to_zero_position():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    sa[1] = 42

    assert sa[1] == 42
    assert sa._data[1] == 42


def test_setitem_zero_removes_value_from_storage():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    sa[2] = 0

    assert sa[2] == 0
    assert 2 not in sa._data


def test_setitem_negative_index():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    sa[-1] = 50

    assert sa[-1] == 50
    assert sa[7] == 50


# --- Delete item ---

def test_delitem_removes_value_and_reduces_length():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    del sa[2]

    assert str(sa) == "[1, 0, 2, 0, 100, 0, 1]"
    assert len(sa) == 7


def test_delitem_shifts_sparse_data():
    sa = SparseArray([0, 7, 0, 50, 0, 90])

    del sa[3]

    assert str(sa) == "[0, 7, 0, 0, 90]"
    assert sa._data == {1: 7, 4: 90}


def test_delitem_negative_index():
    sa = SparseArray([1, 0, 99, 2, 0, 100, 0, 1])

    del sa[-1]

    assert str(sa) == "[1, 0, 99, 2, 0, 100, 0]"
    assert len(sa) == 7


# --- Append ---

def test_append_non_zero():
    sa = SparseArray([1, 0, 5])

    sa.append(7)

    assert str(sa) == "[1, 0, 5, 7]"
    assert sa._data == {0: 1, 2: 5, 3: 7}
    assert len(sa) == 4


def test_append_zero():
    sa = SparseArray([1, 0, 5])

    sa.append(0)

    assert str(sa) == "[1, 0, 5, 0]"
    assert sa._data == {0: 1, 2: 5}
    assert len(sa) == 4


# --- Slicing ---

def test_slice():
    sa = SparseArray([10, 0, 20, 0, 30, 40])

    assert sa[1:4] == [0, 20, 0]


def test_slice_from_start():
    sa = SparseArray([10, 0, 20, 0, 30, 40])

    assert sa[:3] == [10, 0, 20]


def test_slice_to_end():
    sa = SparseArray([10, 0, 20, 0, 30, 40])

    assert sa[3:] == [0, 30, 40]


def test_slice_with_step():
    sa = SparseArray([10, 0, 20, 0, 30, 40])

    assert sa[::2] == [10, 20, 30]


def test_slice_negative_indices():
    sa = SparseArray([10, 0, 20, 0, 30, 40])

    assert sa[-4:-1] == [20, 0, 30]


# --- Invalid indices ---

def test_getitem_index_too_large():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(IndexError):
        sa[3]


def test_getitem_negative_index_too_small():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(IndexError):
        sa[-4]


def test_setitem_index_too_large():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(IndexError):
        sa[3] = 10


def test_setitem_negative_index_too_small():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(IndexError):
        sa[-4] = 10


def test_delitem_index_too_large():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(IndexError):
        del sa[3]


def test_delitem_negative_index_too_small():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(IndexError):
        del sa[-4]


# --- Invalid index type ---

def test_getitem_invalid_type():
    sa = SparseArray([1, 2, 3])

    with pytest.raises(TypeError):
        sa["hello"]
