# test_calculadora.py
import pytest
from calculadora import calcular_iva, dividir

# --- Tests para la función calcular_iva ---

def test_calcular_iva_estandar():
    """
    Verifica el cálculo estándar del IVA (TC-CALC-001).
    Monto base: 100, Tasa IVA: 16% -> Esperado: 116.00
    """
    assert calcular_iva(100, 16) == 116.00

def test_calcular_iva_tasa_cero():
    """
    Verifica el cálculo del IVA con tasa del 0% (TC-CALC-002).
    Monto base: 200, Tasa IVA: 0% -> Esperado: 200.00
    """
    assert calcular_iva(200, 0) == 200.00

def test_calcular_iva_tasa_alta():
    """
    Verifica el cálculo del IVA con una tasa alta (TC-CALC-003).
    Monto base: 50, Tasa IVA: 50% -> Esperado: 75.00
    """
    assert calcular_iva(50, 50) == 75.00

def test_calcular_iva_monto_base_no_numerico():
    """
    Verifica que la función retorne un error para monto base no numérico (TC-CALC-004).
    """
    assert calcular_iva("cien", 16) == "Error: El monto base debe ser un número."

def test_calcular_iva_monto_base_negativo():
    """
    Verifica que la función retorne un error para monto base negativo (TC-CALC-005).
    """
    assert calcular_iva(-100, 16) == "Error: El monto base no puede ser negativo."

def test_calcular_iva_tasa_no_numerica():
    """
    Verifica que la función retorne un error para tasa de IVA no numérica (TC-CALC-006).
    """
    assert calcular_iva(100, "dieciseis") == "Error: La tasa de IVA debe ser un número."

def test_calcular_iva_tasa_fuera_rango_superior():
    """
    Verifica que la función retorne un error para tasa de IVA > 100% (TC-CALC-007).
    """
    assert calcular_iva(100, 101) == "Error: La tasa de IVA debe estar entre 0 y 100."

def test_calcular_iva_tasa_fuera_rango_inferior():
    """
    Verifica que la función retorne un error para tasa de IVA < 0% (aunque el input validation ya cubre esto).
    """
    assert calcular_iva(100, -1) == "Error: La tasa de IVA debe estar entre 0 y 100."

# --- Tests para la función dividir ---

def test_dividir_estandar():
    """
    Verifica una división estándar (TC-DIV-001).
    """
    assert dividir(10, 2) == 5.0

def test_dividir_por_cero():
    """
    Verifica que la función retorne un error al dividir por cero (TC-DIV-002).
    """
    assert dividir(10, 0) == "Error: No se puede dividir por cero."

def test_dividir_numeros_negativos():
    """
    Verifica la división con números negativos (TC-DIV-003).
    """
    assert dividir(-10, 2) == -5.0

def test_dividir_decimal():
    """
    Verifica la división con resultado decimal (TC-DIV-004).
    """
    assert dividir(7, 2) == 3.5

