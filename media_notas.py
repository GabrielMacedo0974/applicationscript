def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia ao estar vazia a nota será dada como 0.")
    return sum(notas) / len(notas)


def main():
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a nota e o peso da nota {i}: "))
        notas.append(nota)

    media = calcular_media(notas)
    print(f"A média das notas é: {media:.2f}")


if __name__ == "__main__":
    main()
