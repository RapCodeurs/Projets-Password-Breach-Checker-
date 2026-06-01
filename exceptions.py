class HIBPError(Exception):
    """Exceptions de base."""
    pass

class APIConnectionError(HIBPError):
    """Erreur de connexion à l'API."""
    pass

class APIResponseError(HIBPError):
    """Réponse de l'API invalide."""
    pass

