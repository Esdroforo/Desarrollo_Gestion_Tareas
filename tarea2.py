# tareas.py
import json
import os


class Configuracion:
    """
    Clase Singleton para la configuración global.
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
    Clase principal que gestiona las tareas y las operaciones sobre ellas.
    """
    def __init__(self, archivo_datos="tareas.json"):
        self.tareas = []
        self.config = Configuracion()
        self.archivo_datos = archivo_datos
        self.cargar_tareas()  # Carga automática al iniciar

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)
        if self.config.modo_debug:
            print(f"[DEBUG] Tarea agregada: {descripcion}")
        self.guardar_tareas()
        return tarea

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.") 
            if self.config.modo_debug:
                print("[DEBUG] No hay tareas registradas.")
            return []  
        print("\n--- Lista de tareas ---")
        for i, tarea in enumerate(self.tareas, start=1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - {estado}")
        if self.config.modo_debug:
            print("[DEBUG] Listando tareas...")
        return self.tareas

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            if self.config.modo_debug:
                print(f"[DEBUG] Tarea completada: {self.tareas[indice]['descripcion']}")
            self.guardar_tareas()
            return True

        if self.config.modo_debug:
            print("[DEBUG] Índice no válido.")
        return False

    # --- NUEVAS FUNCIONES JSON ---
    def guardar_tareas(self):
        """Guarda las tareas en un archivo JSON."""
        try:
            with open(self.archivo_datos, "w", encoding="utf-8") as archivo:
                json.dump(self.tareas, archivo, indent=4, ensure_ascii=False)
            if getattr(self.config, "modo_debug", False):
                print(f"[DEBUG] Tareas guardadas en {self.archivo_datos}")
        except Exception as e:
            print(f"Error al guardar tareas: {e}")

    def cargar_tareas(self):
        """Carga las tareas desde el archivo JSON si existe."""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, "r", encoding="utf-8") as archivo:
                    self.tareas = json.load(archivo)
                if getattr(self.config, "modo_debug", False):
                    print(f"[DEBUG] Tareas cargadas desde {self.archivo_datos}")
            except Exception as e:
                print(f"Error al cargar tareas: {e}")
        else:
            if getattr(self.config, "modo_debug", False):
                print("[DEBUG] No hay archivo de tareas previo, se inicia vacío.")


# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":
    config = Configuracion(modo_debug=True)
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
            print("Guardando tareas y saliendo...")
            gestor.guardar_tareas()
            break
        else:
            print("Opción no válida.")
