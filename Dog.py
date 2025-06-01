class Dog:
    animal = "Dog"
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour
    def detail(self):
        print("Animal :", Dog.animal)
        print("Breed :", self.breed)
        print("Colour :", self.colour)
dog1 = Dog("Labrador Retriever", "Golden")
dog2 = Dog("Alaskan Husky", "Silverish - Grey")
dog3 = Dog("German Shepherd", "Black and Tan")
dog1.detail()
dog2.detail()
dog3.detail()
print("Breed of 1st 2nd and 3rd dog respectively :\n", dog1.breed, dog2.breed, dog3.breed)
print("Colour of 1st 2nd and 3rd dog respectively : \n", dog1.colour, dog2.colour, dog3.colour)