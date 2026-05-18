from main import ordenar_burbuja, procesar_corte_control,operaciones_aritmeticas


def test_ordenar_burbuja_por_sucursal():
    filas = [
        {"PRSUC": "3", "PRCOD": "A", "PRCANT": "1", "PRPRE": "100"},
        {"PRSUC": "1", "PRCOD": "B", "PRCANT": "2", "PRPRE": "50"},
        {"PRSUC": "2", "PRCOD": "C", "PRCANT": "3", "PRPRE": "10"},
    ]

    resultado = ordenar_burbuja(filas)

    assert resultado[0]["PRSUC"] == "1"
    assert resultado[1]["PRSUC"] == "2"
    assert resultado[2]["PRSUC"] == "3"


def test_corte_control_una_sucursal_un_producto():
    filas = [
        {"PRSUC": "1", "PRCOD": "A", "PRCANT": "2", "PRPRE": "100"},
        {"PRSUC": "1", "PRCOD": "A", "PRCANT": "3", "PRPRE": "100"},
    ]

    resultado = procesar_corte_control(filas)

    assert resultado["totales_generales"]["cantidad_sucursales"] == 1
    assert resultado["totales_generales"]["total_importe"] == 500

    sucursal = resultado["sucursales"][0]

    assert sucursal["sucursal"] == "1"
    assert sucursal["total_unidades"] == 5
    assert sucursal["mayor_producto"] == "A"
    assert sucursal["mayor_importe"] == 500
    assert sucursal["menor_producto"] == "A"
    assert sucursal["menor_importe"] == 500


def test_corte_control_una_sucursal_varios_productos():
    filas = [
        {"PRSUC": "1", "PRCOD": "A", "PRCANT": "2", "PRPRE": "100"},
        {"PRSUC": "1", "PRCOD": "A", "PRCANT": "1", "PRPRE": "100"},
        {"PRSUC": "1", "PRCOD": "B", "PRCANT": "5", "PRPRE": "10"},
    ]

    resultado = procesar_corte_control(filas)

    sucursal = resultado["sucursales"][0]

    assert sucursal["total_unidades"] == 8
    assert sucursal["mayor_producto"] == "A"
    assert sucursal["mayor_importe"] == 300
    assert sucursal["menor_producto"] == "B"
    assert sucursal["menor_importe"] == 50


def test_corte_control_varias_sucursales():
    filas = [
        {"PRSUC": "1", "PRCOD": "A", "PRCANT": "2", "PRPRE": "100"},
        {"PRSUC": "1", "PRCOD": "B", "PRCANT": "1", "PRPRE": "50"},
        {"PRSUC": "2", "PRCOD": "C", "PRCANT": "3", "PRPRE": "10"},
        {"PRSUC": "2", "PRCOD": "D", "PRCANT": "4", "PRPRE": "20"},
    ]

    resultado = procesar_corte_control(filas)

    assert resultado["totales_generales"]["cantidad_sucursales"] == 2
    assert resultado["totales_generales"]["total_importe"] == 360

    sucursal_1 = resultado["sucursales"][0]
    sucursal_2 = resultado["sucursales"][1]

    assert sucursal_1["sucursal"] == "1"
    assert sucursal_1["total_unidades"] == 3

    assert sucursal_2["sucursal"] == "2"
    assert sucursal_2["total_unidades"] == 7


def test_operaciones_suma():
    assert operaciones_aritmeticas("+", 5, 3) == 8

def test_operaciones_resta():
    assert operaciones_aritmeticas("-", 10, 4) == 6

def test_operaciones_multiplicacion():
    assert operaciones_aritmeticas("*", 3, 4) == 12

def test_operaciones_division():
    assert operaciones_aritmeticas("/", 10, 2) == 5.0

def test_operaciones_division_por_cero():
    assert operaciones_aritmeticas("/", 5, 0) == "Error: División por cero"

def test_operaciones_invalida():
    assert operaciones_aritmeticas("^", 5, 3) == "Error: Operación no válida"