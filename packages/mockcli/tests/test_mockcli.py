from importlib import metadata
from types import ModuleType

import mocklib
from mocklib.core import hello


def test_project_name(project_name: str, project_pkg: ModuleType):
    assert project_pkg.__name__ == project_name
    assert project_pkg.__name__ == "mockcli"


def test_project_version(project_name: str, project_pkg: ModuleType):
    assert project_pkg.__version__ == metadata.version(project_name)
    assert project_pkg.__version__ == "0.2.0"


def test_mocklib_name():
    assert mocklib.__name__ == "mocklib"


def test_mocklib_hello():
    assert hello() == "Hello from mocklib!"
