# ============================================================
# CLIENTE (Aula 21)
# ============================================================
#
# Responsabilidade: representar os dados de um cliente.
#
# NOVO NA AULA 21: a classe Cliente saiu do techbairro.py
# e veio para este arquivo, sem nenhuma mudança por dentro.
# Este arquivo não sabe nada de janela nem de banco.


class Cliente:
    def __init__(self, nome, telefone, email, endereco, id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return (
            (f"[{self.id}] " if self.id is not None else "")
            + f"Nome: {self.nome} | "
            + f"Telefone: {self.telefone} | "
            + f"E-mail: {self.email} | "
            + f"Endereço: {self.endereco}"
        )
