# test_tareas.py
import unittest
import os
import json
from tarea2 import Configuracion, GestorTareas


class TestConfiguracion(unittest.TestCase):
    def test_singleton(self):
        config1 = Configuracion()
        config2 = Configuracion()
        self.assertIs(config1, config2, "Configuración no es Singleton")

    def test_modo_debug(self):
        config = Configuracion()
        config.activar_debug()
        self.assertTrue(config.modo_debug)
        config.desactivar_debug()
        self.assertFalse(config.modo_debug)


class TestGestorTareas(unittest.TestCase):
    def setUp(self):
        #  Usar un archivo temporal para evitar tareas previas
        self.archivo_test = "tareas_test.json"
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)
        self.gestor = GestorTareas(archivo_datos=self.archivo_test)

    def tearDown(self):
        # Eliminar el archivo al final de cada prueba
        if os.path.exists(self.archivo_test):
            os.remove(self.archivo_test)

    def test_agregar_tarea(self):
        self.gestor.agregar_tarea("Tarea de prueba")
        self.assertEqual(len(self.gestor.tareas), 1)
        self.assertEqual(self.gestor.tareas[0]["descripcion"], "Tarea de prueba")

    def test_completar_tarea_valida(self):
        self.gestor.agregar_tarea("Tarea a completar")
        resultado = self.gestor.completar_tarea(0)
        self.assertTrue(resultado)
        self.assertTrue(self.gestor.tareas[0]["completada"])

    def test_completar_tarea_invalida(self):
        resultado = self.gestor.completar_tarea(5)
        self.assertFalse(resultado)

    def test_listar_tareas(self):
        self.gestor.agregar_tarea("Tarea 1")
        self.gestor.agregar_tarea("Tarea 2")
        lista = self.gestor.listar_tareas()
        self.assertEqual(len(lista), 2)
        self.assertEqual(lista[0]["descripcion"], "Tarea 1")
        self.assertEqual(lista[1]["descripcion"], "Tarea 2")

    def test_guardar_y_cargar_tareas(self):
        self.gestor.agregar_tarea("Guardar prueba")
        nuevo_gestor = GestorTareas(archivo_datos=self.archivo_test)
        self.assertEqual(len(nuevo_gestor.tareas), 1)
        self.assertEqual(nuevo_gestor.tareas[0]["descripcion"], "Guardar prueba")


if __name__ == "__main__":
    unittest.main()
