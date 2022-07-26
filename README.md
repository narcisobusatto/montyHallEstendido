## Paradoxo Monty Hall

Projeto para verificação da estratégia TROCAR PORTAS como estratégia ótima.

# Monty Hall Estendido

O primeiro arquivo permite a simulação do paradoxo no modelo

<img alt="modelo" width="400px" src="/imagens/montyHallEstendido.png" />
<br \>
No qual:
p: quantidade de portas disponíveis para o participante
c: quantidade de carros (ou portas premiadas), de modo que a quantidade de portas com bodes seja p - c
k: quantidade de portas que o apresentador irá abrir.

Para execução

`python3 estrategia_trocar.py <p> <c> <k> <t>`

t: quantidade de jogos realizados (tentativas)


# Estimativa MH(n, 1, n-2)

O segundo arquivo calcula a estimativa para um modelo de n portas, 1 carro (prêmio) e n-2 portas a serem abertas pelo apresentador.

Para execução

`python3 estimativa_MHE.py <p>`

No qual:
p: quantidade de portas disponíveis para o participante

conforme o artigo no [Medium](https://medium.com/@narcisobusatto/paradoxo-de-monty-hall-b4a96ab682bf), a probabilidade de ganho para uma estratégia de TROCAR PORTAS é dada por

<img alt="estimativa" width="400px" src="/imagens/estimativaMHE.png" />
<br \>
<img alt="gráfico" width="400px" src="/imagens/estimativaGraficoMHE.png" />
