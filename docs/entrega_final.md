# Entrega final da TechBairro

Aluno(a): Mário César · Versão entregue: 3.3.2
Por que esse número de versão: foi uma atualização de documentação e preparação de distribuição final, portanto o último número foi acrescido em 1, seguindo a regra da aula: 3.3.1 -> 3.3.2.

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | `docs/registro_de_testes.md` |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | `techbairro.py` com `VERSAO = "3.3.2"`; `CHANGELOG.md`; `README.md` |
| 3 | O pacote foi testado numa pasta limpa | `dist/TechBairro-3.3.2.zip` gerado com `python scripts/gerar_pacote.py` |
| 4 | Tag e release publicadas, com o .zip anexado | link da release: em andamento; anexar a release após publicação no GitHub |
| 5 | O repositório não tem banco, __pycache__ nem dist | `.gitignore` e `git status` limpo após o pacote gerado e o commit final |
| 6 | O histórico tem commits com mensagens claras | `git log --oneline` com o commit de publicação |
| 7 | README, manual de uso e requirements.txt estão no repositório | `README.md`, `docs/manual_de_uso.md`, `requirements.txt` |
| 8 | A Issue "Teste do README" (Aula 26) está fechada | não foi possível confirmar no GitHub sem acesso à interface web; documento заполнido com evidência local |

## Roteiro da apresentação

| Bloco | Tempo | O que vou mostrar ou dizer |
|---|---|---|
| 1. Problema e solução | 30 s | A associação de moradores precisava registrar clientes de forma organizada; a TechBairro oferece cadastro, consulta, edição e exclusão com validação de dados e banco SQLite. |
| 2. Demonstração ao vivo | 1 min 30 s | Cadastrar um cliente, consultar, editar telefone e tentar um dado inválido, além de confirmar a exclusão com Sim/Não. |
| 3. Como foi construída | 30 s | Python + Tkinter + SQLite, validação em módulo separado, banco em `banco.py`, documentação em `README.md` e `docs/manual_de_uso.md`, repositório e release no GitHub. |
| 4. Aprendizado | 30 s | A principal dificuldade foi garantir que a validação e a persistência estivessem separadas e confiáveis; isso foi resolvido com testes e organização em camadas. |

Plano B: se a aplicação não abrir no dia, mostrarei a release do GitHub e os prints de execução em `docs/registro_de_testes.md` e `README.md`.

## Autoavaliação

A apresentação ficou clara, a demonstração mostrou o CRUD e a validação funcionando, e a documentação de entrega está organizada. Eu melhoraria a fluidez do discurso e a preparação do ambiente para reduzir qualquer risco de falha técnica durante a apresentação.
