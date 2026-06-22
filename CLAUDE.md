# Books Project

A personal book tracker in Python. Stores a reading list with metadata (status, rating, format, etc.) in a local `books.json` file.

## Project Structure

| File | Purpose |
|---|---|
| `schema.py` | `VERSION` + `SCHEMA` dict defining field types, required flags, allowed values/patterns, min/max |
| `validate.py` | `validate(book)` — validates a book dict against the schema, returns bool |
| `crud.py` | `load_books`, `write_books`, `create` — file I/O and mutation |
| `utils.py` | `read_json(fname)`, `write_json(fname, data)` — thin JSON helpers |
| `test_data.py` | `valid_books` and `invalid_books` lists for manual testing |
| `test_crud.py` | Manual test script (not a test framework — just run it directly) |
| `books.json` | The "database" — a JSON array of book dicts |
| `todo.md` | Project checklist |

## Current State (as of 2026-06-22)

- [x] Schema defined (`schema.py`)
- [x] Validation complete (`validate.py`) — invalid keys, required keys, type checking, allowed_values, allowed_patterns (regex), min/max
- [x] `load_books()` done
- [x] `write_books(books)` done — needs return value on failure (currently returns None instead of False like load_books)
- [ ] `create(book)` — next step
- [ ] Basic testing
- [ ] Minimal UI

## How to Run

Run each test file directly (no test framework — plain Python scripts):

```bash
python test_validate.py   # tests validate.py
python test_crud.py       # tests crud.py
```

`test_data.py` is shared test data (valid and invalid book dicts), not run directly.

No dependencies beyond the standard library.

## Schema Quick Reference

Required fields: `title` (str), `status` (str: "not started" | "reading" | "read" | "abandoned")

Optional fields: `author` (str), `rating` (int 1–5), `last_read` (str: YYYY or YYYY-MM), `format` (str: "digital" | "physical"), `genres` (list), `takeaway` (str)
