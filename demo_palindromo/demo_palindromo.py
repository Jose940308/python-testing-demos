# DEMO de un programa de identificación de palindromos
import re #re (regular expressions) es un modulo para expresiones regulares, util para limpiar texto

#Definicion de funcion principal
#frase = input()
def es_palindromo(frase) :
    '''
    Verifica si una frase o palabra es un palindromo.
    Ignora espacios, puntuacion y minusculas/mayusculas.

    Args:
        frase (str): La cadena de texto a verificar

    Retunrs:
        bool: True si la frase es un palindromo, Flase en caso contrario
    '''
#Paso 1. Validar que la entrada sea una cadena de texto
    if not isinstance(frase, str):
        return False #Si no es string, no puede ser un palindromo

#Paso 2. Limpiar la frase. Convertir a minusculas para ignorar mayúsculas/minúsculas
    frase_limpia = frase.lower()
    frase_limpia = re.sub (r'[^a-z0-9]', '', frase_limpia)
    '''
        Elimina caracteres no alfanuméricos (espacios, puntos, etc)
        re.sub(patron, reemplazo, cadena) reemplaza todas las condiciones del patrón
        [^a-z0-9] es un patrón que coincide con CUALQUIER COSA QUE NO SEA una letra (a-z) o un número (0-9)
    '''
#Paso 3: Comparar la frase limpia con su version invertida
    return frase_limpia == frase_limpia[::-1]
    '''
        [::-1] es una "rebanada" (slice) de Python que invierte la cadena.
        Si la frase limpia es igual a su versión invertida, es un palindromo.
    '''