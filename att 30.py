# crie uma duncao que calcule a nota a media de 3 notas em seguida verifique se ele esta aprovado ou reprovado para notas acima de 7

def verificar_aprovacao(notas):
    media = sum(notas) / 3
    return media, "Aprovado" if media >= 7 else "Reprovado"

notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
print(f"Média: {verificar_aprovacao(notas)[0]:.2f} - {verificar_aprovacao(notas)[1]}")