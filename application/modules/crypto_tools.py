import re
from unidecode import unidecode
from cryptography.fernet import Fernet
from application.utils import Logger

class TextTransformer:
    """
    Classe utilitaire pour la transformation et le chiffrement de texte.
    
    Méthodes disponibles :
        - zorglangue(text) : renverse chaque mot du texte.
        - caesar(text, key, mode) : chiffrement/déchiffrement de type César.
        - crypto(message=None, key=None, mode="generate_key") : chiffrement/déchiffrement Fernet.
    """

    @staticmethod
    def zorglangue(text: str) -> str:
        """
        Transforme un texte en Zorglangue en inversant chaque mot.
        
        Args:
            text (str): Le texte à transformer.
        
        Returns:
            str: Texte transformé en Zorglangue, ou None en cas d'erreur.
        """
        Logger.log("info", f"Zorglangue: Début traitement du texte: {text}")
        try:
            words = re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ]+', text)
            sentence = re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ]+|[^A-Za-zÀ-ÖØ-öø-ÿ]+', text)
            for i, word in enumerate(sentence):
                if re.match(r'[A-Za-zÀ-ÖØ-öø-ÿ]+', word):
                    sentence[i] = word[::-1]
            reversed_text = ''.join(sentence)
            Logger.log("info", f"Zorglangue: Texte transformé: {reversed_text}")
            return reversed_text
        except Exception as e:
            Logger.log("exception", f"Zorglangue: Erreur inattendue: {e}")
            return None

    @staticmethod
    def caesar(text: str, key: str, mode: str) -> str:
        """
        Chiffre ou déchiffre un texte selon le code César.
        
        Args:
            text (str): Le texte à chiffrer/déchiffrer.
            key (str): Clé de décalage (nombre entier).
            mode (str): "encrypt" pour chiffrer, "decrypt" pour déchiffrer.
        
        Returns:
            str: Texte transformé, ou None en cas d'erreur.
        """
        Logger.log("info", f"Caesar: Début mode={mode}, clé={key}, texte={text}")
        try:                
            unidecode_text = unidecode(text)
            table_alphabet = list("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
            key = int(key) % 26
            shift = key if mode == "encrypt" else -key
            table_converted = table_alphabet[shift*2:] + table_alphabet[:shift*2]
            encoded_text = ""
            for c in unidecode_text:
                if c in table_alphabet:
                    index = table_alphabet.index(c)
                    character = table_converted[index]
                else:
                    character = c 
                encoded_text += character
            Logger.log("info", f"Caesar: Texte transformé: {encoded_text}")
            return encoded_text
        except Exception as e:
            Logger.log("exception", f"Caesar: Erreur inattendue: {e}")
            return None

    @staticmethod
    def crypto(message=None, key=None, mode="generate_key"):
        """
        Chiffre ou déchiffre un texte avec Fernet, ou génère une clé.
        
        Args:
            message (str, optional): Le texte à chiffrer/déchiffrer.
            key (bytes, optional): La clé Fernet.
            mode (str): "generate_key", "encrypt" ou "decrypt".
        
        Returns:
            bytes ou str: Résultat du chiffrement/déchiffrement, ou None en cas d'erreur.
        """
        Logger.log("info", f"Fernet: Début mode={mode}, message={message}, key={key}")
        try:
            if mode == "generate_key":
                generated_key = Fernet.generate_key()
                Logger.log("info", f"Fernet: Clé générée: {generated_key}")
                return generated_key
            elif mode == "encrypt":
                if message is None or key is None:
                    raise ValueError("Message et clé requis pour chiffrer")
                f = Fernet(key)
                cipher_text = f.encrypt(message.encode('utf-8'))
                Logger.log("info", f"Fernet: Texte chiffré: {cipher_text}")
                return cipher_text
            elif mode == "decrypt":
                if message is None or key is None:
                    raise ValueError("Message et clé requis pour déchiffrer")
                f = Fernet(key)
                decrypted_text = f.decrypt(message).decode('utf-8')
                Logger.log("info", f"Fernet: Texte déchiffré: {decrypted_text}")
                return decrypted_text
            else:
                raise ValueError("Mode invalide. Choisir 'generate_key', 'encrypt' ou 'decrypt'")
        except Exception as e:
            Logger.log("exception", f"Fernet: Erreur inattendue: {e}")
            return None

if __name__ == "__main__":
    message = "Bonjour le monde !"
    print("Message original :", message)

    # César
    caesar_text = TextTransformer.caesar(message, 5, mode="encrypt")
    print("César chiffré :", caesar_text)
    caesar_decrypted = TextTransformer.caesar(caesar_text, 5, mode="decrypt")
    print("César déchiffré :", caesar_decrypted)

    # Zorglangue
    zorg_text = TextTransformer.zorglangue(message)
    print("Zorglangue chiffré :", zorg_text)
    zorg_decrypted = TextTransformer.zorglangue(zorg_text)
    print("Zorglangue déchiffré :", zorg_decrypted)

    # Crypto Fernet
    key = TextTransformer.crypto(mode="generate_key")
    print("Clé générée :", key.decode('utf-8'))
    cipher_text = TextTransformer.crypto(message=message, key=key, mode="encrypt")
    print("Fernet chiffré :", cipher_text.decode('utf-8'))
    decrypted_text = TextTransformer.crypto(message=cipher_text, key=key, mode="decrypt")
    print("Fernet déchiffré :", decrypted_text)