# Issues

## MVP
- [x] Validation
- [x] CRUD: load, write, create
- [x] CLI: `add` command
- [x] CLI: `-t` flag for test db
- [x] CLI: `list` command
- [x] CLI: fix skip check for int fields

## Backlog
- [ ] CRUD: delete
- [ ] Duplicate genres not filtered when adding a book
- [ ] User feedback about invalid entry comes too late — after whole book is entered

## Refactor Arc
- [ ] **1. Tests** — write tests for what exists before touching anything
- [ ] **2. Single responsibility** — break up functions doing too many things
- [ ] **3. Separation of layers** — UI knows nothing about data shape; crud knows nothing about CLI
- [ ] **4. Error handling** — consistent, predictable failure modes across all functions
- [ ] **5. Delete** — add missing CRUD operation once the above is solid
