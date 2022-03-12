from operator import index
def menu():
    return input(
    "Oque deseja realizar no momento?\n" + 
    "<INCLUIR> Para inserir um novo cadastro.\n"+
    "<EXCLUIR> Para excluir um cadastro.\n"+
    "<PESQUISAR> Para pesquisar um cadastro existente.\n"+
    "<LISTAR> Listar cadastros.\n"
).upper()
cadastros={}
print("Bem vindo ao Cadastro!!!\n")
opcao = menu()
while opcao == "INCLUIR" or opcao =="EXCLUIR" or opcao == "PESQUISAR" or opcao =="LISTAR":
    if opcao == "INCLUIR":
        nome = input("\n se o nome já existe será atualizado o cadastro!\n"+"Digite o nome para cadastro: ")
        sobrenome = input("Digite agora o sobrenome: ")
        telefone = input("Informe agora um telefone ou celular: ")
        cpf= input("Por fim, informe um CPF válido:")
        cadastros[nome] = [sobrenome, telefone, cpf]
        opcao = menu()
    if opcao == "EXCLUIR":
        cadastros.get(input("Qual o cadastro que deseja excluir\n digite o nome para exclusão:"))
    if opcao == "PESQUISAR":
        pesquisa = cadastros.get(input("Digite o nome para obter as informações:"))
        print(pesquisa)
        menu()
    if opcao == "LISTAR":
        for k,v in cadastros.items():
            print(f'cadastro de  {k} {v}')
            menu()

print(cadastros) 
