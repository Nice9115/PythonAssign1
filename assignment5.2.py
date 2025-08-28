class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        pass
    
    def introduce(self):
        return f"I am a {self.name}"

# Animal subclasses with different move() implementations
class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
    
    def move(self):
        return "Running on four legs"

class Eagle(Animal):
    def __init__(self):
        super().__init__("Eagle")
    
    def move(self):
        return "Soaring high in the sky"

class Dolphin(Animal):
    def __init__(self):
        super().__init__("Dolphin")
    
    def move(self):
        return "Swimming gracefully in the ocean"

class Kangaroo(Animal):
    def __init__(self):
        super().__init__("Kangaroo")
    
    def move(self):
        return "Hopping with powerful legs"

class Snake(Animal):
    def __init__(self):
        super().__init__("Snake")
    
    def move(self):
        return "Slithering silently"

class Monkey(Animal):
    def __init__(self):
        super().__init__("Monkey")
    
    def move(self):
        return "Swinging from tree to tree"

def demonstrate_animal_movement(animals):
    """Demonstrate how different animals move"""
    print("=" * 50)
    print("ANIMAL MOVEMENT DEMONSTRATION")
    print("=" * 50)
    
    for animal in animals:
        print(f"{animal.introduce():<15} → {animal.move()}")

def create_animal_farm():
    """Create and return all animal instances"""
    return [
        Dog(),
        Eagle(),
        Dolphin(),
        Kangaroo(),
        Snake(),
        Monkey()
    ]

def animal_race():
    """Simulate a fun animal race"""
    print("\n" + "=" * 50)
    print("ANIMAL RACE SIMULATION")
    print("=" * 50)
    
    animals = create_animal_farm()
    
    for i, animal in enumerate(animals, 1):
        print(f"Lane {i}: {animal.introduce()} - {animal.move()}")

def interactive_zoo():
    """Interactive zoo experience"""
    animals = create_animal_farm()
    
    print("\n" + "=" * 50)
    print("WELCOME TO THE VIRTUAL ZOO")
    print("=" * 50)
    
    while True:
        print("\nChoose an animal to learn about:")
        for i, animal in enumerate(animals, 1):
            print(f"{i}. {animal.introduce()}")
        print("0. Exit the zoo")
        
        choice = input("\nEnter your choice (1-6, 0 to exit): ")
        
        if choice == '0':
            print("Thank you for visiting the virtual zoo!")
            break
        elif choice in ['1', '2', '3', '4', '5', '6']:
            animal = animals[int(choice) - 1]
            print(f"\n{animal.introduce()}")
            print(f"Movement: {animal.move()}")
            
            # Additional facts
            if isinstance(animal, Dog):
                print("Fact: Dogs can run up to 45 mph!")
            elif isinstance(animal, Eagle):
                print("Fact: Eagles can spot prey from 2 miles away!")
            elif isinstance(animal, Dolphin):
                print("Fact: Dolphins sleep with one eye open!")
            elif isinstance(animal, Kangaroo):
                print("Fact: Kangaroos can jump 30 feet in one leap!")
            elif isinstance(animal, Snake):
                print("Fact: Snakes smell with their tongues!")
            elif isinstance(animal, Monkey):
                print("Fact: Monkeys can recognize themselves in mirrors!")
        else:
            print("Please enter a valid choice (1-6)!")

# Main program execution
if __name__ == "__main__":
    # Create all animals
    animals = create_animal_farm()
    
    # Demonstration
    demonstrate_animal_movement(animals)
    
    # Animal race simulation
    animal_race()
    
    # Interactive zoo experience
    interactive_zoo()