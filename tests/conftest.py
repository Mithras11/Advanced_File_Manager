import pytest
from click.testing import CliRunner

RESOURCE_DIR = "tests/resources/plain"
DUPLICATES_RESOURCE_DIR = "tests/resources/duplicates"


@pytest.fixture(scope="function")
def runner(request):
    return CliRunner()


@pytest.fixture(scope="function")
def mock_organizer(monkeypatch):
    monkeypatch.setattr("shutil.move", lambda src, target: None)
    monkeypatch.setattr("os.makedirs", lambda target: None)
    monkeypatch.setattr("os.rmdir", lambda target: None)
    monkeypatch.setattr("os.remove", lambda target: None)
