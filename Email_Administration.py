from random import choice
from string import ascii_letters, punctuation, digits

database = {} # Stores user emails and passwords

class Email:
    def __init__(self, first, last, department_code, department=None, company="google"):
        self.first = first
        self.last = last
        self.dep = department
        self.dep_code = department_code
        self.comp = company
        self.email_address = self.generate_email() # Store the generated email
        self._password = None
    
    # Generator for email
    def generate_email(self):
        password = self.generate_random_password()
        if self.dep is None:
            database[f"{self.first}{self.last}@{self.comp}.com".lower()] = password
            return f"{self.first}{self.last}@{self.comp}.com".lower()
            
        else:
            database[f"{self.first}{self.last}@{self.dep}.{self.comp}.com".lower()] = password
            return f"{self.first}{self.last}@{self.dep}.{self.comp}.com".lower()
        
    def get_fullinfo(self):
        return f"Display Name: {self.first.title()} {self.last.title()}\nCompany Email: {self.email_address}\nPassword: {self._password}\nDepartment: {self.dep.title()}\nDepartment Code: {self.dep_code}"
        
    def get_dep_code(self):
        return self.dep_code
    
    # Getter method for email
    def get_email(self):
        return self.email_address
            
    # Password Generator
    def generate_random_password(self):
        auto_password = ""
        characters = ascii_letters + punctuation + digits

        for i in range(13):
            auto_password += choice(characters)
            
        self._password = auto_password
        return self._password

    # Getter method for password
    def get_password(self):     
        return self._password

    # Setter method for new password
    def set_new_pass(self, new_password):
        database[self.email_address] = new_password # Use the stored email address
        self._password = new_password # Stores the new pass
        print("Password successfully changed!")
        
    # Setter method for new email address
    def set_new_email(self, new_email):
        current_mail = self.email_address 
        password = database.pop(current_mail) # Retrieve password using stored email
        database[new_email.lower()] = password # Store the new email with the same password

        self.email_address = new_email
        print("Email successfully changed!")
        

# Sign Up User interface
def sign_up():
    department_available = ["sales", "development", "accounting"] 

    first_name = input("What is your first name?: ").strip()
    last_name = input("What is your last name?: ").strip()

    while True:
        department = input("Which department do you belong? (Type help to see available departments): ").strip().lower()
        
        if department == "help":
            available = ", ".join(department_available)
            print(available.title())
            continue
        else:
            break

    if department not in department_available:
         return Email(first_name, last_name)
    else:
        return Email(first_name, last_name, department_available.index(department) + 1, department=department)

    

    
user_1 = sign_up()

user_1.set_new_email("kebdakeb@gmail.com")
user_1.set_new_pass("yuhhhhhhh")
print(database)

print(user_1.get_dep_code(),"\n")

print(user_1.get_fullinfo())


