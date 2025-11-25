import os

class ConsoleUI:
    """Classe pour gérer l'affichage et l'interaction utilisateur dans le terminal."""

    @staticmethod
    def clear():
        """Efface l'écran du terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def show_title(title: str):
        """Affiche un titre encadré centré."""
        ConsoleUI.clear()
        width = max(50, len(title) + 10)
        print("=" * width)
        print(title.center(width))
        print("=" * width)

    @staticmethod
    def show_menu(options: list, title: str = "MENU"):
        """
        Affiche un menu avec des options.
        :param options: liste de chaînes, chaque option du menu
        :param title: titre du menu
        :return: choix de l'utilisateur
        """
        while True:
            ConsoleUI.clear()
            width = max(50, len(title) + 10)
            print("=" * width)
            print(title.center(width))
            print("=" * width + "\n")
            for idx, option in enumerate(options, start=1):
                print(f"[{idx}] {option}")
            print("=" * width)

            choice = input("Entrez le numéro du choix : ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return int(choice)
            else:
                print("Choix invalide. Réessayez.")
                input("Appuyez sur Entrée pour continuer...")

    @staticmethod
    def show_message(message: str):
        """Affiche un message encadré."""
        ConsoleUI.clear()
        width = max(50, len(message) + 10)
        print("!" * width)
        print("!" + " " * (width - 2) + "!")
        print("!" + message.center(width - 2) + "!")
        print("!" + " " * (width - 2) + "!")
        print("!" * width)
        input("Appuyez sur Entrée pour continuer...")

    @staticmethod
    def ask_input(prompt: str):
        """Demande une saisie à l'utilisateur et retourne la chaîne."""
        ConsoleUI.clear()
        return input(f"{prompt} : ").strip()
