class student():

    Id_no=""
    name=""
    age=14
    house="gold"
    classteacher="Simon"

    def __init__(self):
        print("Making New Student")
    
    def update_details(self):
        self.Id_no=input("Enter Id")
        self.name=input("Enter Name")
    
    def show_details(self):
        print("Details Are:")
        print(self.Id_no)
        print(self.name)
        print(self.age)
        print(self.classteacher)
        print(self.house)

Arjun=student()
print(Arjun.update_details())
print(Arjun.show_details())
