import os
import sys
from application.utils import Logger

class ConsoleUI:
    """
    Interface utilisateur pour la console CLI.
    
    Méthodes disponibles :
        - clear() : Efface l'écran.
        - show_title(title) : Affiche un titre centré.
        - show_menu(options, title) : Affiche un menu et retourne le choix utilisateur.
        - show_message(message) : Affiche un message encadré.
        - ask_input(prompt) : Demande une saisie utilisateur.
    """

    @staticmethod
    def clear():
        """Efface l'écran de la console."""
        os.system('cls' if os.name == 'nt' else 'clear')
        Logger.log("debug", "ConsoleUI: Écran effacé")

    @staticmethod
    def show_title(title: str):
        """
        Affiche un titre centré sur l'écran.
        
        Args:
            title (str): Le titre à afficher.
        """
        ConsoleUI.clear()
        Logger.log("info", f"ConsoleUI: Affichage du titre: {title}")
        width = max(50, len(title) + 10)
        print("=" * width)
        print(title.center(width))
        print("=" * width)

    @staticmethod
    def show_menu(options: list, title: str = "MENU") -> int:
        """
        Affiche un menu et retourne le choix de l'utilisateur.
        
        Args:
            options (list): Liste des options du menu.
            title (str): Titre du menu.
        
        Returns:
            int: Numéro de l'option choisie (1-based index).
        """
        Logger.log("info", f"ConsoleUI: Affichage menu '{title}' avec options {options}")
        while True:
            ConsoleUI.clear()
            width = max(50, len(title) + 10)
            print("=" * width)
            print(title.center(width))
            print("=" * width + "\n")
            for idx, option in enumerate(options, start=1):
                print(f"[{idx}] {option}")
            print("=" * width)

            try:
                choice = input("Entrez le numéro du choix : ").strip()
                if choice.isdigit():
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(options):
                        Logger.log("info", f"ConsoleUI: Choix utilisateur = {choice_num}")
                        return choice_num
            except KeyboardInterrupt:
                Logger.log("info", "ConsoleUI: Interruption clavier")
                ConsoleUI.clear()
                sys.exit()

    @staticmethod
    def show_message(message: str):
        """
        Affiche un message encadré et attend que l'utilisateur appuie sur Entrée.
        
        Args:
            message (str): Le message à afficher.
        """
        Logger.log("info", f"ConsoleUI: Affichage message: {message}")
        ConsoleUI.clear()
        width = max(50, len(message) + 10)
        print("!" * width)
        print("!" + " " * (width - 2) + "!")
        print("!" + message.center(width - 2) + "!")
        print("!" + " " * (width - 2) + "!")
        print("!" * width)
        try:
            input("Appuyez sur Entrée pour continuer...")
        except KeyboardInterrupt:
            Logger.log("info", "ConsoleUI: Interruption clavier lors du message")
            sys.exit()
        ConsoleUI.clear()

    @staticmethod
    def ask_input(prompt: str) -> str:
        """
        Demande une saisie utilisateur et la retourne.
        
        Args:
            prompt (str): Le texte de la demande.
        
        Returns:
            str: La saisie utilisateur.
        """
        ConsoleUI.clear()
        Logger.log("info", f"ConsoleUI: Demande input utilisateur: {prompt}")
        try:
            user_input = input(f"{prompt} : ").strip()
            Logger.log("info", f"ConsoleUI: Utilisateur a entré: {user_input}")
            return user_input
        except KeyboardInterrupt:
            Logger.log("info", "ConsoleUI: Interruption clavier lors de l'input")
            ConsoleUI.clear()
            sys.exit()
