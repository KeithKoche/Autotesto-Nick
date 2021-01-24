import pytest


@pytest.fixture(scope="function")
def my_list():
    return ['a', 'b', 'c']


@pytest.fixture(scope="function")
def list_to_del():
    return ['a', 'b', 'c']


@pytest.fixture(scope="function")
def reversed_list():
    return ['c', 'b', 'a']


@pytest.fixture(scope="function")
def my_set():
    return {1, 2, 3}


@pytest.fixture(scope="function")
def other_set():
    return {4, 5, 6}


@pytest.fixture()
def my_dicto():
    return {
        "cat": 1,
        "dog": 2
    }


@pytest.fixture()
def new_pair():
    return {"bird": 3}


@pytest.fixture()
def my_string():
    return "Word"


@pytest.fixture()
def low_string():
    return "wORD"


@pytest.fixture()
def case_string():
    return "world_without_you"
