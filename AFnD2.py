# Definição do AFD
estados = ["q0", "q1", "q2"]
alfabeto = ["a", "b", "e"]
inicial = "q0"
aceitacao = ["q0"]
funcao = {
    "q0": {"a": {}, "b": {"q2"}, "e": {"q1"}},
    "q1": {"a": {"q0"}, "b": {}, "e": {}},
    "q2": {"a": {"q1","q2"}, "b": {"q1"}, "e": {}}
}

# Função para processar transições epsilon
def processar_epsilon(estados_atuais):
    novos_estados = set(estados_atuais)
    while True:
        estados_adicionais = set()
        for estado in novos_estados:
            if "e" in funcao[estado]:
                estados_adicionais.update(funcao[estado]["e"])
        if estados_adicionais.issubset(novos_estados):
            break
        novos_estados.update(estados_adicionais)
    return novos_estados

# Processamento das palavras
input_palavras = input()
palavras = input_palavras.split()

for palavra in palavras:
    estados_atuais = {inicial}
    estados_atuais = processar_epsilon(estados_atuais)
    for caractere in palavra:
        if caractere not in alfabeto:
            print("caractere incorreto")
            break
        novos_estados = set()
        for estado in estados_atuais:
            if caractere in funcao[estado]:
                novos_estados.update(funcao[estado][caractere])
        estados_atuais = processar_epsilon(novos_estados)
    if any(estado in aceitacao for estado in estados_atuais):
        print("aceita")
    else:
        print("rejeita")
