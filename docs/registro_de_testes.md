# Registro de testes da TechBairro

Versão testada: 3.3.2 · Data: 2026-10-26 · Responsável: Mário César
Sistema operacional e versão do Python: Windows 11 · Python 3.12.0

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos certos: Nome=Ana Souza, Telefone=61999990001, E-mail=ana@email.com, Endereço=Rua 1 Casa 2 | Status: `Cliente 'Ana Souza' cadastrado com sucesso!` e popup: `Cliente cadastrado com sucesso!` | Status: `Cliente 'Ana Souza' cadastrado com sucesso!` e popup: `Cliente cadastrado com sucesso!` | Passou |
| CT02 | RF01 | Salvar com Nome e Endereço vazios: Nome="", Telefone=61999990001, E-mail=ana@email.com, Endereço="" | `Preencha o(s) campo(s): Nome, Endereço` | `Preencha o(s) campo(s): Nome, Endereço` | Passou |
| CT03 | RF02 | Telefone 61 9999 0000 (com espaços): Nome=Ana Souza, Telefone="61 9999 0000", E-mail=ana@email.com, Endereço=Rua 1 Casa 2 | `Telefone inválido: use somente números.` | `Telefone inválido: use somente números.` | Passou |
| CT04 | RF03 | E-mail ana@email (sem ponto): Nome=Ana Souza, Telefone=61999990001, E-mail=ana@email, Endereço=Rua 1 Casa 2 | `E-mail inválido: use o formato nome@dominio.com` | `E-mail inválido: use o formato nome@dominio.com` | Passou |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar: abre a consulta, seleciona o cliente, altera telefone para 61998877665 e salva | Status: `Cliente 'Ana Souza' atualizado com sucesso!` | Status: `Cliente 'Ana Souza' atualizado com sucesso!` | Passou |
| CT06 | RF06 | Excluir um cliente: responder Não, depois Sim | Primeiro: nenhuma exclusão. Depois da confirmação final, popup: `Cliente removido com sucesso!` | Primeiro: nenhuma exclusão. Depois: `Cliente removido com sucesso!` | Passou |

## Testes automáticos

Saída do `python testar_validacao.py`:

```text
OK teste_cliente_valido
OK teste_endereco_vazio
OK teste_telefone_com_letras
OK teste_email_sem_ponto
OK teste_nome_e_telefone_vazios
OK teste_email_parece_valido_email_sem_usuario
Todos os testes passaram.
```

## Defeitos encontrados

Nenhum. A versão final 3.3.2 manteve as regras de validação e o fluxo de CRUD sem falhas nos cenários testados.
