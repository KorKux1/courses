class Person(object):
    def __init__(self, name):
        self.name = name

    def move(self):
        print("Ando caminando")


class Biker(Person):
    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print("Ando moviendome en mi bicileta")


def main():
    person = Person('David')
    person.move()
    biker = Biker('Daniel')
    biker.move()   

if __name__ == '__main__':
    main()
    
        