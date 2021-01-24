import pytest
from pytest import fixture


class DictTest:

#1 Тест на метод items (возврат сущностей словаря)
    def test_dict_item_return(self, my_dicto):
        my_dicto.items()
        assert my_dicto == {"cat": 1, "dog": 2}

#2  Тест на метод copy (возврат копии словаря)
    def test_dict_copy(self, my_dicto):
        my_dicto.copy()
        assert my_dicto == {"cat": 1, "dog": 2, "cat": 1, "dog": 2}

#3  Тест на метод update (добавление новой сущности в словарь)
    def test_dict_update(self, my_dicto,new_pair):
        my_dicto.update(new_pair)
        assert my_dicto == {"cat": 1, "dog": 2, "bird": 3}

#4  Тест на метод clear (удаление всех сущностей из словаря)
    def test_dict_clear(self, my_dicto):
        my_dicto.clear()
        assert my_dicto == {}

#5  Параметризованный тест на метод get (возврат значения ключа)
    @pytest.mark.parametrize ("dict_key, dk_value", [("cat", 1), ("dog", 2), ("bird", 3)])
    def test_dict_get(self, my_dicto, dict_key, dk_value):
        my_dicto.get(dict_key)
        assert my_dicto.get(dict_key) == dk_value