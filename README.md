# Gerenciamento de Estoque

## Classes: 
- Produto: atributos incluem id, nome, preço, quantidade e categoria 
- Pedidos: atributos incluem id, data do pedido, status e uma lista de produtos 
- Produtos_pedidos: tabela de relacionamento, incluem as chaves estrangeiras das tabelas produto e pedido e a quantidade 

## Relacionamento: 
Um pedido pode ter vários produtos e um produto pode estar em varios pedidos 

## Comportamento Detalhado: 
- Aviso de estoque baixo quando o produto estiver abaixo de 5 unidades no estoque 
- Busca de produtos no estoque por categoria ou por todas as categorias juntas 
- Busca de produtos para pedidos através de categorias 

## Pontos a serem avaliados: 

Qualidade do Código e Estrutura 
- Legibilidade: O código segue as convenções do PEP 8? 
- Manutenibilidade: O código é bem-organizado e fácil de entender e 
modificar? 

- Reutilização: Existem componentes ou classes que podem ser 
reutilizados em outros contextos ou projetos? 
- Uso de Padrões de Projeto: Padrões de projeto foram usados 
apropriadamente para resolver problemas comuns? 

Funcionalidade e Lógica 
- Corretude: Todas as funcionalidades implementadas funcionam como 
esperado? 
- Tratamento de Erros: O sistema lida adequadamente com entradas 
inválidas e falhas durante a execução? 
- Persistência de Dados: Os dados são salvos e recuperados de forma 
correta e eficiente? 
- Testes: O sistema possui testes automatizados para garantir sua 
corretude e robustez? 

Interface do Usuário e Experiência do Usuário (UI/UX) 
- Clareza: A interface é intuitiva e as informações são fáceis de 
encontrar? 
- Design: A interface é visualmente agradável e consistente? 
- Responsividade: A interface responde bem a diferentes ações do 
usuário? 
- Acessibilidade: O sistema é acessível para usuários com diferentes 
habilidades? 

Performance e Otimização 
- Eficiência: O sistema responde rapidamente às interações do usuário? 
- Consumo de Recursos: O sistema faz uso eficiente de memória e 
outros recursos? 
- Escalabilidade: O sistema pode lidar com um aumento no volume de 
dados ou usuários? 

Funcionalidades Adicionais 
- Inovação: As funcionalidades adicionais oferecem melhorias 
significativas ao uso do sistema? 
- Integração: As funcionalidades adicionais estão bem integradas ao 
sistema existente? 
- Valor Agregado: As funcionalidades adicionais aumentam o valor do 
sistema para o usuário final? 

## Ferramentas Utilizadas 
- Python 
- Pyside6 
- QTDesign 
- SQLAlchemy 
- Pandas

  ## Diagrama de Classes
  

![DiagramaDeClasses](https://github.com/victorzxhugo/TrabalhoFinalDevDesktop/assets/141194148/58dae381-6980-4a79-9e26-2cedc875a5dc)


## Diagrama de Caso de Uso

![Caso_De_Uso](https://github.com/victorzxhugo/TrabalhoFinalDevDesktop/assets/141194148/49206a5e-01c1-4a85-bea1-3e3e1ca4d223)











