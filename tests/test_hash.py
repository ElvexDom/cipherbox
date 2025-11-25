import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from application import Zorglangue, Caesar
from utils import crypto_tools

@pytest.mark.parametrize(

    "plain_text",

    [
    # Exemples donnés
    ("Bonjour"),
    ("Vive Zorglub !"),
    ("Ceci est un message secret"),

    # Ponctuation collée au mot
    ("Bonjour!"),
    ("Hello, world!"),
    ("(Salut)"),  # parenthèses restent à leur position

    # Majuscules : la majuscule suit la lettre lors de l'inversion (on ne change pas la casse)
    ("Zorglub"),
    ("AbC"),

    # Espaces multiples et tabulations
    ("Mot   avec  espaces"),

    # Cas avec caractères accentués (unicode)
    ("École française"),
    ("àéî ôü"),  # inversion des lettres unicode

    # Jetons sans lettre (uniquement ponctuation) restent inchangés
    ("!!! ... ?"),

    # Cas vide / espaces seulement
    (""),
    ("   "),
    ]
)

def test_crypto(plain_text):
    key= crypto_tools.generate_key()
    ciphertext = crypto_tools.encrypt(plain_text,key)
    assert crypto_tools.decrypt(ciphertext,key) == plain_text
