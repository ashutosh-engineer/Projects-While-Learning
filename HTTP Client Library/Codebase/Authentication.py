class Authenticate:
    register : dict = {}

       # Validation logic
    def validation_logic(self , name  : str, password : int):
        if name not in self.register:
            print("Username is Aceepted")
            return 1


    def register_user(self , name : str , password : int ):
        if name not in self.register:
            self.register[name] = password



class login(Authenticate):
    pass

