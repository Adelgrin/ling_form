estados = ['q1','q2','q3','q4','q5','q6','q7']
alfabeto = ['0','1']
inicial = 'q1'
atual = inicial
aceitacao = ['q5']
funcao = {
    'q1' : {'1' : 'q3', '0' : 'q2'},
    'q2' : {'1' : 'q5', '0' : 'q4'},
    'q3' : {'0' : 'q5', '1' : 'q7'},
    'q4' : {'1' : 'q6', '0' : 'q4'},
    'q5' : {'1' : 'q7', '0' : 'q6'},
    'q6' : {'1' : 'q7', '0' : 'q6'},
    'q7' : {'1' : 'q7', '0' : 'q7'}
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