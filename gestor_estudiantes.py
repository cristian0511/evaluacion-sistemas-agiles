from estudiante import Estudiante

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def registrar_estudiante(self, nombre: str, nota1: float, nota2: float, nota3: float) -> Estudiante:
        estudiante = Estudiante(nombre, nota1, nota2, nota3)
        self.estudiantes.append(estudiante)
        return estudiante

    def listar_estudiantes(self) -> list:
        return self.estudiantes

    def buscar_estudiante(self, nombre: str):
        return [e for e in self.estudiantes if e.nombre.lower() == nombre.lower()]