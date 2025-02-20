estados = ['q1','q2','q3','q4','q5']
alfabeto = ['a','b']
inicial = 'q1'
atual = inicial
aceitacao = ['q2','q3']
funcao = {
    'q1' : {'a' : 'q2', 'b' : 'q3'},
    'q2' : {'a' : 'q2', 'b' : 'q4'},
    'q3' : {'b' : 'q3', 'a' : 'q5'},
    'q4' : {'a' : 'q2', 'b' : 'q4'},
    'q5' : {'b' : 'q3', 'a' : 'q5'}
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