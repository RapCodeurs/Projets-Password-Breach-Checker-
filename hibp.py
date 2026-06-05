import hashlib
import requests # pyright: ignore[reportMissingModuleSource]

<<<<<<< HEAD
<<<<<<< HEAD


def sha1_hash(password: str) -> str:
    # Convertir le mot de passe en SHA-1 et le retourner en majuscules
    return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

def get_pwned_count(password: str) -> int:
    # Obtenir le hash SHA-1 du mot de passe et diviser en préfixe et suffixe
    hashed_password = sha1_hash(password)
    prefix = hashed_password[:5]
    suffix = hashed_password[5:]

    # Interroger l'API avec les 5 premiers caractères du hash
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, Verifiez l'API et essayez à nouveau.")
    
    # Parcourir les résultats pour trouver le suffixe correspondant
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0
=======
=======
>>>>>>> 5535edcfcaf42465cfd94d5e039d316e59bc8a2e
from exceptions import (
    APIConnectionError,
    APIResponseError,
)

class HIBPClient:
    BASE_URL = ("https://api.pwnedpasswords.com/range/")

    def __init__(self, timeout=10):
        self.timeout = timeout
        
    
    def _sha1_hash(self, password: str) -> str:
        # Convertir le mot de passe en SHA-1 et le retourner en majuscules
        return hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    
    def _get_hash_range(self, prefix: str) -> str:
        # Interroger l'API avec les 5 premiers caractères du hash
        url = f"{self.BASE_URL}{prefix}"
        try:
            response = requests.get(url, timeout=self.timeout)       
        except requests.RequestException as e:
            raise APIConnectionError( str(e))
        if response.status_code != 200:
            raise APIResponseError(f"Status code: {response.status_code}, Verifiez l'API et essayez à nouveau.")
        return response.text
    
    def check_password(self, password: str) -> int:
        # Obtenir le hash SHA-1 du mot de passe et diviser en préfixe et suffixe
        hashed_password = self._sha1_hash(password)
        prefix = hashed_password[:5]
        suffix = hashed_password[5:]

        response_text = self._get_hash_range(prefix)
        # Parcourir les résultats pour trouver le suffixe correspondant
        hashes = (line.split(":") for line in response_text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return int(count)
        return 0



<<<<<<< HEAD
>>>>>>> 5535edcfcaf42465cfd94d5e039d316e59bc8a2e
=======
>>>>>>> 5535edcfcaf42465cfd94d5e039d316e59bc8a2e


