
# API Automation Framework 

This repository contains a compact but practical API testing setup built using `pytest`.  
The **Cat Facts API** was chosen because it’s stable, open, and provides enough variety to demonstrate schema validation, pagination checks, parameter testing, and negative testing.

---

## How to Run

```bash
pip install -r requirements.txt
pytest -v
```

---

## Test Cases (Required Table)

| Test Name | Purpose | Validation Used | Why This Validation |
|----------|----------|----------------|---------------------|
| Endpoint availability | Check `/fact`, `/breeds`, `/facts` all respond correctly | Status code check | Ensures endpoints are alive and responding as expected |
| Fact structure | Verify `/fact` has expected structure | Key presence + type check | Ensures schema consistency |
| Fact text not empty | Validate `/fact` returns meaningful text | String non-empty check | Prevents empty/blank values from passing silently |
| Breeds list format | Check `/breeds` returns list with expected fields | Key check + type check | Ensures returned data is well‑structured |
| Breeds pagination fields | Validate pagination metadata | Key presence checks | Ensures paginated API remains stable |
| Limit parameter behavior | Confirm `/facts` obeys `limit` query | Array length assertion | Confirms backend honors query filters |
| Facts list structure | Light schema sniffing on `/facts` items | Key presence check | Ensures general consistency without strict contracts |
| Invalid endpoint returns 404 | Validate error handling | Status code check | Confirms API behaves correctly for invalid routes |

---

## Description of Validations (Required Section)

### Status Code Validation  
Used to confirm endpoint health and ensure the service is reachable.  
Useful for detecting outages or misconfigured URLs.

### Schema/Key Validation  
Ensures the API maintains its expected contract.  
Helps catch backend changes that break clients.

### Type Validation  
Light type checks (e.g., string, list) prevent subtle issues like returning an empty object instead of a list.

### Functional Parameter Validation  
Used for the `limit` parameter to ensure the API respects input filters.

### Negative Validation  
A proper API must return the correct status code (`404`) for invalid endpoints.  
This ensures predictable and safe error handling.

---

##  Notes 

- Helpers and assertions intentionally remain lightweight.
- The structure avoids unnecessary layers but is extendable.
- Tests cover availability, schema, pagination, parameters, and negative flow.
- Good balance of readability and thoroughness.

---

## Test Execution (GIF)

The GIF below shows the test running locally:

![Test Execution](assets/test_run.gif)

##  Folder Structure
```
api_automation_framework/
│── pytest.ini
│── requirements.txt
│── README.md
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── core/
│   ├── __init__.py
│   └── api_client.py
│
├── asset/
│   ├── test_run.gif
|
├── utils/
│   ├── __init__.py
│   └── assertions.py
│
└── tests/
    └── test_api.py
```