VERSION = "1.0"
SCHEMA = {
    "title": {
    "type": str,
    "required" : True,
    "identity": True
    },
    "status":{
        "type": str,
        "required": True,
        "allowed_values": ["not started", "reading", "read", "abandoned"]
    },
    "author": {
        "type": str,
        "required": False,
        "identity": True
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
        "allowed_patterns" : [r"^\d{4}$", r"^\d{4}-\d{2}$"]
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
