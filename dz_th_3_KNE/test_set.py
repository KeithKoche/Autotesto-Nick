import pytest
from pytest import fixture


class SetTest:

#1 Тест на метод update (набор my_set дополнен значениями из набора other_set)
    def test_set_update(self, my_set, other_set):
        my_set.update(other_set)
        assert my_set == {1, 2, 3, 4, 5, 6}

#2 Тест на метод add (добавление нового элемента в набор)
    def test_set_add(self, my_set):
        my_set.add(9)
        assert my_set == {1, 2, 3, 9}

#3  Тест на метод discard (уаление элемента набора)
    def test_set_pop(self, my_set):
        my_set.discard(1)
        assert my_set == {2, 3}

#4  Тест на метод copy (копия набора)
    def test_set_copy(self, my_set):
        my_set.copy()
        assert my_set == {1, 2, 3, 1, 2, 3}

#5  Параметризованный тест на метод intersection (пересечение двух наборов по одинаковым элементам)
    @pytest.mark.parametrize("same_set", [{1, 0, 2}, {1, 2, 3}, {1, 4, 5}])
    def test_set_intersection(self, my_set, same_set):
        my_set.intersection(same_set)
        assert my_set == same_set


