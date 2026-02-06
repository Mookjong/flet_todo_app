class Person:
    counter = 0
    age: int = 0
    
    def __init__(self, name: str):
        self.name = name
        Person.counter += 1
    def greet(self):
        print(f"Hello, my name is {self.name}, I'm {self.age} years old!")
        
        
if __name__ == "__main__":
    
    person = Person("Alice")
    
    print(f"Number of people created: {Person.counter}")
    
    
    next_person = Person("Bob")
    next_person.age = 30
    next_person.greet()

    person.greet()
    print(f"Number of people created: {Person.counter}")