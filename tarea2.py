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