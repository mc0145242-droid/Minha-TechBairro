# TechBairro

A TechBairro é um aplicativo de computador para a associação de moradores cadastrar, consultar, alterar e excluir dados de clientes.

**Versão atual:** 3.3.1 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastro de clientes com nome, telefone, e-mail e endereço.
- Consulta, alteração e exclusão de clientes, com contador de registros.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows, macOS ou Linux com ambiente gráfico. No Linux pode ser necessário instalar o pacote Tkinter da distribuição. |
| Python | Python 3; há registro de teste com Python 3.12 no Windows em `COMO_EXECUTAR.txt`. |
| Tkinter | Necessário para abrir as janelas. Geralmente acompanha o Python; no Linux, instale `python3-tk` se estiver ausente. |
| Bibliotecas externas | Nenhuma. A aplicação usa módulos da biblioteca padrão do Python. |
| Internet | Necessária para baixar o projeto; não é necessária para usar o aplicativo. |

Para conferir a versão do Python e testar o Tkinter no computador de instalação, execute:

```powershell
python --version
python -m tkinter
```

O primeiro comando mostra a versão instalada. O segundo deve abrir uma pequena janela de demonstração do Tkinter; feche-a para continuar. Se o Python ainda não estiver instalado, instale Python 3 e, no Windows, marque a opção para adicioná-lo ao PATH.

## Instalação

### Opção 1: baixar com Git

1. Instale Python 3 e Git. No GitHub, abra **Code**, escolha **HTTPS** e copie o endereço do repositório.
2. Abra o PowerShell (Windows) ou um terminal e execute os comandos abaixo:

   ```powershell
   git clone https://github.com/mc0145242-droid/Minha-TechBairro.git
   cd Minha-TechBairro
   ```

3. Instale os requisitos e inicie o programa:

   ```powershell
   python -m pip install -r requirements.txt
   python techbairro.py
   ```

### Opção 2: baixar pelo botão Code

1. No GitHub, abra **Code > Download ZIP** e salve o arquivo no computador.
2. Extraia o ZIP. No Windows, abra a pasta extraída no Explorador de Arquivos, clique na barra de endereço, digite `powershell` e pressione Enter. No macOS ou Linux, abra um terminal dentro da pasta extraída. Confirme que nela está o arquivo `techbairro.py`.
3. Nesse terminal, instale os requisitos e inicie o programa:

   ```powershell
   python -m pip install -r requirements.txt
   python techbairro.py
   ```

O arquivo `requirements.txt` informa que o projeto não precisa de pacotes externos; por isso, o comando de instalação não deve instalar nenhum pacote. Ao iniciar, deve abrir a janela **Gerenciador de Clientes**. No terminal aparecerá `Banco em uso:` seguido do caminho completo do arquivo de dados.

Se `python` não for reconhecido no Windows, instale Python marcando a opção para adicioná-lo ao PATH. No Linux, se a janela não abrir por falta do Tkinter, instale `python3-tk` pelo gerenciador de pacotes do sistema.

## Configuração do banco de dados

A TechBairro usa SQLite. Na primeira execução, cria automaticamente o arquivo `techbairro.db` na mesma pasta de `techbairro.py` e prepara a tabela de clientes. O caminho completo do arquivo em uso aparece no terminal na linha `Banco em uso: ...`; confira essa linha se houver mais de uma cópia do projeto.

O arquivo do banco não é distribuído nem deve ser enviado ao GitHub: ele contém dados pessoais dos clientes e está listado no `.gitignore`. Para fazer uma cópia de segurança, feche o programa e copie `techbairro.db` para um local protegido, com acesso restrito. Para restaurar os dados, feche o programa e coloque a cópia de volta na pasta do projeto, com esse mesmo nome. Proteja também as cópias: elas contêm os mesmos dados pessoais.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

| Arquivo ou pasta | O que contém |
|---|---|
| `techbairro.py` | Abre a interface, inicia o banco e coordena as ações. |
| `cliente.py` | Reúne os dados de cada cliente. |
| `banco.py` | Salva, consulta, altera e remove clientes no SQLite. |
| `validacao.py` | Confere os campos antes de salvar. |
| `requirements.txt` | Registra que não há dependências externas. |
| `docs/manual_de_uso.md` | Instruções para cadastrar e administrar clientes. |
| `CHANGELOG.md` | Histórico de alterações por versão. |
| `.gitignore` | Impede o envio do banco e de arquivos locais ao GitHub. |
| `scripts/` | Ferramentas auxiliares do projeto. |

## Autor

Mário César · Técnico em Desenvolvimento de Sistemas · Senac DF
