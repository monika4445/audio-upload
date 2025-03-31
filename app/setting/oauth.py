import os
from authlib.integrations.starlette_client import OAuth

oauth = OAuth()

OAUTH_CLIENT_ID = os.getenv("YANDEX_CLIENT_ID")
OAUTH_CLIENT_SECRET = os.getenv("YANDEX_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8000/auth/callback"

oauth.register(
    name="yandex",
    client_id=OAUTH_CLIENT_ID,
    client_secret=OAUTH_CLIENT_SECRET,
    access_token_url="https://oauth.yandex.ru/token",
    authorize_url="https://oauth.yandex.ru/authorize",
    client_oauth_config={"scope": "login:email"}
)