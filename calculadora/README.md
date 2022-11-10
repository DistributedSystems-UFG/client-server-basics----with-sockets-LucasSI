# ClientServerBasics
Starter code for the basic client-server assignment


Atividade 1 - Criação de uma calculadora para apresentar interação entre cliente - servidor onde o cliente passa uma equação sendo ela uma soma, uma subtração uma multiplicação ou uma divisão e recebe devolta a resposta.

o cliente envia uma equação qualquer no formato digito operação digito como uma string.
o servidor lê a string, identifica a operação lendo a string e comparando um a um aos operadores, depois ele separa os 2 digitos da operação utilizando string slicing, transforma em integers, aplica a operação desejada através de uma condição para utilizar o operador indicado e após isso envia a resposta devolta ao cliente.

https://drive.google.com/file/d/1h1jqhD45bv6UJ-KMVxVHFvGKx_LdU_1R/view?usp=share_link video do funcionamento feito em localhost pois não consegui configurar o aws para fazer a comunicação entre duas instâncias.
