import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def test_activities(monkeypatch):
    """Provide a fresh activities dictionary for each test."""
    isolated_activities = copy.deepcopy(app_module.activities)
    monkeypatch.setattr(app_module, "activities", isolated_activities)
    return isolated_activities


@pytest.fixture
def client(test_activities):
    """Create an API client with isolated test data."""
    return TestClient(app_module.app)