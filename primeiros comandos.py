Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## Primeiros passos em Python
>>> ## Exercicios realizados durante a aula de Python do Curso em Video
>>> ## Professor Gustavo Guanabara
>>> ## Executados em agosto de 2018
>>> 
>>> ## Para mostrar/printar frases é necessário usar aspas
>>> print ('Hello, World!')
Hello, World!
>>> 
>>> ## Para a soma, estrutura é parecida, mas não se usa aspas
>>> print (5+7)
12
>>> print (8+9)
17
>>> print (26+99)
125
>>> print (50+50)
100
>>> print (18+18)
36
>>> 
>>> ## Se utilizarmos aspas, os numeros serão considerados texto e colocados lado a lado
>>> print ('2'+'6')
26
>>> 
>>> ## Também podemos fazer calculos sem utilizar o comando print
>>> 5+7
12
>>> 8+9+22
39
>>> 
>>> ## Para atribuir valores às variáveis, usamos o simbolo de igual (recebe)
>>> 
>>> nome = 'Jennie'
>>> idade = 21
>>> peso = 50.1
>>> 
>>> ## Para mostrar os valores atribuidos
>>> print (nome + idade + peso)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print (nome + idade + peso)
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> print (nome, idade, peso)
Jennie 21 50.1
>>> 
>>> ## Como pôde ser observado, nesse caso é necessário o uso de virgula
>>> 
>>> ## Podemos fazer um modelo para completar e interagir
>>> 
>>> 
======== RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/testando.py ========
Qual é o seu nome? Lisa
Quantos anos você tem? 20
E quanto você pesa? 46.1
Ok, você é a  Lisa tem  20 anos e pesa  46.1 . Estou certa?
>>> 
>>> ## Testando com alguns ajustes
>>> 
======== RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/testando.py ========
Qual é o seu nome? Jisoo
Quantos anos você tem? 22
E quanto você pesa?45.1
Ok, você é a  Jisoo , tem  22 anos e pesa 45.1 kgs. Estou certa?
>>> 
>>> ## Agora começam os desafios!
>>> ## Desafio 01: Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/grupo.py =========
Olá, qual é o seu nome? Jennie
Vi, que você canta em um grupo, qual é o nome dele? BlackPink
Olá,  Jennie Eu sou adoro as musicas do  BlackPink . É uma horna te-la conosco
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/grupo.py =========
Olá, qual é o seu nome? Rosé
Vi, que você canta em um grupo, qual é o nome dele? BlackPink
Olá,  Rosé ! Eu adoro as musicas do  BlackPink . É uma horna te-la conosco
>>> 
>>> ## Desafio 02
>>> ## Crie um script Python que leia o dia, o mês e o ano de nsacimento de uma pessoa e mostre a mensagem com a data formatada.
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/grupo.py =========
Em qual dia você nasceu? 26
E em qual mês? 09
De qual ano? 1999
Você nasceu no dia  26 de  09 ano de ano. Confirma?
Ou, dizendo de outra forma,  26 /  09 /  1999
>>> 
>>> ## Desafio 03: Crie um script Python que leia dois numeros e tente mostrar uma soma entre eles.
>>> 
>>> ## A primeira tentativa juntou os dois numeros, mas depois consegui
>>> 
>>> 
========= RESTART: C:/Users/Ana Beatriz/Desktop/scripts-py/grupo.py =========
Primeiro numero: 25
Segundo numero: 4
O resultado da soma é 29 . Acertei?
>>> 
>>> ## PS: As palavras estão diferentes das usadas pelo professor, porque refiz e adaptei alguns detalhes.
