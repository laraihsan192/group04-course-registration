# Testing — v0.1.0

Run from the repository root after installing `requirements.txt`.

```sh
python -m unittest discover -s tests -v
```

**Result:** All six automated tests passed.

- **FR-01 — Demo sign-in:** Valid sign-in works, invalid sign-in shows an error, and the catalog requires sign-in.
- **FR-02 — Course search:** Search works by name and code, results show section details, and a query with no matches shows a message.
