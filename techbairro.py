import os
import sqlite3
import tkinter as tk
from tkinter import messagebox

from banco import GerenciadorClientes
from cliente import Cliente
from validacao import ValidadorCliente

# NOVO NA AULA 18: a versão fica num único lugar.
# Para publicar uma versão nova, basta mudar aqui
# (e registrar a mudança no CHANGELOG).
VERSAO = "3.3.1"

# ============================================================
# OBJETO GERENCIADOR
# ============================================================

# NOVO NA AULA 16: caminho completo do banco.
#
# __file__ é o caminho deste arquivo .py.
# Assim o techbairro.db fica SEMPRE na mesma pasta do projeto,
# não importa de onde o VS Code rodar o programa.
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
CAMINHO_BANCO = os.path.join(PASTA_DO_PROJETO, "techbairro.db")
# Mostra no terminal qual banco está em uso
print(f"Banco em uso: {CAMINHO_BANCO}")
# Cria o objeto responsável por gerenciar os clientes
gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()

# Guarda o id (do banco) do cliente em edição; None = cadastro novo
id_em_edicao = None
clientes_na_tela = []


# ============================================================
# FUNÇÕES DA INTERFACE
# ============================================================

def atualizar_contador():
    """Mostra na tela quantos clientes existem no banco."""
    try:
        texto = f"Clientes cadastrados: {gerenciador.total()}"
    except sqlite3.Error:
        texto = "Clientes cadastrados: ?"
    contador.config(text=texto)


def limpar_campos():
    """Limpa todos os campos do formulário e reseta o modo de edição."""
    global id_em_edicao

    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_endereco.delete(0, tk.END)

    id_em_edicao = None
    atualizar_titulo_botao_salvar()
    entrada_nome.focus()


def atualizar_titulo_botao_salvar():
    if id_em_edicao is not None:
        botao_salvar.config(text="Salvar edição")
    else:
        botao_salvar.config(text="Salvar")


def cancelar():
    # NOVO NA AULA 20: antes de limpar, descobre se estava editando
    estava_editando = id_em_edicao is not None
    limpar_campos()
    if estava_editando:
        status.config(text="Edição cancelada. Nada foi alterado.", fg="gray")
    else:
        status.config(text="Formulário limpo", fg="gray")


