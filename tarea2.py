class Configuracion:
    """
    Clase Singleton para manejar la configuración global de la aplicación.
    Solo puede existir una instancia de esta clase.
    """
    _instancia = None

    def __new__(cls, modo_debug=False):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.modo_debug = modo_debug
        return cls._instancia

    def activar_debug(self):
        self.modo_debug = True

    def desactivar_debug(self):
        self.modo_debug = False
        
class GestorTareas:
    """
    Clase que permite agregar, listar y marcar tareas como completadas.
    """
    def __init__(self):
        self.tareas = []
        self.config = Configuracion()  # Acceso al Singleton

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)
        if self.config.modo_debug:
            print(f"[DEBUG] Tarea agregada: {descripcion}")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        print("\n--- Lista de tareas ---")
        for i, tarea in enumerate(self.tareas, start=1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - {estado}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            if self.config.modo_debug:
                print(f"[DEBUG] Tarea completada: {self.tareas[indice]['descripcion']}")
        else:
            print("Índice no válido.")

        # Programa principal
if __name__ == "__main__":
    config = Configuracion(modo_debug=True)  # Se crea la única instancia
    gestor = GestorTareas()

    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Escribe la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            gestor.listar_tareas()
        elif opcion == "3":
            gestor.listar_tareas()
            try:
                num = int(input("Número de la tarea a completar: ")) - 1
                gestor.completar_tarea(num)
            except ValueError:
                print("Debes ingresar un número válido.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")