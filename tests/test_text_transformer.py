from application.modules.crypto_tools import TextTransformer
from unittest.mock import patch

# ---------------------------
# Test zorglangue
# ---------------------------
def test_zorglangue_basic():
    text = "Bonjour le monde !"
    result = TextTransformer.zorglangue(text)
    # Chaque mot inversé
    assert result.startswith("ruojnoB") and "!" in result

def test_zorglangue_logger():
    text = "Salut"
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        TextTransformer.zorglangue(text)
        assert mock_log.called

# ---------------------------
# Test caesar
# ---------------------------
def test_caesar_encrypt_decrypt():
    text = "Hello"
    key = "3"
    encrypted = TextTransformer.caesar(text, key, mode="encrypt")
    decrypted = TextTransformer.caesar(encrypted, key, mode="decrypt")
    assert decrypted.lower() == text.lower()  # unidecode ignore les accents

def test_caesar_logger():
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        TextTransformer.caesar("Test", "5", mode="encrypt")
        assert mock_log.called

# ---------------------------
# Test Fernet crypto
# ---------------------------
def test_crypto_generate_key():
    key = TextTransformer.crypto(mode="generate_key")
    assert isinstance(key, bytes)

def test_crypto_encrypt_decrypt():
    message = "Secret message"
    key = TextTransformer.crypto(mode="generate_key")
    cipher_text = TextTransformer.crypto(message=message, key=key, mode="encrypt")
    decrypted_text = TextTransformer.crypto(message=cipher_text, key=key, mode="decrypt")
    assert decrypted_text == message

def test_crypto_logger():
    key = TextTransformer.crypto(mode="generate_key")
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        TextTransformer.crypto(message="Test", key=key, mode="encrypt")
        assert mock_log.called

# ---------------------------
# Test erreurs
# ---------------------------
def test_caesar_invalid_key():
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        result = TextTransformer.caesar("Test", "invalid", mode="encrypt")
        assert result is None
        assert mock_log.called

def test_crypto_invalid_mode():
    with patch('application.utils.logging_service.Logger.log') as mock_log:
        result = TextTransformer.crypto(message="Test", key=b"dummy", mode="invalid")
        assert result is None
        assert mock_log.called
