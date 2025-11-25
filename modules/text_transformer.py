import logging
import re
from unidecode import unidecode
from cryptography.fernet import Fernet

logging.basicConfig(filename='text_transformer.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TextTransformer:
    
    @staticmethod
    def zorglangue(text: str):
        try:
            words = re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ]+', text)
            sentence = re.findall(r'[A-Za-zÀ-ÖØ-öø-ÿ]+|[^A-Za-zÀ-ÖØ-öø-ÿ]+', text)
            for word in sentence:
                if word in words:
                    index = sentence.index(word)
                    REWord = word[::-1]
                    sentence[index] = REWord
            reversed_text = ''.join(sentence)
            return reversed_text
        
        except Exception as e:
            logging.error(f"Erreur inattendue: {e}")

    @staticmethod
    def caesar(text: str, key: str, mode: str):
        try:                
            unidecode_text =unidecode(text)
            table_alphabet = list("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
            key = int(key)%26
            if mode == "decrypt":
                key = -key
                # key = 26 - key
            table_converted = table_alphabet[key*2:] + table_alphabet[:key*2]
            encoded_text = ""
            for c in unidecode_text:
                if c in table_alphabet:
                    index = table_alphabet.index(c)
                    character = table_converted[index]
                else:
                    character = c 
                encoded_text += character
            return encoded_text
        
        except Exception as e:
            logging.error(f"Erreur inattendue: {e}")


    @staticmethod
    def crypto(message=None, key=None, mode="generate_key"):
        try:
            if mode == "generate_key":
                return Fernet.generate_key()
            elif mode == "encrypt":
                if message is None or key is None:
                    raise ValueError("Pour le chiffrement, le message et la clé sont requis")
                f = Fernet(key)
                return f.encrypt(message.encode('utf-8'))
            elif mode == "decrypt":
                if message is None or key is None:
                    raise ValueError("Pour le déchiffrement, le message et la clé sont requis")
                f = Fernet(key)
                return f.decrypt(message).decode('utf-8')
            else:
                raise ValueError("Mode invalide. Choisir 'generate_key', 'encrypt' ou 'decrypt'")
            
        except Exception as e:
            logging.error(f"Erreur inattendue: {e}")
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