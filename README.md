# Integração ao Banco de de dados

Implementação do exemplo clássico da biblioteca salvando em um Banco de dados *sqlite*.

As tabelas do projeto são:

**usuarios**(*id, nome*)  
**autores**(*id, nome*)  
**livros**(*id, titilo, id_autor, ano_oublicacao, edicao, disponivel*)  
**empestimos**(*id, id_usuario, data*)  
**empestimos_livros**(*id_emprestimo, id_livro, data_devolucao*)  