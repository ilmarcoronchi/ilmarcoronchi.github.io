class Persona:

    # Attributi
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    # Metodi
    def description(self):
        return f"{self.nome} {self.cognome}"


if __name__ == '__main__':
    mario = Persona("Mario", "Rossi")
    print("ACCESSO AD ATTRIBUTO: "+mario.nome)
    print("CHIAMATA METODO: "+mario.description())
