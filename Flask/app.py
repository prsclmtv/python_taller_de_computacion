from flask import Flask

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
        


