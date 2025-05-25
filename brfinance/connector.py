from requests import Session
import requests

# Disable warnings for unverified HTTPS requests
requests.packages.urllib3.disable_warnings()

# Configure ciphers for urllib3 compatibility with both old and new API
try:
    # For urllib3 < 2.0.0
    if hasattr(requests.packages.urllib3.util.ssl_, 'DEFAULT_CIPHERS'):
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    
    # Try to configure pyopenssl if available
    if hasattr(requests.packages.urllib3, 'contrib') and hasattr(requests.packages.urllib3.contrib, 'pyopenssl'):
        if hasattr(requests.packages.urllib3.contrib.pyopenssl, 'DEFAULT_SSL_CIPHER_LIST'):
            requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except (AttributeError, ImportError):
    # No relevant urllib3 features available or different API structure in urllib3 >= 2.0.0
    pass


class CVMHttpClientConnector():

    def __init__(self) -> None:
        self.CONNECTOR = Session()

    def get_connector(self):
        return self.CONNECTOR


class CVMHttpClientConnector():

    def __init__(self) -> None:
        self.CONNECTOR = Session()

    def get_connector(self):
        return self.CONNECTOR
