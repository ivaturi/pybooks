VERSION = "1.0"
SCHEMA = {
    "title": {
    "type": str,
    "required" : True
    },
    "status":{
        "type": str,
        "required": True,
        "allowed_values": ["not started", "reading", "read", "abandoned"]
    },
    "author": {
        "type": str,
        "required": False
    },
    "rating": {
        "type": int,
        "required": False,
        "min": 1,
        "max": 5
    },
    "last_read": {
        "type": str,
        "required": False,
        "allowed_patterns" : ["yyyy", "yyyy-mm"]
    },
    "format": {
        "type": str,
        "required": False,
        "allowed_values": ["digital", "physical"]
    },
    "genres": {
        "type": list,
        "required" : False
    },
    "takeaway": {
        "type": str,
        "required": False
    }
}
