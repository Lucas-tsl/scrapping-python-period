import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="urllib3")
# Suppress the specific NotOpenSSLWarning
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL 1.1.1+")

# Alternatively, you can suppress all urllib3 warnings:
# warnings.filterwarnings("ignore", module="urllib3")

import requests

# Simuler un navigateur Chrome pour éviter un blocage 403 Forbidden
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

URL = "https://v6.voiranime.com/"
response = requests.get(URL, headers=headers)

# response.content contient maintenant le HTML brut de la page