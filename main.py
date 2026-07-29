from gestor_estudiantes import GestorEstudiantes

if __name__ == "__main__":
    gestor = GestorEstudiantes()

    # Registro
    gestor.registrar_estudiante("Ana", 8, 8, 8)
    gestor.registrar_estudiante("Luis", 6, 6, 6)
    gestor.registrar_estudiante("Carlos", 10, 9, 8)

    # Listar
    print("--- LISTA DE ESTUDIANTES ---")
    for e in gestor.listar_estudiantes():
        print(f"{e.nombre} | Notas: {e.nota1}, {e.nota2}, {e.nota3} | Suma: {e.calcular_suma()} | Estado: {e.obtener_estado()}")

    # Buscar
    print("\n--- BÚSQUEDA ---")
    resultados = gestor.buscar_estudiante("Ana")
    for e in resultados:
        print(f"Encontrado: {e.nombre} - {e.obtener_estado()}")