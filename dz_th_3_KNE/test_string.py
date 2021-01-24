import pytest
from pytest import fixture

class StringTest:

#1 Тест на метод istitle (строка начинается с заглавной буквы)
    def test_string_istitle(self, my_string):
        my_string.istitle()
        assert my_string.istitle() == True

#2  Тест на метод capitalize (перенос первого символа значения строки в верхний регистр)
    def test_string_capitalize(self, low_string):
        low_string.capitalize()
        assert low_string.capitalize() == "Word"

#3  Тест на метод isspace (наличие неотображаемых символов)
    def test_string_isspace(self, my_string):
        my_string.isspace()
        assert my_string.isspace() == False

#4  Тест на метод upper (символы переходя в врехний регистр)
    def test_string_upper(self, case_string):
        case_string.upper()
        assert case_string.upper() == "WORLD_WITHOUT_YOU"

#5  Параметризованный тест на метод index
    @pytest.mark.parametrize("key, ind", [('W', 0), ('o', 1), ('r', 2), ('d', 3)])
    def test_string_index(self, my_string, key, ind ):
        my_string.index(key)
        assert my_string.index(key) == ind