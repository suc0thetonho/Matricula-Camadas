from negocio import *


def menu():
    criar_tabelas()
    semear()
    while True:
        print("\n1) Matricular  2) Listar  3) Cancelar expiradas  4) Sair")
        opcao = input("> ").strip()
        if opcao == "1":
            print(matricular(input("id do aluno, codigo da turma: ")))
        elif opcao == "2":
            print(listar(int(input("id do aluno: "))))
        elif opcao == "3":
            print(cancelar_expiradas())
        elif opcao == "4":
            break
        else:
            print("Opcao invalida")
