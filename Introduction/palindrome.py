'''
Palíndromo

Ianerisson tem uma string s com apenas letras minúsculas de 'a' a 'z'. 
Ele quer modificar exatamente um caractere por outro de 'a' a 'z' 
de modo que a nova string seja um palíndromo.

Um palíndromo é uma string que possui a mesma sequência de caracteres, 
tanto de frente para trás, como de trás para frente. Por exemplo as strings "z", 
"aaa", "aba" e "abccba" são palíndromos, enquanto as strings "unb", 
"realidade" e "ab" não são palíndromos.

Entrada

A entrada possui uma única linha com uma string s de até 100 caracteres.

Saída

Imprima "POSSÍVEL" (sem as aspas duplas) se Ianerisson puder trocar exatamente 
um caractere para que a string resultante seja um palíndromo e 
"IMPOSSÍVEL" (sem as aspas duplas) caso contrário.


For example:

Input	
abccaa

Result
POSSÍVEL
'''

string = input()

count = 0

stringSize = len(string)

for i in range(stringSize//2):

    if string[i] != string[-i-1]:
        count += 1

if (count == 1) or (count == 0 and stringSize%2 != 0):
    print('POSSÍVEL')
else:
    print('IMPOSSÍVEL')