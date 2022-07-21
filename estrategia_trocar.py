import sys
import numpy as np
import random
import matplotlib.pyplot as plt

def main():
    try:
        if len(sys.argv) != 5:
            raise ValueError("Preencha os atributos")
        portas = int(sys.argv[1])
        carros = int(sys.argv[2])
        portas_abertas_pelo_apresentador = int(sys.argv[3])
        tentativas = int(sys.argv[4])
        if(portas < carros + portas_abertas_pelo_apresentador + 1):
            raise ValueError("Verifique os valores de modo que quantidade_de_portas > quantidade_de_carros + quantidade_de_portas_abertas_pelo_apresentador")
        monty_hall(portas,carros,portas_abertas_pelo_apresentador,tentativas)
    except ValueError as e:
        print('MONTY HALL ESTENDIDO!!!')
        print('Para executar via terminal:')
        print('python3 estrategia_trocar.py <quantidade_de_portas> <quantidade_de_carros> <quantidade_de_portas_abertas_pelo_apresentador> <quantidade de tentativas>')
        print('')
        print(e)

def escolher_aleatoriamente(opcoes):
    return random.choice(opcoes)
    
def monty_hall(portas,total_carros,portas_abertas_pelo_apresentador,tentativas):
    vitorias = 0
    x=[]
    y=[]
    for t in range(1, tentativas+1):
        carros=[]
        opcoes=np.array(range(1,portas+1))
        for _ in range(0, total_carros):
            carros.append(escolher_aleatoriamente(np.setdiff1d(opcoes, carros)))
        posicao_atual = escolher_aleatoriamente(opcoes)
        for _ in range(0, portas_abertas_pelo_apresentador):
            opcoes = np.setdiff1d(opcoes, escolher_aleatoriamente(np.setdiff1d(opcoes, carros + [posicao_atual])))
            posicao_atual = escolher_aleatoriamente(np.setdiff1d(opcoes, posicao_atual))
        if posicao_atual in carros:
            vitorias += 1
        if t % 10 == 0:
            x.append(t)
            y.append(vitorias/t)
    print('Probabilidade final = %.5f' % (vitorias/tentativas))
    plt.plot(x, y)
    plt.show()
       

if __name__ == '__main__':
    main()