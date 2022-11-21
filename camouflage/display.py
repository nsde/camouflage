import os
import uuid
import tempfile
import webbrowser

from httpx import Response as httpx_response
from requests import Response as requests_response

from typing import Union

def show(response_or_html: Union[httpx_response, requests_response]) -> None:
    path = os.path.join(tempfile.gettempdir(), f'camouflage_python_{uuid.uuid4()}.html')
    
    html = response_or_html
    print(type(html))
    if isinstance(response_or_html, httpx_response) or isinstance(response_or_html, requests_response):
        html = response_or_html.text

    with open(path, 'w') as temp_html:
        temp_html.write(html)
    
    webbrowser.open(path)

if __name__ == '__main__':
    show('<h1><code>display.show()</code> works great!</h1>')