def salvar():
    global id_em_edicao

    nome = entrada_nome.get().strip()
    telefone = entrada_telefone.get().strip()
    email = entrada_email.get().strip()
    endereco = entrada_endereco.get().strip()

    cliente = Cliente(nome, telefone, email, endereco)

    # MUDOU NA AULA 21: as regras saíram daqui e foram
    # para o ValidadorCliente (validacao.py).
    # A tela só pergunta e mostra a resposta.
    erro = validador.validar(cliente)
    if erro is not None:
        status.config(
            text=erro,
            fg="red",
        )
        return

    # ---------------- GRAVA NO BANCO ----------------
    try:
        if id_em_edicao is not None:
            cliente.id = id_em_edicao
            alterou = gerenciador.atualizar(id_em_edicao, cliente)
            if not alterou:
                status.config(
                    text="Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.",
                    fg="red",
                )
                limpar_campos()
                return
            status.config(
                text=f"Cliente '{cliente.nome}' atualizado com sucesso!",
                fg="green",
            )
            atualizar_contador()
            limpar_campos()
            return
        else:
            gerenciador.adicionar(cliente)
            status.config(text=f"Cliente '{cliente.nome}' cadastrado com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    except sqlite3.Error as erro:
        messagebox.showerror("Erro no banco", f"Não foi possível salvar o cliente.\n{erro}")
        return

    atualizar_contador()
    limpar_campos()


def abrir_consulta():
    """Janela de consulta: lista os clientes com Editar e Excluir."""
    janela_consulta = tk.Toplevel(janela)
    janela_consulta.title("Consulta de Clientes")
    janela_consulta.geometry("800x500")
    janela_consulta.configure(bg="#FADD00")

    tk.Label(
        janela_consulta,
        text="Clientes Cadastrados",
        font=("Arial", 16, "bold"),
        bg="#FADD00",
        fg="#2C2C2C",
    ).pack(pady=15)

    frame_lista = tk.Frame(janela_consulta, bg="#FADD00")
    frame_lista.pack(fill="both", expand=True, padx=20, pady=10)

    lista = tk.Listbox(
        frame_lista,
        width=100,
        height=15,
        font=("Arial", 10),
        bg="#33322B",
        fg="#FADD00",
        selectbackground="#CFBB23",
        selectforeground="#33322B",
    )
    lista.pack(fill="both", expand=True)

    # NOVO NA AULA 20: guarda os clientes que estão aparecendo
    # na Listbox, na mesma ordem das linhas.
    clientes_na_tela.clear()

    def preencher_lista():
        """Lê o banco e mostra na Listbox (com tratamento de erro)."""
        lista.delete(0, tk.END)
        clientes_na_tela.clear()
        try:
            clientes = gerenciador.listar()
        except sqlite3.Error as erro:
            messagebox.showerror("Erro no banco", f"Não foi possível ler os clientes.\n{erro}")
            lista.insert(tk.END, f"Erro ao ler o banco: {erro}")
            return
        if len(clientes) == 0:
            lista.insert(tk.END, "Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                lista.insert(tk.END, str(cliente))
                clientes_na_tela.append(cliente)

    def cliente_selecionado(acao):
        # Descobre qual linha foi selecionada
        selecionado = lista.curselection()

        # Verifica se alguma linha foi selecionada
        #
        # A segunda condição protege as linhas de aviso,
        # como "Nenhum cliente cadastrado", que não são clientes.
        if not selecionado or selecionado[0] >= len(clientes_na_tela):
            messagebox.showwarning(
                "Atenção",
                f"Selecione um cliente antes de {acao}.",
            )
            return None

        # Pega o cliente que está na mesma posição da linha
        return clientes_na_tela[selecionado[0]]

    def editar_selecionado():
        global id_em_edicao

        cliente = cliente_selecionado("editar")
        if cliente is None:
            return

        entrada_nome.delete(0, tk.END)
        entrada_nome.insert(0, cliente.nome)
        entrada_telefone.delete(0, tk.END)
        entrada_telefone.insert(0, cliente.telefone)
        entrada_email.delete(0, tk.END)
        entrada_email.insert(0, cliente.email)
        entrada_endereco.delete(0, tk.END)
        entrada_endereco.insert(0, cliente.endereco)

        # Guarda o ID do banco (e não a posição na lista)
        id_em_edicao = cliente.id
        status.config(text="Editando cliente", fg="blue")
        atualizar_titulo_botao_salvar()
        janela_consulta.destroy()

    def excluir_selecionado():
        cliente = cliente_selecionado("excluir")
        if cliente is None:
            return

        confirmacao = messagebox.askyesno(
            "Confirmar Exclusão",
            f"Deseja realmente excluir {cliente.nome}?\n"
            f"Telefone: {cliente.telefone}\n"
            f"E-mail: {cliente.email}",
        )

        if confirmacao:
            try:
                removido = gerenciador.remover(cliente.id)
            except sqlite3.Error as erro:
                messagebox.showerror(
                    "Erro no banco", f"Não foi possível excluir o cliente.\n{erro}"
                )
                return
            if not removido:
                messagebox.showwarning(
                    "Cliente não encontrado",
                    f"{cliente.nome} já não está mais no banco.\n"
                    f"A lista será atualizada.",
                )
                preencher_lista()
                atualizar_contador()
                return
            messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
            preencher_lista()
            atualizar_contador()

    frame_botoes = tk.Frame(janela_consulta, bg="#FADD00")
    frame_botoes.pack(pady=15)

    tk.Button(
        frame_botoes,
        text="Editar selecionado",
        width=20,
        command=editar_selecionado,
        bg="#7A733D",
        fg="#FADD00",
        font=("Arial", 10, "bold"),
    ).grid(row=0, column=0, padx=5)

    tk.Button(
        frame_botoes,
        text="Excluir selecionado",
        width=20,
        command=excluir_selecionado,
        bg="#C41E3A",
        fg="#FADD00",
        font=("Arial", 10, "bold"),
    ).grid(row=0, column=1, padx=5)

    # NOVO NA AULA 20: duplo clique numa linha também abre a edição.
    lista.bind("<Double-Button-1>", lambda evento: editar_selecionado())

    preencher_lista()


# ============================================================
# JANELA PRINCIPAL
# ============================================================

janela = tk.Tk()
janela.title("Gerenciador de Clientes")
janela.geometry("600x500")
janela.resizable(False, False)
janela.configure(bg="#FADD00")

# ---------------- TÍTULO ----------------
tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18, "bold"),
    bg="#FADD00",
    fg="#2C2C2C",
).pack(pady=20)

