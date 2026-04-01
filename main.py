class Saludo:
    
    def __init__ (self, name: str):
        self.name = name
    
    def saludar (self):
        print(f"Hola {self.name}")



misaludo = Saludo("Santiago")

misaludo.saludar()
