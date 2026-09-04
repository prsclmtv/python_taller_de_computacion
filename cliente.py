import requests

BASE_URL = "http://52.205.10.150/todos"


def obtener_tareas():
    print("\n--- 1. Obtener todas las tareas (GET) ---")
    try:
        response = requests.get(BASE_URL)
        print(f"Código HTTP: {response.status_code}")
        print("Respuesta:", response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None


def crear_tarea(titulo):
    print(f"\n--- 2. Crear tarea: '{titulo}' (POST) ---")
    nueva_tarea = {"titulo": titulo}
    try:
        response = requests.post(BASE_URL, json=nueva_tarea)
        print(f"Código HTTP: {response.status_code}")
        print("Respuesta:", response.json())
        if response.status_code == 201:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
    return None


def actualizar_tarea(tarea_id, datos_actualizados):
    print(
        f"\n--- 3. Actualizar tarea ID {tarea_id} (PUT) ---",
    )
    try:
        response = requests.put(
            f"{BASE_URL}/{tarea_id}", json=datos_actualizados
        )
        print(f"Código HTTP: {response.status_code}")
        print("Respuesta:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")


def eliminar_tarea(tarea_id):
    print(f"\n--- 4. Eliminar tarea ID {tarea_id} (DELETE) ---")
    try:
        response = requests.delete(f"{BASE_URL}/{tarea_id}")
        print(f"Código HTTP: {response.status_code}")
        print("Respuesta:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")


def ejecutar_secuencia_pruebas():
    try:
        obtener_tareas()
        tarea_creada = crear_tarea("Estudiar Flask con Python")
        obtener_tareas()
        tarea_id = tarea_creada.get("id") if tarea_creada else 1
        actualizar_tarea(
            tarea_id,
            {"titulo": "Estudiar Flask y requests", "completada": True},
        )
        eliminar_tarea(tarea_id)
        actualizar_tarea(9999, {"titulo": "Tarea fantasma", "completada": True})

        eliminar_tarea(9999)

    except requests.exceptions.ConnectionError:
        print(
            "\n[ERROR] No se pudo conectar al servidor. Asegúrate de que app.py esté ejecutándose en http://127.0.0.1:5000."
        )


if __name__ == "__main__":
    ejecutar_secuencia_pruebas()