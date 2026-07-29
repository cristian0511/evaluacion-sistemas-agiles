class Estudiante:
    NOTA_MINIMA = 0.0
    NOTA_MAXIMA = 10.0
    UMBRAL_APROBACION = 24.0

    def __init__(self, nombre: str, nota1: float, nota2: float, nota3: float):
        self.nombre = self._validar_nombre(nombre)
        self.nota1 = self._validar_nota(nota1)
        self.nota2 = self._validar_nota(nota2)
        self.nota3 = self._validar_nota(nota3)

    def _validar_nombre(self, nombre: str) -> str:
        if not nombre or nombre.strip() == "":
            raise ValueError("Nombre incorrecto")
        return nombre.strip()

    def _validar_nota(self, nota: float) -> float:
        if nota < self.NOTA_MINIMA or nota > self.NOTA_MAXIMA:
            raise ValueError("Nota incorrecta")
        return nota

    def calcular_suma(self) -> float:
        return self.nota1 + self.nota2 + self.nota3

    def obtener_estado(self) -> str:
        return "APROBADO" if self.calcular_suma() >= self.UMBRAL_APROBACION else "REPROBADO"