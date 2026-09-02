from flask import Flask


app = Flask(__name__)

class tarea:
    def __init__(self, id, titulo, completada):
        self.id = id
        self.titulo = titulo
        self. completada = completada

        def to_dict(self):
            return {
                "id" : self.id,
                "titulo" : self.titulo,
                "completada" : self.completada
            }
tarea_1 = tarea(1, "Aprender Flask", False),
tarea_2 = tarea(2, "Aprender Python", True),
tarea_3= tarea(3, "Aprender JavaScript", False)      

lista_de_tareas = [
    tarea_1,
    tarea_2,
    tarea_3
]

lista_de_tareas_dict = [tarea.to_dict() for tarea in lista_de_tareas]

@app.route('/todos', methods=['GET'])
def obtener_tareas():
    return lista_de_tareas_dict, 200

print(lista_de_tareas)