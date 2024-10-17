import json
from peticiones_http import obtener_cita
import datetime

# Diccionario para almacenar las tareas
tareas = []

# Función para crear una nueva tarea en el que le pido al usuario 3 datos
def crear_tarea(descripcion, prioridad, fecha_vencimiento):
    tarea = {
        "id": len(tareas) + 1,
        "descripcion": descripcion,
        "fecha_creacion": datetime.date.today().strftime("%d-%m-%Y"),
        "fecha_vencimiento": fecha_vencimiento,
        "prioridad": prioridad,
        "completada": False
    }
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' creada correctamente.\n")

# Con esta función muestro todas las tareas existenes 
def mostrar_tareas():
    if tareas:
        for tarea in tareas:
            print(f"Tarea {tarea['id']}: {tarea['descripcion']}, prioridad {tarea['prioridad']}, fecha_creacion: {tarea['fecha_creacion']}, fecha_vencimiento: {tarea['fecha_vencimiento']}, completada: {tarea['completada']}")
    else:
        print("No hay tareas.\n")

# Funcion para marcar una tarea como completada
def completar_tarea(id_tarea):
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
            print(f"Tarea {id_tarea} completada.\n")
            return
    print(f"Tarea con ID {id_tarea} no encontrada.\n")

# Filtrar tareas por estado (completadas o no completadas)
def filtrar_tareas_completadas(completadas=True):
    filtradas = [tarea for tarea in tareas if tarea["completada"] == completadas]
    if filtradas:
        for tarea in filtradas:
            print(f"Tarea {tarea['id']}: {tarea['descripcion']}, completada: {tarea['completada']}")
    else:
        print(f"No hay tareas {'completadas' if completadas else 'pendientes'}.\n")

# Ordenar tareas por prioridad usando función lambda
def ordenar_por_prioridad():
    tareas.sort(key=lambda tarea: tarea["prioridad"])
    print("Tareas ordenadas por prioridad.\n")

# Menú principal del gestor de tareas
def menu():
    while True:
        print("\nGestor de Tareas:")
        print("1. Crear tarea")
        print("2. Mostrar todas las tareas")
        print("3. Completar tarea")
        print("4. Filtrar tareas completadas")
        print("5. Ordenar tareas por prioridad")
        print("6. Obtener cita motivacional")  # NUEVA OPCIÓN
        print("7. Salir")
        
        opcion = input("Elige una opción: ")
        match opcion:
            
            case "1":
                descripcion = input("Descripción de la tarea: ")
                prioridad = int(input("Prioridad (1-5): "))
                fecha_vencimiento = input("Fecha de vencimiento: ")
                crear_tarea(descripcion, prioridad, fecha_vencimiento)
            case "2":
                mostrar_tareas()
            case "3":
                id_tarea = int(input("ID de la tarea a completar: "))
                completar_tarea(id_tarea)
            case "4":
                filtrar_tareas_completadas(completadas=True)
            case "5":
                ordenar_por_prioridad()
            case "6":
                obtener_cita()
            case "7":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor elige una opción correcta.\n")
                
# Para que se ejecute el menu al iniciar el programa
if __name__ == "__main__":
    menu()