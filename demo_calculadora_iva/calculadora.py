def calcular_iva(monto_base, tasa_iva_porcentaje=16):
    """
    Calcula el monto total incluyendo el IVA.

    Args:
        monto_base (float or int): El monto original del producto o servicio.
        tasa_iva_porcentaje (float or int): La tasa de IVA en porcentaje (ej. 16 para 16%).

    Returns:
        float: El monto total con IVA, redondeado a dos decimales.
               Retorna un mensaje de error si los inputs son inválidos.
    """
    # Validaciones de entrada para monto_base
    if not isinstance(monto_base, (int, float)):
        return "Error: El monto base debe ser un número."
    if monto_base < 0:
        return "Error: El monto base no puede ser negativo."

    # Validaciones de entrada para tasa_iva_porcentaje
    if not isinstance(tasa_iva_porcentaje, (int, float)):
        return "Error: La tasa de IVA debe ser un número."
    if not (0 <= tasa_iva_porcentaje <= 100):
        return "Error: La tasa de IVA debe estar entre 0 y 100."

    iva_decimal = tasa_iva_porcentaje / 100
    monto_total = monto_base * (1 + iva_decimal)
    return round(monto_total, 2)

def dividir(a, b):
    """
    Realiza una división.

    Args:
        a (float or int): Numerador.
        b (float or int): Denominador.

    Returns:
        float or str: El resultado de la división o un mensaje de error si el denominador es cero.
    """
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

