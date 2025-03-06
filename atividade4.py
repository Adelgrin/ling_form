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

alfabeto_entrada = input().split()
for alfa in alfabeto_entrada:
    alfabeto.append(alfa)


inicial = input()
atual = inicial
aceitacao_entrada = input().split()
for aceita in aceitacao_entrada:
    aceitacao.append(aceita)


for i in range(len(estados)):
    func_entrada = input().split()
    func = set()
    for f in func_entrada:
        if f == "vazio":
            func.add("")
            break
        for item in f.split(","):
            func.add(item)
    

    funcao[func[0]] = {alfabeto[0] : func[1], alfabeto[1] : func[2], {""} : func[3]}
    tempfunc = []

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