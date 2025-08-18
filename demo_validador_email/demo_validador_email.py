# Código demo para validador de email
import re # re=Regular Expression, herramienta para trabajar con patrones de texto complejo

def validar_email(email):
'''Valida si una cadena de texto tiene el formato basico de un email.
Este validador es una version simplificada para propositos de demostracion, no cubre todas las
comolejidades del estandar RFC'''
    if not isinstance(email, str):
        return False #No es una cadena de texto

# validador_email.py
import re

def validar_email(email):
    """
    Valida si una cadena de texto tiene el formato básico de un email.
    Este validador es una versión simplificada para propósitos de demostración.
    No cubre todas las complejidades del estándar RFC 5322.
    """
    if not isinstance(email, str):
        return False # No es una cadena de texto

    # Expresión regular simplificada para un formato básico de email
    # ^[a-zA-Z0-9._%+-]+ : Inicio de la cadena, usuario (letras, nums, ., _, %, +, -)
    # @                 : El símbolo arroba
    # [a-zA-Z0-9.-]+    : Dominio (letras, nums, ., -)
    # \.                : Un punto literal
    # [a-zA-Z]{2,}$     : Extensión (al menos 2 letras, fin de la cadena)
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, email): #re.match busca el patron al inicio de la cadena
        return True
            else:
                return False

    # Aquí irá la aplicación del patrón
