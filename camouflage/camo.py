import pkgutil

from urllib.parse import urlparse
from contextlib import contextmanager

@contextmanager
def camouflaged(domain_or_url: str=None) -> dict:
    """Returns a naturalistic request headers."""
    
    domain = urlparse(domain_or_url).netloc
    
    file_content = pkgutil.get_data('camouflage', 'config/headers.txt').decode('utf8').replace('DOMAIN', domain).split('\r\n')

    headers = {}

    for line in file_content:
        line = line.split(': ')
        
        if not domain and line[0] == 'Host':
            continue

        headers[line[0]] = line[1].strip()

    yield headers
