# Programa de testing en Python para propbar el detector de palindromos
import pytest
from demo_palindromo import es_palindromo

# --- Tests para la función es_palindromo ---
def test_es_palindromo_palabra_simple():
    '''
        Verifica que la función detecte un palíndromo de palabra simple.
        Ejemplo: "oso"
    '''
    assert es_palindromo("oso") is True
def test_es_palindromo_frase_con_espacios():
    """
    Verifica que la función detecte un palíndromo en una frase con espacios,
    ignorando dichos espacios. Ej: "anilina" -> "anilin a"
    """
    assert es_palindromo("anilin a") is True

def test_es_palindromo_mayusculas_y_minusculas():
    """
    Verifica que la función detecte un palíndromo ignorando mayúsculas y minúsculas.
    Ej: "Reconocer"
    """
    assert es_palindromo("Reconocer") is True

def test_es_palindromo_frase_compleja():
    """
    Verifica que la función detecte un palíndromo en una frase compleja,
    ignorando espacios y puntuación. Ej: "Anita lava la tina"
    """
    assert es_palindromo("Anita lava la tina") is True

def test_es_palindromo_con_numeros():
    """
    Verifica que la función detecte un palíndromo que contenga números.
    Ej: "Amanece con nEceMAna"
    """
    assert es_palindromo("Amanece con nEceMAna") is True

def test_es_palindromo_cadena_vacia():
    """
    Verifica que una cadena vacía sea considerada un palíndromo.
    """
    assert es_palindromo("") is True

def test_es_palindromo_un_caracter():
    """
    Verifica que una cadena con un solo carácter sea un palíndromo.
    """
    assert es_palindromo("a") is True
    assert es_palindromo("Z") is True
    assert es_palindromo("7") is True

# Casos de prueba para NO palíndromos (inválidos)
def test_es_palindromo_palabra_no_palindromo():
    """
    Verifica que la función detecte correctamente una palabra que no es palíndromo.
    Ej: "hola"
    """
    assert es_palindromo("hola") is False

def test_es_palindromo_frase_no_palindromo():
    """
    Verifica que la función detecte correctamente una frase que no es palíndromo.
    Ej: "Esto no es un palindromo"
    """
    assert es_palindromo("Esto no es un palindromo") is False

def test_es_palindromo_con_simbolos_no_alfanumericos():
    """
    Verifica que la función maneje frases con símbolos y no los considere.
    Ej: "¿Qué tal?"
    """
    assert es_palindromo("¿Qué tal?") is False

def test_es_palindromo_no_string():
    """
    Verifica que la función retorne False si la entrada no es una cadena de texto.
    """
    assert es_palindromo(123) is False
    assert es_palindromo(None) is False
    assert es_palindromo(["lista"]) is False
    assert es_palindromo(True) is False

def test_es_palindromo_solo_simbolos():
    """
    Verifica que una cadena con solo símbolos sea tratada como un palíndromo vacío
    después de la limpieza.
    """
    assert es_palindromo("!@#$%^&*()") is True # Se convierte en "" después de limpiar