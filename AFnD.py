# Definição do AFD
estados = ["q1", "q2", "q3", "q4"]
alfabeto = ["0", "1", "e"]
inicial = "q1"
aceitacao = ["q4"]
funcao = {
    "q1": {"0": {"q1"}, "1": {"q1", "q2"}, "e": {}},
    "q2": {"0": {"q3"}, "1": {}, "e": {"q3"}},
    "q3": {"0": {}, "1": {"q4"}, "e": {}},
    "q4": {"0": {"q4"}, "1": {"q4"}, "e": {}}
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