# ---------------- FORMULÁRIO ----------------
formulario = tk.Frame(janela, bg="#504D35", padx=20, pady=20)
formulario.pack(padx=20, pady=10)


def criar_linha(linha, rotulo):
    tk.Label(
        formulario,
        text=rotulo,
        width=12,
        anchor="w",
        font=("Arial", 10, "bold"),
        bg="#504D35",
        fg="#FADD00",
    ).grid(row=linha, column=0, pady=5)
    entrada = tk.Entry(
        formulario,
        width=40,
        font=("Arial", 10),
        bg="#33322B",
        fg="#FADD00",
        insertbackground="#FADD00",
    )
    entrada.grid(row=linha, column=1, pady=5)
    return entrada


entrada_nome = criar_linha(0, "Nome:")
entrada_telefone = criar_linha(1, "Telefone:")
entrada_email = criar_linha(2, "E-mail:")
entrada_endereco = criar_linha(3, "Endereço:")

# ---------------- BOTÕES ----------------
botoes = tk.Frame(janela, bg="#FADD00")
botoes.pack(pady=15)

# Botão Salvar
#
# MUDOU NA AULA 20: o botão fica guardado na variável botao_salvar,
# para que o texto dele possa mudar no modo de edição.
# (o grid fica numa linha separada; se ficasse junto,
# a variável guardaria None em vez do botão)
botao_salvar = tk.Button(
    botoes,
    text="Salvar",
    width=15,
    command=salvar,
    bg="#7A733D",
    fg="#FADD00",
    font=("Arial", 10, "bold"),
)
botao_salvar.grid(row=0, column=0, padx=5)

tk.Button(
    botoes, text="Consultar", width=15, command=abrir_consulta,
    bg="#CFBB23", fg="#2C2C2C", font=("Arial", 10, "bold"),
).grid(row=0, column=1, padx=5)

tk.Button(
    botoes, text="Cancelar", width=15, command=cancelar,
    bg="#FADD00", fg="#2C2C2C", font=("Arial", 10, "bold"),
).grid(row=0, column=2, padx=5)

# ---------------- CONTADOR (lido do banco ao abrir) ----------------
contador = tk.Label(
    janela,
    text="Clientes cadastrados: ?",
    font=("Arial", 11, "bold"),
    bg="#FADD00",
    fg="#2C2C2C",
)
contador.pack(pady=5)

status = tk.Label(
    janela,
    text="Pronto",
    font=("Arial", 10, "bold"),
    bg="#FADD00",
    fg="#2C2C2C",
)
status.pack(pady=5)

atualizar_contador()

# ---------------- VERSÃO ----------------
tk.Label(
    janela, text=f"v{VERSAO}", bg="#FADD00", fg="#504D35", font=("Arial", 9)
).place(relx=0.97, rely=0.97, anchor="se")

janela.mainloop()
