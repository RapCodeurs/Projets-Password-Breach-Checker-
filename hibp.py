import hashlib
import requests # pyright: ignore[reportMissingModuleSource]



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


