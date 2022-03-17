from operator import index
def menu():
    return input(
    "Oque deseja realizar no momento?\n" + 
    "<INCLUIR> Para inserir um novo cadastro.\n"+
    "<EXCLUIR> Para excluir um cadastro.\n"+
    "<PESQUISAR> Para pesquisar um cadastro existente.\n"+
    "<LISTAR> Listar cadastros.\n"
).upper()

def selecao():
    selecao_1 = input("Precisa de outro servico? caso queira digite CONTINUAR.").upper()
    if selecao_1 != "CONTINUAR":
        print("Obrigado pelo acesso, volte quando precisar de um novo cadastro!!")
    else:
        menu()


def incluir():
        nome = input("\n se o nome já existe será atualizado o cadastro!\n"+"Digite o nome para cadastro: ")
        sobrenome = input("Digite agora o sobrenome: ")
        telefone = input("Informe agora um telefone ou celular: ")
        cpf= input("Por fim, informe um CPF válido:")
        cadastros[nome] = [sobrenome, telefone, cpf]
        return cadastros

def pesquisa():
    pesquisa = cadastros.get(input("Digite o nome para obter as informações:"))
    print(pesquisa)
    return pesquisa
cadastros={}
print(f"Bem vindo ao Cadastro!!!\n")
print("-"*40)
opcao = menu()
if opcao == "INCLUIR" or opcao =="EXCLUIR" or opcao == "PESQUISAR" or opcao =="LISTAR":
    if opcao == "INCLUIR":
        incluir()
        selecao()
    if opcao == "EXCLUIR":
        #cadastros.pop(cadastros.get(input("Qual o cadastro que deseja excluir\n digite o nome para exclusão:")))
        print(cadastros)
        menu()
    if opcao == "PESQUISAR":       
        pesquisa()
        menu()
    if opcao == "LISTAR":
        for k,v in cadastros.items():
            print(f'cadastro de  {k} {v}')
            break
        menu()

print(cadastros)