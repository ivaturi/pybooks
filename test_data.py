# valid books - varied optional fields
valid_books = [
    {"title": "Dune", "status": "read", "rating": 5, "format": "physical", "author": "Frank Herbert"},
    {"title": "1984", "status": "reading"},
    {"title": "Sapiens", "status": "not started", "genres": ["history", "science"], "takeaway": "Interesting take on human progress"},
    {"title": "Neuromancer", "status": "abandoned", "last_read": "2023-06", "rating": 3},
    {"title": "Shogun", "status": "read", "last_read": "2021", "format": "digital", "author": "James Clavell", "rating": 4},
]

# invalid books - different ways to break schema
invalid_books = [
    {"title": "Bad Rating", "status": "read", "rating": 7},
    {"title": "Bad Status", "status": "finished"},
    {"title": "Bad Date", "status": "read", "last_read": "23-06"},
    {"title": "Bad Format", "status": "read", "format": "audio"},
    {"title": "Bad Key", "status": "read", "page": 42},
    {"status": "read"},
    {"title": "Bad Rating Low", "status": "read", "rating": 0},
    {"title": "Bad Rating string", "status": "read", "rating": "0"},
]

corrupt_json = "[{'title' : 'Bad rating' 'status' : 'unread}]"