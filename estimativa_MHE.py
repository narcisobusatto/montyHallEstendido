import sys
import math
import matplotlib.pyplot as plt

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Preencha o atributo")
        portas = int(sys.argv[1])
        estimativa_monty_hall(portas)
    except ValueError as e:
        print('MONTY HALL ESTENDIDO!!!')
        print('python3 teste2.py <quantidade_de_portas>')
        print(e)
    
def estimativa_monty_hall(portas):
    somatorio = 1
    x=[]
    y=[]
    y2=[]
    for p in range(0, portas+1):
        somatorio -= ((-1) ** p)/math.factorial(p)
        x.append(p)
        y.append(somatorio)
        y2.append(1-1/math.e)
    plt.plot(x, y2, label='1-1/e')
    plt.plot(x, y)
    plt.show()
       

if __name__ == '__main__':
    main()