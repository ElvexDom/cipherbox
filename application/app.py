import logging
import re
from unidecode import unidecode

# Configuration du logging
logging.basicConfig(filename='text_transformer.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Caesar:
    
    def crypt_text(self,text: str, key: str, encrypt=False, decrypt=False):
        """
        Function for encrypting a text with a given key.

        Returns:
            Encrypted text.
        """

        try:                
            unidecode_text =unidecode(text)
            alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
            
            table_alphabet = re.findall(r'[A-Za-z]', alphabet)
            key = int(key)%26
            if encrypt:
                key = key
            elif decrypt:
                key = 26 - key
            table_converted = table_alphabet[key*2:] + table_alphabet[:key*2]
            print(table_converted)
            character = ""
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
            logging.error(str(e))


class Zorglangue:
    
    def __init__(self):
        logging.debug("=== Instance de Zorglangue créée avec succès ===")
        pass

    def reverse_text(self, text):
        """
        Function for reversing only the letters in a given text. The order in which the words appear remains the same.

        Returns:
            Identical text, with words reversed.
        """

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
            logging.error(str(e))
            
if __name__ == "__main__":
    # logging.info('=== Zorglangue a démarré avec succès (lancé depuis __main__) ===')
    # zorlangue = Zorglangue()
    # text = input('Entrez un texte pour le convertir en Zorglangue: ')
    # zorglangue_text = zorlangue.reverse_text(text)
    # print(f"Texte converti en Zorglangue: {zorglangue_text}")
    # logging.info('=== Zorglangue a fini avec succès (lancé depuis __main__) ===')
    caesar = Caesar()
    caesar.encrpyt_text('PapA, est un "rolling Stône" !', '5')
