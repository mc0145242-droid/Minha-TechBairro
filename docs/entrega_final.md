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


## Perguntas

**1. Por que o arquivo `techbairro.db` não está no GitHub?**  
Porque ele guarda dados pessoais dos clientes. Mantê-lo fora do repositório evita expor esses dados; o `.gitignore` exclui o banco.

**2. Qual caso de teste pegou um defeito de verdade? Qual era o defeito?**  
Nos seis casos da versão 3.3.2 não foi encontrado defeito. Uma correção anterior, registrada na versão 3.3.0, tratou edição e exclusão que poderiam atingir o cliente errado se a lista mudasse depois de aberta a consulta. O programa passou a identificar o cliente pelo ID do banco e a conferir se o registro ainda existe.

**3. Se o voluntário tiver só o link do repositório, como instala e executa?**  
Instala o Python 3 com Tkinter, baixa o projeto pelo botão **Code > Download ZIP** no GitHub, extrai o arquivo, abre um terminal na pasta que contém `techbairro.py` e executa `python techbairro.py`. O projeto não requer bibliotecas externas. O [README](../README.md) contém as instruções.


