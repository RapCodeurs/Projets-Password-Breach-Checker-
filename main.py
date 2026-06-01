from hibp import get_pwned_count

def main():
    password = input("Entrer un mot de passe: ")
    count = get_pwned_count(password)

    if count:
        print(f"Ce mot de passe {count} a été trouvé dans des fuites de données. Vous devriez envisager de le modifier.")
    else:
        print("Ce mot de passe n'a pas été trouvé dans aucune fuite de données connue. Bon travail!")

if __name__ == "__main__":
    main()

