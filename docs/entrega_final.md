# Entrega final da TechBairro

Aluno(a): Mário César · Versão entregue: 3.3.2  
Por que esse número de versão: desde a versão 3.3.1 foram acrescentadas documentação e preparação da distribuição, sem novas funções; por isso, foi incrementado o último número: 3.3.1 -> 3.3.2.

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | [Registro dos seis testes e saída dos testes automáticos](./registro_de_testes.md). Os testes automáticos também passaram em Python 3.14.7 em 28/10/2026. |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | `techbairro.py`: `VERSAO = "3.3.2"`; [CHANGELOG v3.3.2](../CHANGELOG.md); [README v3.3.2](../README.md). |
| 3 | O pacote foi testado numa pasta limpa | `dist/TechBairro-3.3.2.zip` foi extraído numa pasta temporária limpa em 28/10/2026. A aplicação iniciou, criou um banco novo com 0 clientes e os seis testes automáticos passaram no conteúdo extraído (Python 3.14.7). |
| 4 | Tag e release publicadas, com o .zip anexado | [Release TechBairro 3.3.2](https://github.com/mc0145242-droid/Minha-TechBairro/releases/tag/v3.3.2), com `TechBairro-3.3.2.zip`. |
| 5 | O repositório não tem banco, __pycache__ nem dist | [Arquivos do repositório no GitHub](https://github.com/mc0145242-droid/Minha-TechBairro): banco, `__pycache__` e `dist` não estão publicados; `.gitignore` os exclui. |
| 6 | O histórico tem commits com mensagens claras | [Histórico de commits](https://github.com/mc0145242-droid/Minha-TechBairro/commits/main), incluindo [“Finaliza documentação de entrega e testes”](https://github.com/mc0145242-droid/Minha-TechBairro/commit/89dcc922833e04343564ee8f7de5648b6fefa720). |
| 7 | README, manual de uso e requirements.txt estão no repositório | [README](../README.md), [manual de uso](./manual_de_uso.md) e `requirements.txt` na raiz do repositório. |
| 8 | A Issue "Teste do README" (Aula 26) está fechada | [Issue #1 — Teste do README: fechada](https://github.com/mc0145242-droid/Minha-TechBairro/issues/1). |
| 9 | O vídeo está publicado e o link abre sem pedir login | **Pendente:** depois de publicar o vídeo, cole aqui o link e teste-o numa janela anônima. |

## Roteiro do vídeo (até 3 minutos)

| Bloco | Tempo | O que mostrar ou dizer |
|---|---|---|
| 1. Problema e solução | 30 s | A associação precisava organizar os cadastros; a TechBairro permite cadastrar, consultar, editar e excluir clientes, com validação e banco SQLite. Apresentar a versão 3.3.2. |
| 2. Demonstração | 1 min 30 s | Com dados fictícios, cadastrar um cliente, consultar, editar o telefone, mostrar uma validação recusando um dado inválido e excluir: primeiro responder Não e depois Sim. |
| 3. Como foi construída | 30 s | Python, Tkinter, SQLite, validação em módulo separado, testes, documentação, repositório e release no GitHub. |
| 4. Aprendizado | 30 s | Contar uma dificuldade do projeto e como foi resolvida, ou uma melhoria que faria. |

### Texto para falar

As instruções entre colchetes são ações na tela; não precisam ser lidas. Use apenas os dados fictícios abaixo e deixe o aplicativo aberto antes de começar.

**0:00–0:30 — Apresentação**

> Olá, eu sou Mário e vou apresentar a versão 3.3.2 da TechBairro. A associação de moradores precisava organizar os cadastros de clientes. Para resolver esse problema, desenvolvi um aplicativo que permite cadastrar, consultar, editar e excluir registros, com validação dos campos e armazenamento em um banco SQLite.

**0:30–2:00 — Demonstração**

> Vou cadastrar um cliente fictício. [Preencha Ana Souza, 61999990001, ana@email.com e Rua 1 Casa 2; clique em Salvar e confirme o aviso.] O cadastro foi salvo e o contador foi atualizado. Agora vou consultar a lista e selecionar a Ana para editar. [Abra Consultar, selecione a cliente e clique em Editar selecionado.] O formulário voltou preenchido. Vou trocar o telefone para 61998877665 e salvar a edição. [Salve e mostre a mensagem de sucesso.] Para demonstrar a validação, vou informar um e-mail sem ponto no domínio. [Tente salvar com o e-mail ana@email.] O sistema recusou o dado inválido; isso ajuda a evitar cadastros incorretos. Agora vou excluir esse registro. [Abra Consultar, selecione Ana e clique em Excluir selecionado.] Primeiro vou escolher Não para cancelar. [Clique em Não.] O cadastro continua na lista. Vou repetir e confirmar a exclusão. [Abra a confirmação novamente e clique em Sim.] Pronto: o cliente foi removido.

**2:00–2:30 — Construção e entrega**

> O aplicativo foi feito em Python com Tkinter para as telas e SQLite para armazenar os dados. Organizei o modelo, o acesso ao banco e as validações em módulos separados e registrei os testes e as instruções de uso. O código está no GitHub, e a versão 3.3.2 foi publicada com um pacote para download.

**2:30–3:00 — Aprendizado e encerramento**

> Uma dificuldade importante foi garantir que editar ou excluir afetasse o cliente certo. A aplicação usa o identificador do registro no banco, e os testes ajudam a conferir as regras e esse fluxo. Aprendi que separar responsabilidades e testar a versão final torna o sistema mais confiável. Obrigado por assistir.

## Perguntas

**1. Por que o arquivo `techbairro.db` não está no GitHub?**  
Porque ele guarda dados pessoais dos clientes. Mantê-lo fora do repositório evita expor esses dados; o `.gitignore` exclui o banco.

**2. Qual caso de teste pegou um defeito de verdade? Qual era o defeito?**  
Nos seis casos da versão 3.3.2 não foi encontrado defeito. Uma correção anterior, registrada na versão 3.3.0, tratou edição e exclusão que poderiam atingir o cliente errado se a lista mudasse depois de aberta a consulta. O programa passou a identificar o cliente pelo ID do banco e a conferir se o registro ainda existe.

**3. Se o voluntário tiver só o link do repositório, como instala e executa?**  
Instala o Python 3 com Tkinter, baixa o projeto pelo botão **Code > Download ZIP** no GitHub, extrai o arquivo, abre um terminal na pasta que contém `techbairro.py` e executa `python techbairro.py`. O projeto não requer bibliotecas externas. O [README](../README.md) contém as instruções.

## Autoavaliação

O roteiro organiza a apresentação para mostrar o problema, o sistema funcionando e como o projeto foi construído. Ao assistir à gravação, vou conferir se a tela está legível, se a explicação cabe no tempo e se o áudio está claro; se necessário, vou regravar o trecho que precisar. Aprendi que testar a versão final e preparar dados fictícios ajudam a apresentar o sistema com segurança.

**Depois de publicar o vídeo:** preencher o item 9 com o link e confirmar que ele abre sem login.
