estados = ['q1','q2','q3','q4']
alfabeto = ['0','1']
inicial = 'q1'
atual = inicial
aceitacao = ['q1','q2','q3']
funcao = {
    'q1' : {'1' : 'q2', '0' : 'q1'},
    'q2' : {'1' : 'q3', '0' : 'q1'},
    'q3' : {'0' : 'q4', '1' : 'q1'},
    'q4' : {'1' : 'q4', '0' : 'q4'},
    }

input = input()
palavras = input.split()
for palavra in palavras:
    for caractere in palavra:
        atual = funcao[atual][caractere]
    if atual in aceitacao:
        print("aceito")
    else:
        print("rejeito")
    atual = inicial