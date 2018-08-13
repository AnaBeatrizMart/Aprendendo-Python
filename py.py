Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Primeiros passos em python
>>> ## Exercicios realizados durante a aula de Python do Curso em Video
>>> ## Professor Gustavo Guanabara
>>> ## Executados em Agosto de 2018
>>> 
>>> ## Para mostrar/printar frases na tela é indispensavel o uso de aspas
>>> print ('Hello, world')
Hello, world
>>> 
>>> ## A soma utiliza uma estrutura parecida, mas não usas aspas
>>> print (5+7)
12
>>> print (8+9)
17
>>> print(26+99)
125
>>> print (50+50)
100
>>> print (18+18)
36
>>> ## Testando a soma utilizando aspas
>>> print ('7'+'4')
74
>>> ## Calculos sem o comando print
>>> 7+4
11
>>> 5+8+8
21
>>> ## Mostrando duas variaveis de texto sem usar print
>>> '59'+'48'
'5948'
>>> nome = Jennie
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nome = Jennie
NameError: name 'Jennie' is not defined
>>> nome = 'Jennie'
>>> idade = 21
>>> peso = 50
>>> print (nome, idade, peso)
Jennie 21 50
>>> ## Testando o processo anterior usando + invés de virgula
>>> print (nome + idade + peso)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print (nome + idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> ## Deu erro, porque não se trata somente de mensagens
>>> 
>>> ## Perguntando
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome? Lisa
>>> idade = input ('Qual a sua idade?')
Qual a sua idade? 20
>>> peso = input ('Qual é o seu peso?')
Qual é o seu peso?46
>>> print (nome, idade, peso)
 Lisa  20 46
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome? Jisoo
Qual é a sua idade?22
Qual é o seu peso?45
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome? Roseanne
Qual é a sua idade?20
Qual é o seu peso?45.5
>>> 45.5
45.5
>>> 
>>> ## Desafio 01:
>>> ## Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
>>> nome = input 'Qual é o seu nome?')
SyntaxError: invalid syntax
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome?Ana
>>> 
>>> print ('Olá, nome, seja bem-vindo!')
Olá, nome, seja bem-vindo!
>>> 
>>> 
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome?Ana
>>> Print ('Olá, + nome + seja muito bem-vindo(a)!')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    Print ('Olá, + nome + seja muito bem-vindo(a)!')
NameError: name 'Print' is not defined
>>> 
>>> 
>>> nome = input ('Qual é o seu nome?') + print ('Olá, + input + seja bem vindo!')
Qual é o seu nome?Ana
Olá, + input + seja bem vindo!
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    nome = input ('Qual é o seu nome?') + print ('Olá, + input + seja bem vindo!')
TypeError: can only concatenate str (not "NoneType") to str
>>> 
>>> nome = input ('Qual é o seu nome'?)
SyntaxError: invalid syntax
>>> nome = input ('Qual é o seu nome?')
Qual é o seu nome? Ana
>>> Print ('Olá', + nome + 'seja muito bem-vindo')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    Print ('Olá', + nome + 'seja muito bem-vindo')
NameError: name 'Print' is not defined
>>> print ('Olá', +nome+ 'Seja muito bem vindo (a)!')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print ('Olá', +nome+ 'Seja muito bem vindo (a)!')
TypeError: bad operand type for unary +: 'str'
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome? Ana
Olá, nome, seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome? Ana
Olá, + nome +, seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome?Ana
Olá Ana seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome?Ana
Olá, Ana seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome?Ana
Olá, Ana , seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome?Ana
Olá, Ana ,, seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome?Ana
Olá, Ana ,seja muito bem vindo!
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Qual é o seu nome?Jisoo
Olá, Jisoo ,seja muito bem vinda(o)!
>>> 
>>> 
>>> ## Desafio 02
>>> 
>>> ## Crie um script python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
26091999
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
dia/ mês/ano
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
dia/mês/ano
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
dia/ mês/ ano
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
Você nasceu no dia 26 de 09 ano de ano
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
Você nasceu no dia 26 de 09 ano de ano. Confirma?
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
Você nasceu no dia 26 de 09 ano de ano. Confirma?
Ou, dizendo de outra forma, 26 / mês/ ano
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Em qual dia você nasceu?26
E em qual mês?09
De qual ano?1999
Você nasceu no dia 26 de 09 ano de ano. Confirma?
Ou, dizendo de outra forma, 26 / 09 / 1999
>>> 
>>> 
>>> dia = input ('Em qual dia você nasceu?')
mês = input ('E em qual mês?')
ano = input ('De qual ano?')
print ('Você nasceu no dia', dia, 'de', mês, 'ano de', 'ano''. Confirma?')

print ('Ou, dizendo de outra forma,',dia , '/', mês, '/', ano)

SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> Desafio 03
SyntaxError: invalid token
>>> ## Desafio 03
>>> ## Crie um script python que leia dois numeros e tente mostrar a soma entre eles
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Primeiro numero:5
Segundo numero:5
55
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Primeiro numero:5
Segundo numero:5
Traceback (most recent call last):
  File "C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py", line 3, in <module>
    result = int(num1) + int(num2)
NameError: name 'num1' is not defined
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Primeiro numero:5
Segundo numero:5
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/teste.py =========
Primeiro numero:5
Segundo numero:5
O resultado da soma é 10
>>> 
