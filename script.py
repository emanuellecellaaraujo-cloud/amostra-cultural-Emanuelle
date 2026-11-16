def obter_nota(mensagem):
    """Solicita uma nota ao usuário e valida se é um número entre 0 e 10."""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("⚠️ Erro: A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("⚠️ Erro: Entrada inválida. Por favor, digite apenas números.")


def calcular_media():
    """Função principal que coleta os dados, calcula a média e exibe o status."""
    print("=== Calculadora de Média Escolar ===")
    nome = input("Digite o nome do aluno: ").strip()

    if not nome:
        nome = "Aluno(a)"

    nota1 = obter_nota("Digite a primeira nota (0 a 10): ")
    nota2 = obter_nota("Digite a segunda nota (0 a 10): ")

    media = (nota1 + nota2) / 2

    print(f"\nAluno: {nome}")
    print(f"Média final: {media:.1f}")

    if media >= 7.0:
        print("Status: Aprovado!")
    elif media >= 5.0:
        print("Status: Em Recuperação.")
    else:
        print("Status: Reprovado.")


if __name__ == "__main__":
    calcular_media()

