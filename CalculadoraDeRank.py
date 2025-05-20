def calcularSaldo(vitorias, derrotas):
    return vitorias - derrotas

def determinarNivel(vitorias):
    if vitorias <= 10:
        return "Ferro"
    elif 11 <= vitorias <= 20:
        return "Bronze"
    elif 21 <= vitorias <= 50:
        return "Prata"
    elif 51 <= vitorias <= 80:
        return "Ouro"
    elif 81 <= vitorias <= 90:
        return "Diamante"
    elif 91 <= vitorias <= 100:
        return "Lendário"
    else:
        return "Imortal"

# Entrada do usuário
vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

# Processamento
saldo = calcularSaldo(vitorias, derrotas)
nivel = determinarNivel(vitorias)

# Saída
print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")
