# Nome do arquivo
nome_arquivo = "numeros.py"

# Abrir o arquivo no modo de escrita
with open(nome_arquivo, "w") as arquivo:
    # Usar um loop for para escrever as linhas
    for numero in range(1, 11):
        arquivo.write(f"for numero in range(1, {numero + 1}):\n")
        arquivo.write("    print(numero)\n")
        arquivo.write("\n")  # Linha em branco para melhor organização

print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
