import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from application import Zorglangue, Caesar

@pytest.mark.parametrize(

    "inp, expected", 

    [
    # Exemples donnés
    ("Bonjour", "ruojnoB"),
    ("Vive Zorglub !", "eviV bulgroZ !"),
    ("Ceci est un message secret", "iceC tse nu egassem terces"),

    # Ponctuation collée au mot
    ("Bonjour!", "ruojnoB!"),
    ("Hello, world!", "olleH, dlrow!"),
    ("(Salut)", "(tulaS)"),  # parenthèses restent à leur position

    # Majuscules : la majuscule suit la lettre lors de l'inversion (on ne change pas la casse)
    ("Zorglub", "bulgroZ"),
    ("AbC", "CbA"),

    # Espaces multiples et tabulations
    ("Mot   avec  espaces", "toM   ceva  secapse"),

    # Cas avec caractères accentués (unicode)
    ("École française", "elocÉ esiaçnarf"),
    ("àéî ôü", "îéà üô"),  # inversion des lettres unicode

    # Jetons sans lettre (uniquement ponctuation) restent inchangés
    ("!!! ... ?", "!!! ... ?"),

    # Cas vide / espaces seulement
    ("", ""),
    ("   ", "   "),
    ]
)

def test_zorglangue_examples(inp, expected):
    zorglangue = Zorglangue()
    assert zorglangue.reverse_text(inp) == expected

@pytest.mark.parametrize(
    "original_text, key , crypted_text",

    [
        #Check all the keys
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1, "BCDEFGHIJKLMNOPQRSTUVWXYZA"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2, "CDEFGHIJKLMNOPQRSTUVWXYZAB"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3, "DEFGHIJKLMNOPQRSTUVWXYZABC"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4, "EFGHIJKLMNOPQRSTUVWXYZABCD"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5, "FGHIJKLMNOPQRSTUVWXYZABCDE"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 6, "GHIJKLMNOPQRSTUVWXYZABCDEF"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 7, "HIJKLMNOPQRSTUVWXYZABCDEFG"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 8, "IJKLMNOPQRSTUVWXYZABCDEFGH"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 9, "JKLMNOPQRSTUVWXYZABCDEFGHI"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10, "KLMNOPQRSTUVWXYZABCDEFGHIJ"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 11, "LMNOPQRSTUVWXYZABCDEFGHIJK"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 12, "MNOPQRSTUVWXYZABCDEFGHIJKL"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 13, "NOPQRSTUVWXYZABCDEFGHIJKLM"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 14, "OPQRSTUVWXYZABCDEFGHIJKLMN"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 15, "PQRSTUVWXYZABCDEFGHIJKLMNO"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 16, "QRSTUVWXYZABCDEFGHIJKLMNOP"),            
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 17, "RSTUVWXYZABCDEFGHIJKLMNOPQ"),             
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 18, "STUVWXYZABCDEFGHIJKLMNOPQR"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 19, "TUVWXYZABCDEFGHIJKLMNOPQRS"),            
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 20, "UVWXYZABCDEFGHIJKLMNOPQRST"), 
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 21, "VWXYZABCDEFGHIJKLMNOPQRSTU"), 
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 22, "WXYZABCDEFGHIJKLMNOPQRSTUV"), 
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 23, "XYZABCDEFGHIJKLMNOPQRSTUVW"), 
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 24, "YZABCDEFGHIJKLMNOPQRSTUVWX"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25, "ZABCDEFGHIJKLMNOPQRSTUVWXY"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        
        # Basic shift
        ("abc", 1, "bcd"),
        ("xyz", 2, "zab"),
        ("hello", 3, "khoor"),

        # Uppercase preserved
        ("ABC", 1, "BCD"),
        ("XYZ", 3, "ABC"),
        ("Hello", 3, "Khoor"),

        # Mixed case
        ("HeLLo", 2, "JgNNq"),

        # Spaces and punctuation stay unchanged
        ("Hello, World!", 3, "Khoor, Zruog!"),
        ("Salut !", 1, "Tbmvu !"),

         # Negative shift
        ("bcd", -1, "abc"),
        ("abc", -3, "xyz"),
        ("Hello", -5, "Czggj"),

        # Shift > 26
        ("abc", 27, "bcd"),      # 27 = 1 mod 26
        ("xyz", 52, "xyz"),      # 52 = 0 mod 26
        ("Hello", 57, "Mjqqt"),  # 57 = 5 mod 26

        # Empty string
        ("", 10, ""),

        # no changes : 
        ("le monde est beau", 0, "le monde est beau"),
        # Jetons sans lettre (uniquement ponctuation) restent inchangés
        ("!!! ... ?", 6, "!!! ... ?"),

        # Cas vide / espaces seulement
        ("", 16, ""),
        ("   ", 23, "   "),

        # No changes in non-letter
        ("1234!?", 4, "1234!?")
    ]

)

def test_caesar_exemple(original_text:str, crypted_text:str, key:int):
    caesar = Caesar()
    assert caesar.crypt_text(original_text, key, encrypt=True) == crypted_text
    assert caesar.crypt_text(crypted_text, key, decrypt=True) == original_text