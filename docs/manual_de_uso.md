# Manual de uso da TechBairro

## A tela principal

A janela **Gerenciador de Clientes** mostra o título **Cadastro de Clientes** e quatro campos: **Nome**, **Telefone**, **E-mail** e **Endereço**. Abaixo deles ficam os botões **Salvar**, **Consultar** e **Cancelar**. Também aparecem o total de clientes cadastrados, uma mensagem de situação (inicialmente **Pronto**) e a versão do programa no canto inferior direito.

## Cadastrar um cliente

1. Na tela principal, preencha **Nome**, **Telefone**, **E-mail** e **Endereço**.
2. Clique em **Salvar**.
3. Quando os dados forem aceitos, a tela mostrará `Cliente 'nome' cadastrado com sucesso!` e aparecerá a confirmação **Cliente cadastrado com sucesso!**. Os campos serão limpos e o contador será atualizado.

## Consultar os clientes cadastrados

1. Clique em **Consultar**.
2. Na janela **Consulta de Clientes**, leia os dados na lista. Se não houver registros, aparecerá **Nenhum cliente cadastrado.**
3. Para voltar ao cadastro, feche a janela de consulta.

## Alterar os dados de um cliente

1. Clique em **Consultar**.
2. Selecione o cliente que deseja alterar e clique em **Editar selecionado**. Você também pode dar um duplo clique no cliente.
3. Na tela principal, altere os campos necessários. O botão principal passa a se chamar **Salvar edição**.
4. Clique em **Salvar edição**. A tela informará `Cliente 'nome' atualizado com sucesso!` e os campos serão limpos.
5. Se não quiser continuar, clique em **Cancelar**. A tela mostrará **Edição cancelada. Nada foi alterado.**

## Excluir um cliente

1. Clique em **Consultar**.
2. Selecione o cliente que deseja remover e clique em **Excluir selecionado**.
3. Confira o nome, o telefone e o e-mail na confirmação **Confirmar Exclusão**. Clique em **Sim** para excluir ou **Não** para manter o cadastro.
4. Ao confirmar, aparecerá **Cliente removido com sucesso!** e a lista e o contador serão atualizados.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Não deixe em branco. |
| Telefone | Sim | Informe somente números, sem espaços, hífen ou parênteses. |
| E-mail | Sim | Informe no formato `nome@dominio.com`, com texto antes do `@` e um ponto depois dele. |
| Endereço | Sim | Não deixe em branco. |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| `Preencha o(s) campo(s): ...` | Um ou mais campos obrigatórios estão vazios. | Preencha os campos indicados e clique em **Salvar** novamente. |
| `Telefone inválido: use somente números.` | O telefone contém algo além de números. | Apague espaços, sinais e letras; digite apenas os números. |
| `E-mail inválido: use o formato nome@dominio.com` | O e-mail não está no formato aceito. | Confira se há um nome antes do `@` e um ponto no domínio, por exemplo `ana@email.com`. |
| `Cliente 'nome' cadastrado com sucesso!` / **Cliente cadastrado com sucesso!** | O novo cadastro foi salvo. | Clique em **OK** na confirmação. |
| **Selecione um cliente antes de editar.** | Nenhuma pessoa foi selecionada para alteração. | Selecione uma linha da lista e clique em **Editar selecionado**. |
| **Selecione um cliente antes de excluir.** | Nenhuma pessoa foi selecionada para remoção. | Selecione uma linha da lista e clique em **Excluir selecionado**. |
| **Nenhum cliente cadastrado.** | Ainda não há clientes salvos. | Feche a consulta e cadastre um cliente na tela principal. |
| **Cliente removido com sucesso!** | O cadastro foi excluído. | Nenhuma ação adicional é necessária. |
| `Não foi possível salvar o cliente.` / `Não foi possível ler os clientes.` / `Não foi possível excluir o cliente.` | O programa não conseguiu acessar o arquivo de dados. | Anote a mensagem completa, inclusive o detalhe exibido, e peça ajuda à pessoa responsável pela instalação. |

## Dúvidas frequentes

**O que faço se esqueci um campo?**  
Preencha os quatro campos. Nome, telefone, e-mail e endereço são obrigatórios.

**Como corrijo um cadastro que já foi salvo?**  
Abra **Consultar**, selecione o cliente e clique em **Editar selecionado** (ou dê um duplo clique nele). Faça as alterações e clique em **Salvar edição**.

**O que acontece se eu clicar em Não na confirmação de exclusão?**  
O cliente continua cadastrado. Abra a consulta novamente se precisar conferir a lista.

**Onde estão os dados cadastrados?**  
No arquivo `techbairro.db`, na pasta do programa. Não apague nem compartilhe esse arquivo; ele contém dados pessoais.
