from application.modules import TextTransformer, ConsoleUI
from application.utils import Logger

def start():
    """
    Boucle principale de l'application.

    Affiche le menu des outils, récupère les choix de l'utilisateur,
    exécute la transformation/chiffrement correspondante et affiche le résultat.
    """
    Logger.log("info", "Démarrage de l'application")
    
    while True:
        try:
            ConsoleUI.show_title("OUTILS DISPONIBLES")
            choice_tool = ConsoleUI.show_menu(
                ["Zorglangue", 
                 "Code César", 
                 "Cryptographie", 
                 "Quitter"],
                title="Choisis un outil"
            )
            Logger.log("info", f"Choix de l'outil: {choice_tool}")

            if choice_tool == 1:  # Zorglangue
                text = ConsoleUI.ask_input("Entre un texte pour le convertir en Zorglangue")
                Logger.log("info", f"Zorglangue: Texte utilisateur: {text}")
                encrypted_text = TextTransformer.zorglangue(text)
                Logger.log("info", f"Zorglangue: Texte transformé: {encrypted_text}")
                ConsoleUI.show_message(f"Texte transformé en Zorglangue : {encrypted_text}")

            elif choice_tool == 2:  # Code César
                action = ConsoleUI.show_menu(["Chiffrer", "Déchiffrer"], title="Veux-tu chiffrer ou déchiffrer ?")
                Logger.log("info", f"César: Action choisie: {action}")

                text = ConsoleUI.ask_input("Écris ton texte")
                Logger.log("info", f"César: Texte utilisateur: {text}")

                key = ""
                while not key.isdigit():
                    key = ConsoleUI.ask_input("Donne la clé de décalage (nombre)")
                    if not key.isdigit():
                        Logger.log("warning", f"César: Clé invalide entrée: {key}")

                if action == 1:  # Chiffrer
                    encrypted_text = TextTransformer.caesar(text, int(key), mode="encrypt")
                    Logger.log("info", f"César: Texte chiffré: {encrypted_text}")
                    ConsoleUI.show_message(f"Texte chiffré : {encrypted_text}")
                else:  # Déchiffrer
                    decrypted_text = TextTransformer.caesar(text, int(key), mode="decrypt")
                    Logger.log("info", f"César: Texte déchiffré: {decrypted_text}")
                    ConsoleUI.show_message(f"Texte déchiffré : {decrypted_text}")

            elif choice_tool == 3:  # Cryptographie (Fernet)
                action = ConsoleUI.show_menu(["Chiffrer", "Déchiffrer"], title="Veux-tu chiffrer ou déchiffrer ?")
                Logger.log("info", f"Fernet: Action choisie: {action}")

                if action == 1:  # Chiffrer
                    key_choice = ConsoleUI.show_menu(
                        ["Générer une clé aléatoire", "Fournir une clé"],
                        title="Choix de la clé"
                    )
                    Logger.log("info", f"Fernet: Méthode clé choisie: {key_choice}")

                    if key_choice == 1:
                        key = TextTransformer.crypto(mode="generate_key")
                        Logger.log("info", f"Fernet: Clé générée: {key}")
                        ConsoleUI.show_message(f"Clé générée : {key.decode('utf-8')}")
                    else:
                        key_input = ConsoleUI.ask_input("Entre ta clé secrète (Base64)")
                        key = key_input.encode()
                        Logger.log("info", f"Fernet: Clé utilisateur fournie")

                    message = ConsoleUI.ask_input("Entre le message à chiffrer")
                    Logger.log("info", f"Fernet: Message utilisateur: {message}")
                    cipher_text = TextTransformer.crypto(message=message, key=key, mode="encrypt")
                    Logger.log("info", f"Fernet: Texte chiffré: {cipher_text}")
                    ConsoleUI.show_message(f"Texte chiffré : {cipher_text.decode('utf-8')}")

                else:  # Déchiffrer
                    cipher_text = ConsoleUI.ask_input("Entre ton message chiffré").encode()
                    key_input = ConsoleUI.ask_input("Entre ta clé secrète").encode()
                    Logger.log("info", f"Fernet: Message et clé pour déchiffrement fournis")
                    decrypted_text = TextTransformer.crypto(message=cipher_text, key=key_input, mode="decrypt")
                    Logger.log("info", f"Fernet: Texte déchiffré: {decrypted_text}")
                    ConsoleUI.show_message(f"Texte déchiffré : {decrypted_text}")

            else:  # Quitter
                Logger.log("info", "Quitter l'application")
                ConsoleUI.show_message("Au revoir !")
                break

        except Exception as e:
            Logger.log("exception", f"Erreur inattendue dans la boucle principale: {e}")
            ConsoleUI.show_message("Une erreur est survenue, consultez le fichier de logs.")

if __name__ == "__main__":
    start()
