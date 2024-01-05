class Password:
    def __init__(self,password):
        self.__password =password
    def get_password(self,isAuth):
        if isAuth:
         return self.__password
        else:
            print("Error")
    def set_password(self,password):
        if len(password)>10:
            self.__password = password
        else:
            print("Weak Password")
    def print_len(self):
        print("Your Password Len is",len(self.__password))
pwd = Password("Hacker123")
pwd.print_len()
pssd =pwd.get_password(False)
print(pssd)
pwd.set_password("Pramod123123")
pwd.print_len()