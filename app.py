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

    
tarea_1 = tarea(1, "Aprender Flask", False).to_dict()
tarea_2 = tarea(2, "Aprender Python", True).to_dict()
tarea_3= tarea(3, "Aprender JavaScript", False).to_dict()

lista_de_tareas = [
    tarea_1,
    tarea_2,
    tarea_3
]


@app.route('/todos', methods=['GET'])
def obtener_tareas():
    return lista_de_tareas, 200

if __name__ == "__main__":
    app.run(debug=True)

