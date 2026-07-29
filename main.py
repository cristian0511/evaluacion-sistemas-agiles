# main.py - Código Base Inicial
estudiantes = []

def p(n, n1, n2, n3):
    if n == "":
        print("Nombre incorrecto")
        return
    if n1 < 0 or n1 > 10:
        print("Nota incorrecta")
        return
    if n2 < 0 or n2 > 10:
        print("Nota incorrecta")
        return
    if n3 < 0 or n3 > 10:
        print("Nota incorrecta")
        return
    suma = n1 + n2 + n3
    if suma >= 24:
        estado = "APROBADO"
    else:
        estado = "REPROBADO"
    estudiantes.append({
        "nombre": n,
        "nota1": n1,
        "nota2": n2,
        "nota3": n3,
        "suma": suma,
        "estado": estado
    })
    print("Estudiante registrado")

def l():
    if len(estudiantes) == 0:
        print("No existen estudiantes")
    else:
        print("LISTA DE ESTUDIANTES")
        for e in estudiantes:
            print(e["nombre"], e["nota1"], e["nota2"], e["nota3"], e["suma"], e["estado"])

def buscar(n):
    encontrado = False
    for e in estudiantes:
        if e["nombre"] == n:
            print(e["nombre"], e["nota1"], e["nota2"], e["nota3"], e["suma"], e["estado"])
            encontrado = True
    if not encontrado:
        print("Estudiante no encontrado")

# Pruebas iniciales de ejecución
p("Ana", 8, 8, 8)
p("Luis", 6, 6, 6)
p("Carlos", 10, 9, 8)
l()
buscar("Ana")