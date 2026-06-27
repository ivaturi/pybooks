# Issues

- [x] Validation

- CRUD
    - [ ] delete

- Adding books  
    - [ ] Move validate out of create (create expects valid entries - single responsibility)
    - [ ] It is possible to add "genre", "genre", "genre" as a valid list of genres when creating a book
    - [ ] User feedback about invalid entry comes too late - after the whole book is entered

- CLI
  - [x] `add` command
  - [x] `-t` flag for test db
  - [ ] `list` command
  - [x] fix skip check for int fields (line 17 `books.py` — `len()` crashes on int)

- Testing
