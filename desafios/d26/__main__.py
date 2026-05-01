from funcionarios import *
from rich import print


def main():
    f1 = Horista('Carlos', 35, 160)
    f1.calc_sal()
    analise = f1.analisar_sal()
    print(analise)
    
    print()
    
    f2 = Mensalista('Luis', 1800)
    f2.calc_sal()
    analise2 = f2.analisar_sal()
    print(analise2)


if __name__ == '__main__':
    main()