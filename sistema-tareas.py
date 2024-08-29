def agregar_tarea(id_tarea, descripcion, prioridad):
    if id_tarea in tareas:
        raise ValueError("La tarea con este ID ya existe.")
    tareas[id_tarea]={
        'descripcion': descripcion,
        'prioridad': prioridad,
        'completado': False
    }

def actualizar_tarea(id_tarea, nueva_descripcion, nueva_prioridad):
    if id_tarea not in tareas:
        raise KeyError("La tarea no existe.")
    tareas[id_tarea]['descripcion']=nueva_descripcion
    tareas[id_tarea]['prioridad']=nueva_prioridad

def marcar_completada(id_tarea):
    if id_tarea in tareas:
        raise KeyError("La tarea no existe.")
    tareas[id_tarea]['completado']=True

def eliminar_tarea(id_tarea):
    if id_tarea not in tareas:
        raise KeyError("La tarea no existe.")
    del tareas[id_tarea]

def enlistar_tarea(completada=False):
    return [tareas['descripcion'] for tarea in tareas.values() if tareas['completado']== completada]

tareas = {}
agregar_tarea(10,'agregar','alta')
print(tareas)
