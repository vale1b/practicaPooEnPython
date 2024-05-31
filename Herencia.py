# La herencia permite que se puedan definir nuevas clases basadas de unas ya existentes a fin de reutilizar el codigo.

class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

# A la clase Empleado le pasamos como parametro la clase Persona y de esta forma Empleado hereda todo lo de Persona.
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        # super() se usa cuando queremos indicar las propiedades que va a heredar la clase hija.
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

roberto = Empleado('Roberto', 43, 'argentino', 'Programador', 100000)

# Podemos acceder a todas las propiedades mediante la notacion de punto.
print(roberto.nombre)