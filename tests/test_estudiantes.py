import pytest
from estudiante import Estudiante
from gestor_estudiantes import GestorEstudiantes

def test_calculo_suma_y_estado_aprobado():
    est = Estudiante("Ana", 8, 8, 8)
    assert est.calcular_suma() == 24.0
    assert est.obtener_estado() == "APROBADO"

def test_calculo_suma_y_estado_reprobado():
    est = Estudiante("Luis", 5, 5, 5)
    assert est.calcular_suma() == 15.0
    assert est.obtener_estado() == "REPROBADO"

def test_validacion_notas_invalidas():
    with pytest.raises(ValueError, match="Nota incorrecta"):
        Estudiante("Pedro", -1, 5, 5)
    with pytest.raises(ValueError, match="Nota incorrecta"):
        Estudiante("Maria", 5, 11, 5)

def test_validacion_nombre_invalido():
    with pytest.raises(ValueError, match="Nombre incorrecto"):
        Estudiante("", 8, 8, 8)

def test_registro_y_busqueda_gestor():
    gestor = GestorEstudiantes()
    gestor.registrar_estudiante("Carlos", 10, 9, 8)
    assert len(gestor.listar_estudiantes()) == 1

    busqueda = gestor.buscar_estudiante("Carlos")
    assert len(busqueda) == 1
    assert busqueda[0].nombre == "Carlos"