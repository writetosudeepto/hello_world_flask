import pytest
from app import app
import json


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/api/greeting')
    assert resp.status_code == 200
    assert resp.json == {'message': 'Hello, this is your Flask API!'}
