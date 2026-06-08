from ex008 import ContaBancaria


def main():
    c1 = ContaBancaria(12077, "Luis", 1000)
    c1.deposito(500)
    c1.saque(-100)
    
    
    print(c1)

if __name__ == "__main__":
    main()