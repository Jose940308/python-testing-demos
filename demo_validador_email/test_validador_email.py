# Codigo de test del validador de emails
import pytest
from demo_validador_email import validar_email

# --- Comienzan los test para validar_email ---

# Casos de prueba para emails válidos
def test_validar_email_valido_simple():    ''' Verifica un email válido con formato estándar (Es la definicion de una función de prueba)'''
assert validar_email("test@example.com") is True

def test_validar_email_valido_subdominio(): '''Verifica un email válido con subdominio'''
assert validar_email("nombre.apellido@sub.cominio.co") is True

def test_validar_email_valido_numeros(): '''Verifica un email válido co números en usuario y dominio'''
assert validar_email("usuario123@dominio456.net") is True

def test_validar_email_valido_guiones(): '''Verifica un email válido con guiones en usuario y dominio'''
assert validar_email("user-name@ndomain-name.org") is True

def test_validar_email_valido_guion_bajo(): '''Verifica un email válido con guiones bajos en usuario'''
assert validar_email("user_name@ndomain.info") is True

def test_validar_email_valido_mas_caracteres_especiales_usuario(): '''Verifica email váido con %, +, . en el usuario'''
assert validar_email("my.email+alias%test@example.com") is True

# Casos de prueba para emails inválidos
def test_validar_email_invalido_sin_arroba():
    """Verifica un email inválido sin el símbolo @."""
    assert validar_email("testexample.com") is False

def test_validar_email_invalido_sin_dominio():
    """Verifica un email inválido sin dominio."""
    assert validar_email("test@.com") is False

def test_validar_email_invalido_sin_extension():
    """Verifica un email inválido sin extensión."""
    assert validar_email("test@example") is False

def test_validar_email_invalido_extension_corta():
    """Verifica un email inválido con extensión de menos de 2 caracteres."""
    assert validar_email("test@example.c") is False

def test_validar_email_invalido_doble_arroba():
    """Verifica un email inválido con doble arroba."""
    assert validar_email("test@@example.com") is False

def test_validar_email_invalido_espacios():
    """Verifica un email inválido con espacios."""
    assert validar_email("test @example.com") is False
    assert validar_email("test@ example.com") is False

def test_validar_email_invalido_caracteres_no_permitidos():
    """Verifica un email inválido con caracteres no permitidos en el usuario/dominio."""
    assert validar_email("test!@example.com") is False
    assert validar_email("test@examp!e.com") is False

def test_validar_email_invalido_cadena_vacia():
    """Verifica una cadena vacía."""
    assert validar_email("") is False

def test_validar_email_invalido_no_string():
    """Verifica que la función maneje entradas que no son strings."""
    assert validar_email(123) is False
    assert validar_email(None) is False
    assert validar_email(["test@example.com"]) is False
