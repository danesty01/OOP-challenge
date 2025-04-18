# File: /OOP-DigitalPet/OOP-DigitalPet/src/main.py

from pet import Pet

def main():
    # Create an instance of the Pet class
    my_pet = Pet(name="Buddy")

    # Test the pet's methods
    print(my_pet.get_status())
    
    my_pet.eat()
    print(my_pet.get_status())
    
    my_pet.sleep()
    print(my_pet.get_status())
    
    my_pet.play()
    print(my_pet.get_status())
    
    my_pet.train("roll over")
    print(my_pet.show_tricks())

if __name__ == "__main__":
    main()