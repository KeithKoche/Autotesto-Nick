import pytest
from pytest import fixture


class ListTest:

#1 Тест на метод append (добавление значения в список)
    def test_list_appending(self, my_list):
        my_list.append('d')
        assert my_list == ['a', 'b', 'c', 'd']

#2 Тест на метод clear (удаление всех значений из списка)
    def test_list_clearing(self, list_to_del):
        list_to_del.clear()
        assert list_to_del == []

#3 Тест на метод reverse (удаление значения из списка)
    def test_list_reverse(self, my_list, reversed_list):
        my_list.reverse()
        assert my_list == reversed_list

#4 Тест на метод update (дублирование списка)
    def test_list_update(self, my_list):
        my_list *= 2
        assert my_list == ['a', 'b', 'c', 'a', 'b', 'c']

#5  Параметризованный тест на метод remove (удаление значения из списка)
    @pytest.mark.parametrize("removable", ['a', 'd'])
    def test_list_fi_remove(self, my_list, removable):
        my_list.remove(removable)
        assert my_list == ['b', 'c']