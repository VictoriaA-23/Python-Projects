 #this program gets attributes for a pet and assigns them to an object. The program then displays the information that is provided.

class Pet:
    def __init__(self):
        self.__name = 'Not provided'
        self.__kind = 'Not provided'
        self.__age = 0
        
#accessor and mutator methods
        
    def setname(self,name):
        self.__name = name
        
    def setkind(self,kind):
        self.__kind = kind
        
    def setage(self,age):
        self.__age = age

    def getname(self):
        return self.__name

    def getkind(self):
        return self.__kind

    def getage(self):
        return self.__age
        
#main function that creates object and organizes information to be displayed

def main():
    
    pet1 = Pet()
    
    print('A pet object has been created. Here is the initial information about the pet:')

    print('Name of pet:',pet1.getname())
    print('Type of pet:', pet1.getkind())
    print('Age of pet:', pet1.getage())

    print("Let's update the information for a pet!")
    

    pet1.setname(input("Enter the pet's name:"))
    pet1.setkind(input('Enter the type of animal:'))
    pet1.setage(input("Enter the pet's age:"))

    print('Here is the updated information about the pet:')
    print('Name of pet:',pet1.getname())
    print('Type of pet:',pet1.getkind())
    print('Age of pet:',pet1.getage())
    
    

main()
    
