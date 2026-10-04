class Authenticate:
    ''' user Signup'''
    register : dict = {}

       # Validation logic
    def validation_logic(self , name  : str, password : int):
        if name not in self.register:
            return "Usernam is Aceepted"
            return True
        # True is 1 only


    def register_user(self , name : str , password : int ):
        if name not in self.register:
            self.register[name] = password
            return "User registered Sucesfully"
            return True



class login(Authenticate):
    ''' USer login  '''

    def Check_is_registered(self, name):
        if name not in self.register:
            print("User is not registered; kindly register first")
            return False
        else:
            print("User is already registered")
            return True

    def logined(self, name, password):
        if self.Check_is_registered(name):
            if self.register[name] == password:
                print("Login Sucessfully ")
                return True
            else:
                print("Password or name wrong")
                return False
