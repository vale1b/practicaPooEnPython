class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    # Estos metodos llamados llamar y cortar son las acciones que hara el objeto, se le pasa self como parametro como referencia del objeto.
    def llamar(self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')
        
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')
        
celular1 = Celular('Samsung', 'S23', '48MP')

print(celular1)