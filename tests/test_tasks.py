import pytest

from crispy import tasks

@pytest.fixture
def base_task():
    return tasks.BaseTask('test')


def test_task(base_task):
    task = base_task
    print(task)
    assert 0
