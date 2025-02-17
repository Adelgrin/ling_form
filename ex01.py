# Definição do AFD
estados = ["q1", "q2", "q3"]
alfabeto = ["0", "1"]
inicial = "q1"
aceitacao = ["q2"]
funcao = {
    "q1": {"0": "q1", "1": "q2"},
    "q2": {"0": "q3", "1": "q2"},
    "q3": {"0": "q2", "1": "q2"}
}

# Processamento das palavras
atual = inicial
#input = "0000 1000 0100 0010 0001 1100 1010 1001 0110 0101 0011 1110 1101 1011 0111 1111" 
input = input() 
palavras = input.split()

for palavra in palavras:
    for caractere in palavra:
        atual = funcao[atual][caractere]
    if atual in aceitacao:
        print("aceita")
    else:
        print("rejeita")
    atual = inicial