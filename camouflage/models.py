"""Model manager"""

class Headers(dict):
    """Represents request headers."""

    def __init__(self, headers: dict):
        for k, v in headers.items():
            setattr(self, k.replace('-', '_').lower(), v)
