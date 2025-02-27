estados = []
alfabeto = []
inicial = ''
aceitacao = []
funcao = {
    
}
tempfunc = []
estados_entrada = input().split()
for estado in estados_entrada:
    estados.append(estado)
inicial = input()
atual = inicial
aceitacao_entrada = input().split()
for aceita in aceitacao_entrada:
    aceitacao.append(aceita)
alfabeto_entrada = input().split()
for alfa in alfabeto_entrada:
    alfabeto.append(alfa)
for i in range(len(estados)):
    func_entrada = input().split()
    for func in func_entrada:
        tempfunc.append(func)
    funcao[tempfunc[0]] = {alfabeto[0] : tempfunc[1], alfabeto[1] : tempfunc[2]}
    tempfunc = []

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