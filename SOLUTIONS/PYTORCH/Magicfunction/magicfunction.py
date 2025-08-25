class Person:
    def __init__(self, name, age):  # Constructor magic method
        self.name = name
        self.age = age
    
    def __str__(self):  # String representation when using print()
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):  # Developer representation
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):  # Makes len() work on our object
        return len(self.name)
    
    def __eq__(self, other):  # Equality comparison ==
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):  # Less than comparison <
        return self.age < other.age
    
    def __add__(self, other):  # Addition operator +
        return f"{self.name} & {other.name}"
    
    def __getitem__(self, key):  # Makes object subscriptable obj[key]
        if key == 0:
            return self.name
        elif key == 1:
            return self.age
        else:
            raise IndexError("Index out of range")
    
    def __call__(self):  # Makes object callable like a function
        return f"Hello, I'm {self.name}!"

if __name__ == "__main__":
    # Create objects
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    person3 = Person("Alice", 25)
    
    # __str__ magic method
    print("Using __str__:")
    print(person1)  # Calls __str__
    
    # __repr__ magic method
    print("\nUsing __repr__:")
    print(repr(person1))  # Calls __repr__
    
    # __len__ magic method
    print(f"\nLength of person1's name: {len(person1)}")  # Calls __len__
    
    # __eq__ magic method
    print(f"\nperson1 == person2: {person1 == person2}")  # Calls __eq__
    print(f"person1 == person3: {person1 == person3}")
    
    # __lt__ magic method
    print(f"\nperson1 < person2: {person1 < person2}")  # Calls __lt__
    
    # __add__ magic method
    print(f"\nperson1 + person2: {person1 + person2}")  # Calls __add__
    
    # __getitem__ magic method
    print(f"\nperson1[0]: {person1[0]}")  # Calls __getitem__
    print(f"person1[1]: {person1[1]}")
    
    # __call__ magic method
    print(f"\nCalling person1(): {person1()}")  # Calls __call__
    
    print("\n" + "="*50)
    print("COMMON MAGIC METHODS:")
    print("="*50)
    print("__init__     - Constructor")
    print("__str__      - String representation (user-friendly)")
    print("__repr__     - String representation (developer-friendly)")
    print("__len__      - Length when len() is called")
    print("__eq__       - Equality comparison ==")
    print("__lt__       - Less than comparison <")
    print("__gt__       - Greater than comparison >")
    print("__add__      - Addition operator +")
    print("__sub__      - Subtraction operator -")
    print("__mul__      - Multiplication operator *")
    print("__getitem__  - Indexing obj[key]")
    print("__setitem__  - Assignment obj[key] = value")
    print("__call__     - Makes object callable like function")
    print("__enter__    - Context manager (with statement)")
    print("__exit__     - Context manager cleanup")
