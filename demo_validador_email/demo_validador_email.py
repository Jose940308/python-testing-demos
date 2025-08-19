# Código demo validador de eimail

import re # Importamos el módulo de expresiones regulares

def validar_email(email):
    """
    Valida si una cadena de texto tiene el formato básico de un email.
    Este validador es una versión simplificada para propósitos de demostración.
    No cubre todas las complejidades del estándar RFC 5322.

    Un formato básico aceptable es: usuario@dominio.extension
    Donde:
    - 'usuario' puede contener letras, números, puntos, guiones y guiones bajos.
    - 'dominio' puede contener letras, números y guiones.
    - 'extension' debe tener al menos 2 letras (ej. .com, .org, .net).
    """
    # Paso 1: Validar que la entrada sea una cadena de texto (string)
    if not isinstance(email, str):
        return False # Si no es string, no es un email válido

    # Paso 2: Definir la expresión regular (regex) para el patrón de email
    ''' ^                  : Inicio de la cadena
    [a-zA-Z0-9._%+-]+  : Una o más letras, números, puntos, guiones bajos, porcentajes, signos más o guiones (usuario)
    @                  : El símbolo arroba
    [a-zA-Z0-9.-]+     : Una o más letras, números, puntos o guiones (dominio)
    \.                 : Un punto literal (escapado con \)
    [a-zA-Z]{2,}$      : Extensión de al menos dos letras hasta el final de la cadena
    '''
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" 

    # Paso 3: Usar re.match para buscar el patrón al inicio de la cadena
    if re.match(patron, email):
        return True # Si el patrón coincide, el email es válido
    else:
        return False # Si el patrón no coincide, el email es inválido
