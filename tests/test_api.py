
import pytest
from core.api_client import APIClient
from utils.assertions import assert_status, assert_key

client = APIClient()

@pytest.mark.parametrize("endpoint", ["fact", "breeds", "facts"])
def test_endpoint_availability(endpoint):
    resp = client.get(endpoint)
    assert_status(resp)

def test_fact_structure():
    resp = client.get("fact")
    body = resp.json()
    assert_key(body, "fact")
    assert isinstance(body["fact"], str)

def test_fact_not_empty():
    resp = client.get("fact")
    fact_text = resp.json().get("fact", "")
    assert fact_text.strip()

def test_breeds_list_format():
    resp = client.get("breeds")
    body = resp.json()
    assert_key(body, "data")
    assert isinstance(body["data"], list)
    if body["data"]:
        assert "breed" in body["data"][0]

def test_breeds_pagination_fields():
    resp = client.get("breeds")
    body = resp.json()
    for key in ["current_page", "last_page", "total"]:
        assert key in body

def test_limit_param_effect():
    resp = client.get("facts", params={"limit": 3})
    items = resp.json().get("data", [])
    assert len(items) == 3

def test_facts_list_structure():
    resp = client.get("facts", params={"limit": 2})
    items = resp.json().get("data", [])
    assert isinstance(items, list)
    if items:
        assert "fact" in items[0]

def test_invalid_endpoint_returns_404():
    resp = client.get("no-such-endpoint-xyz")
    assert resp.status_code == 404
