# Changelog da TechBairro

## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.

## v3.3.2 (Aula 27)
### Adicionado
- README com requisitos, instalação e configuração do banco.
- Arquivo requirements.txt.
- Manual de uso em docs/manual_de_uso.md.
- Registro de testes em docs/registro_de_testes.md.

## v3.3.1 (Aula 21)
### Alterado
- A TechBairro foi reorganizada em camadas: modelo em `cliente.py`, acesso a dados em `banco.py`, regras de negócio em `validacao.py` e a interface em `techbairro.py`.
- A validação foi movida para a classe `ValidadorCliente`, sem mudar a aparência nem o comportamento observado pela interface.
### Corrigido
- A regra de negócio foi centralizada em um único lugar para permitir testes sem abrir a janela.

## v3.3.0 (Aula 20)
### Adicionado
- Modo de edição visível no botão principal, mostrando "Salvar edição" enquanto edita.
- Duplo clique na linha da Consulta para abrir a edição imediatamente.
- Lista interna da tela para garantir que a operação sempre use o cliente realmente visível ao usuário.
### Corrigido
- Edição e exclusão passaram a operar sobre o cliente correto, mesmo quando o banco muda entre a abertura da Consulta e a ação.
- O salvamento confere se o cliente ainda existe antes de gravar a atualização.
- A exclusão agora verifica se o cliente já foi removido e recarrega a lista quando isso acontece.
- Mensagens de cancelamento e status do formulário ficam corretas durante a edição.

## v3.2.1 (Aula 18)
### Alterado
- O número da versão passou a ficar em um único lugar: a constante `VERSAO` em `techbairro.py`.
### Adicionado
- Script `scripts/gerar_pacote.py`, que gera o arquivo de distribuição `TechBairro-3.2.1.zip` e deixa de fora arquivos e pastas não versionáveis.
- Arquivo `COMO_EXECUTAR.txt`, com instruções de execução e a versão do Python usada (3.12.0).

## v3.2 (Aula 16)
### Alterado
- O banco agora é aberto pelo caminho completo (os.path + __file__),
  sempre na pasta do projeto, não importa de onde o programa seja executado.
### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

## v3.1 (Aula 15)
### Corrigido
- O Endereço voltou a ser obrigatório no cadastro.
- A validação de e-mail passou a recusar e-mail sem nome antes do @ ou sem ponto depois do @.
- A Consulta voltou a listar os clientes em ordem alfabética.
- A edição de um cliente passou a ser gravada no banco (faltava o commit).
- A exclusão só acontece quando o usuário responde Sim na confirmação.

## v3.0 (Aula 14)
### Alterado
- O GerenciadorClientes deixou de guardar os clientes numa lista em memória
  e passou a gravar no banco SQLite techbairro.db.
- Editar e excluir passaram a usar o id do cliente no banco (id_em_edicao),
  e não mais a posição na lista (indice_em_edicao).
- O contador de clientes passou a vir do banco ao abrir a aplicação.
### Adicionado
- Tratamento de erros do banco com try/except sqlite3.Error.

## v2.0 (Aulas 11 e 12)
### Adicionado
- Classes Cliente e GerenciadorClientes.
- Tela de Consulta com a lista de clientes e os botões Editar e Excluir.
- Confirmação antes de excluir um cliente.

## Antes da v2.0 (Aulas 5 a 10)
- Janela de cadastro com Tkinter, eventos dos botões e validação dos campos.
