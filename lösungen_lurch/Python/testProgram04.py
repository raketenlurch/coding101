set_benutzername = "raketenlurch"
set_password = "test1234"

while True:
    benutzername = input("Benutzer*innenname:")
    passwort = input("Passwort:")

    if benutzername == set_benutzername:
        print("Login erfolgreich!")
        break
    else:
        print("Daten falsch. Nochmal versuchen.")
        continue
