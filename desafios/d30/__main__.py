from classe import *
from rich import inspect

def main():
    user = Credencial()
    user.senha = 'CEV*9!'
    print(user.senha)
    
    user.validar('Luis2014')
    inspect(user, private=True, methods=True)
    

if __name__ == '__main__':
    main()