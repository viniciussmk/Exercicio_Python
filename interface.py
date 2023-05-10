import tkinter as tk
import re

def validar():
    nome = entrada_usuario.get()
    senha = entrada_senha.get()
    nome_arquivo = entrada_arquivo.get()
    
    # Verifica se a senha é igual ao nome do usuário
    if senha == nome:
        lbl_erro.config(text="Erro: a senha não pode ser igual ao nome de usuário.")
    else:
        # Verifica a complexidade da senha
        if not re.search(r'[0-9]', senha):
            lbl_erro.config(text="Erro: a senha deve conter pelo menos um número.")
        elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            lbl_erro.config(text="Erro: a senha deve conter pelo menos um caractere especial.")
        elif not re.search(r'[A-Z]', senha):
            lbl_erro.config(text="Erro: a senha deve conter pelo menos uma letra maiúscula.")
        else:
            # Salva as informações em um arquivo com o nome informado pelo usuário
            with open(f'{nome_arquivo}.txt', 'a') as arquivo:
                arquivo.write(f"{nome}:{senha}\n")
            lbl_erro.config(text="Usuário e senha cadastrados com sucesso!")

janela = tk.Tk()
janela.title("Verificar senha")

# Criando as caixas de entrada e labels
lbl_usuario = tk.Label(janela, text="Usuário:")
lbl_usuario.pack()
entrada_usuario = tk.Entry(janela)
entrada_usuario.pack()

lbl_senha = tk.Label(janela, text="Senha:")
lbl_senha.pack()
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

lbl_arquivo = tk.Label(janela, text="Nome do arquivo:")
lbl_arquivo.pack()
entrada_arquivo = tk.Entry(janela)
entrada_arquivo.pack()

# Criando o botão de validação e a label de erro
btn_validar = tk.Button(janela, text="Validar", command=validar)
btn_validar.pack()

lbl_erro = tk.Label(janela, fg="red", font=("Arial", 12))
lbl_erro.pack()

janela.mainloop()
