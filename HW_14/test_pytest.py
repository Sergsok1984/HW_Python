import json
import pytest

from task1 import Project


@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.json'
    with open("users.json", 'r', encoding='utf-8') as f, open(f_name, 'w', encoding='utf-8') as test_f:
        file = json.load(f)
        json.dump(file, test_f, ensure_ascii=False)
        yield test_f


def test_get_users_list(get_file):
    data = f'{Project.get_users_list().users_lst}'
    assert data == (f"[self.name='John', self.u_id=1, self.level=1, self.name='Tom', self.u_id=2, self.level=1, "
                    f"self.name='Bob', self.u_id=3, self.level=2]")


def test_login(get_file):
    p = Project.get_users_list()
    p.login("John", 1)
    data = f'{p.admin}'
    assert data == f"self.name='John', self.u_id=1, self.level=1"


def test_add_user(get_file):
    p = Project.get_users_list()
    p.login("John", 1)
    p.add_user("Sergei", 4, 2)
    data = f'{p.users_lst}'
    assert data == (f"[self.name='John', self.u_id=1, self.level=1, self.name='Tom', self.u_id=2, self.level=1, "
                    f"self.name='Bob', self.u_id=3, self.level=2, self.name='Sergei', self.u_id=4, self.level=2]")


def test_del_user(get_file):
    p = Project.get_users_list()
    p.login("John", 1)
    p.del_user("Bob", 3, 2)
    data = f'{p.users_lst}'
    assert data == f"[self.name='John', self.u_id=1, self.level=1, self.name='Tom', self.u_id=2, self.level=1]"


if __name__ == '__main__':
    pytest.main(['-v'])
