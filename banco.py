# ============================================================
# BANCO (Aula 21)
# ============================================================
#
# Responsabilidade: toda a comunicação com o banco SQLite.
# Este arquivo não sabe nada de janela.
# Importa o módulo do SQLite (já vem com o Python)
import sqlite3
from contextlib import closing

# O banco devolve linhas; o GerenciadorClientes transforma
# cada linha num objeto Cliente, por isso precisa conhecer a classe
from cliente import Cliente


class GerenciadorClientes:
    """Gerencia clientes usando um banco SQLite.

    Os métodos NÃO mostram mensagens: se algo der errado eles deixam
    o sqlite3.Error subir, e quem chama (a tela) decide o que mostrar.
    """

    def __init__(self, caminho_banco="techbairro.db"):
        self.caminho_banco = caminho_banco
        self.criar_tabela()

    def conectar(self):
        return sqlite3.connect(self.caminho_banco)

    def criar_tabela(self):
        # Mesma estrutura da Aula 14 (a do importar_planilha_antiga.py)
        with closing(self.conectar()) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS clientes ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "nome TEXT NOT NULL, "
                "telefone TEXT, "
                "email TEXT, "
                "endereco TEXT)"
            )
            conn.commit()

    def adicionar(self, cliente):
        with closing(self.conectar()) as conn:
            cur = conn.execute(
                "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
                (cliente.nome, cliente.telefone, cliente.email, cliente.endereco),
            )
            conn.commit()
            cliente.id = cur.lastrowid
        return cliente

    def listar(self):
        with closing(self.conectar()) as conn:
            linhas = conn.execute(
                "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY id"
            ).fetchall()
        return [Cliente(n, t, e, en, id=i) for (i, n, t, e, en) in linhas]

    def atualizar(self, id_cliente, cliente):
        """Atualiza pelo id do cliente e retorna True se uma linha foi alterada."""
        if id_cliente is None:
            raise ValueError("Cliente sem id não pode ser atualizado")
        with closing(self.conectar()) as conn:
            cur = conn.execute(
                "UPDATE clientes SET nome=?, telefone=?, email=?, endereco=? WHERE id=?",
                (cliente.nome, cliente.telefone, cliente.email, cliente.endereco, id_cliente),
            )
            conn.commit()
        return cur.rowcount == 1

    def remover(self, id_cliente):
        with closing(self.conectar()) as conn:
            cur = conn.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
            conn.commit()
        return cur.rowcount == 1

    def total(self):
        with closing(self.conectar()) as conn:
            return conn.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
