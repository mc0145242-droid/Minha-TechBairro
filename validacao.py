# ============================================================
# VALIDAÇÃO (Aula 21)
# ============================================================
#
# Responsabilidade: as regras de negócio do cadastro (RF01 a RF03).
# Este arquivo não sabe nada de janela nem de banco.


class ValidadorCliente:
    """Confere todas as regras do cliente."""

    def validar(self, cliente):
        # RF01: lista com os campos vazios, com o nome que aparece na tela
        vazios = []
        if cliente.nome == "":
            vazios.append("Nome")
        if cliente.telefone == "":
            vazios.append("Telefone")
        if cliente.email == "":
            vazios.append("E-mail")
        if cliente.endereco == "":
            vazios.append("Endereço")

        # Se houver algum campo vazio
        if vazios:
            return f"Preencha o(s) campo(s): {', '.join(vazios)}"

        # RF02: o telefone precisa ter somente números
        if not cliente.telefone.isdigit():
            return "Telefone inválido: use somente números."

        # RF03: o e-mail precisa estar no formato nome@dominio.com
        if not self.email_parece_valido(cliente.email):
            return "E-mail inválido: use o formato nome@dominio.com"

        # Nenhum problema encontrado
        return None

    def email_parece_valido(self, email):
        """nome@dominio.com: algo antes do @ e um ponto depois do @."""
        if "@" not in email:
            return False
        usuario, _, dominio = email.partition("@")
        return usuario != "" and "." in dominio.strip(".")
