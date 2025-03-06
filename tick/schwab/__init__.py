import os
import ssl

from .. import SECRETS


CLIENT_ID = os.environ.get("SCHWAB_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("SCHWAB_CLIENT_SECRET", "")
OAUTH_AUTHORIZE_URL = os.environ.get("SCHWAB_OAUTH_AUTHORIZE_URL", "")
OAUTH_TOKEN_URL = os.environ.get("SCHWAB_OAUTH_TOKEN_URL", "")
REDIRECT_URI = os.environ.get("SCHWAB_REDIRECT_URI", "")

PEM_PASSWORD = os.environ.get("PEM_PASSWORD", "")

CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
CONTEXT.load_cert_chain(SECRETS / "cert.pem", SECRETS / "key.pem", PEM_PASSWORD)
