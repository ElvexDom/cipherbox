from modules import TextTransformer
from modules import ConsoleUI

def start():
    while True:
        ConsoleUI.show_title("JEUX DISPONIBLES")
        choice_game = ConsoleUI.show_menu(
            ["Zorglangue", "Code César", "Cryptographie d’un texte", "Quitter"],
            title="Choisis ton jeu"
        )

        if choice_game == 1:  # Zorglangue
            text = ConsoleUI.ask_input("Entre un texte pour le convertir en Zorglangue")
            encrypted_text = TextTransformer.zorglangue(text)
            ConsoleUI.show_message(f"Zorglangue chiffré : {encrypted_text}")

        elif choice_game == 2:  # Code César
            text = ConsoleUI.ask_input("Écris ton texte")
            key = ""
            while not key.isdigit():
                key = ConsoleUI.ask_input("Donne la clé de décalage (nombre)")
            action = ConsoleUI.show_menu(["Chiffrer", "Déchiffrer"], title="Veux-tu chiffrer ou déchiffrer ?")

            if action == 1:  # Chiffrer
                encrypted_text = TextTransformer.caesar(text, key, mode="encrypt")
                ConsoleUI.show_message(f"César chiffré : {encrypted_text}")
            else:  # Déchiffrer
                decrypted_text = TextTransformer.caesar(text, key, mode="decrypt")
                ConsoleUI.show_message(f"César déchiffré : {decrypted_text}")

        elif choice_game == 3:  # Cryptographie (Fernet)
            action = ConsoleUI.show_menu(["Chiffrer", "Déchiffrer"], title="Veux-tu chiffrer ou déchiffrer ?")

            if action == 1:
                key_choice = ConsoleUI.show_menu(
                    ["Générer une clé aléatoire", "Fournir une clé"],
                    title="Choix de la clé"
                )
                if key_choice == 1:
                    key = TextTransformer.crypto(mode="generate_key")
                    ConsoleUI.show_message(f"Clé générée : {key.decode('utf-8')}")
                else:
                    key_input = ConsoleUI.ask_input("Entre ta clé secrète (Base64)")
                    key = key_input.encode()

                message = ConsoleUI.ask_input("Choisis un message à chiffrer")
                cipher_text = TextTransformer.crypto(message=message, key=key, mode="encrypt")
                ConsoleUI.show_message(f"Fernet chiffré : {cipher_text.decode('utf-8')}")

            else:  # Déchiffrer
                cipher_text = ConsoleUI.ask_input("Entre ton message chiffré").encode()
                key_input = ConsoleUI.ask_input("Entre ta clé secrète").encode()
                decrypted_text = TextTransformer.crypto(message=cipher_text, key=key_input, mode="decrypt")
                ConsoleUI.show_message(f"Fernet déchiffré : {decrypted_text}")

        else:  # Quitter
            ConsoleUI.show_message("Au revoir !")
            break

if __name__ == "__main__":
    start()
