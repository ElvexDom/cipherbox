from application.modules.display_manager import ConsoleUI
from unittest.mock import patch

# ---------------------------
# Test ask_input
# ---------------------------
def test_ask_input(monkeypatch):
    # Simule la saisie utilisateur
    monkeypatch.setattr('builtins.input', lambda _: "test value")
    result = ConsoleUI.ask_input("Entrez quelque chose")
    assert result == "test value"

# ---------------------------
# Test show_menu
# ---------------------------
def test_show_menu(monkeypatch):
    # Simule la saisie utilisateur pour choisir l'option 2
    monkeypatch.setattr('builtins.input', lambda _: "2")
    options = ["Option 1", "Option 2", "Option 3"]
    choice = ConsoleUI.show_menu(options, "Test Menu")
    assert choice == 2

# ---------------------------
# Test show_message
# ---------------------------
def test_show_message(monkeypatch):
    # Simule l'appui sur Entrée
    monkeypatch.setattr('builtins.input', lambda _: "")
    ConsoleUI.show_message("Message test")  # Vérifie que ça s'exécute sans erreur

# ---------------------------
# Test show_title
# ---------------------------
def test_show_title():
    ConsoleUI.show_title("Titre test")  # Vérifie que ça s'exécute sans erreur

# ---------------------------
# Test clear
# ---------------------------
def test_clear():
    with patch('os.system') as mock_system:
        ConsoleUI.clear()
        mock_system.assert_called_once()  # Vérifie que clear a été appelé

# ---------------------------
# Test Logger.log appelé dans ask_input
# ---------------------------
def test_logger_called_in_ask_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "test")
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        ConsoleUI.ask_input("Prompt")
        assert mock_log.called

# ---------------------------
# Test Logger.log appelé dans show_menu
# ---------------------------
def test_logger_called_in_show_menu(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        ConsoleUI.show_menu(["Opt1", "Opt2"], "Menu")
        assert mock_log.called

# ---------------------------
# Test Logger.log appelé dans show_message
# ---------------------------
def test_logger_called_in_show_message(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "")
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        ConsoleUI.show_message("Message")
        assert mock_log.called

# ---------------------------
# Test Logger.log appelé dans show_title
# ---------------------------
def test_logger_called_in_show_title():
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        ConsoleUI.show_title("Titre")
        assert mock_log.called
