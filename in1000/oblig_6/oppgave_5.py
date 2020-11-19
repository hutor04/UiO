# Create a class names Person. The instance must be initiated with name and age. The constructor must also create
# an empty list that contains the information abbout hobbies.
# The class must have a method to add new hobbies, to print out the hobbies, and to print out all the information
# about the instance.


# Define class
class Person():
    # Initiate class
    def __init__(self, navn, alder):
        self._name = navn
        self._age = alder
        self._hobbies = []

    # Add an entry to the list with hobbies.
    def leggTilHobby(self, hobby):
        self._hobbies.append(hobby)

    # Print out hobbies
    def skrivHobbyer(self):
        print("Person's hobbies are:")
        for hobby in self._hobbies:
            print(hobby)

    # Print out the information about the instance
    def skrivUt(self):
        print("Person's name: {}.\nPerson's age: {}.".format(self._name, self._age))
        self.skrivHobbyer()


# The function asks the user to create new instance of Person class and populates it with data.
def populate_person():
    # User input
    name = input('Type in the name of a person: ')
    age = int(input('Type in the age of the person: '))
    # Create instance
    p = Person(name, age)
    # Loop to get hobbies
    happy = False
    while not happy:
        hobby = input('Type in a hobby of the person or "q" to quit: ')
        if hobby != 'q':
            # Call method to add hobbies
            p.leggTilHobby(hobby)
        elif hobby == 'q':
            # Print out information about the instance and exit the loop
            p.skrivUt()
            happy = True

if __name__ == '__main__':
    populate_person()

