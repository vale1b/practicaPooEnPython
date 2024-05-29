class Celular:
    
    # Esto es un metodo constructor y self sirve para referenciarse asi mismo.
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
 
# Esto es un objeto y le pasamos los atributos en el momento que instanciamos la clase.        
celular1 = Celular('samsung', 'S23', '48MP')

# Aca podemos preguntar por las propiedades del celular haciendo uso o no de la notacion de punto.
print(celular1)