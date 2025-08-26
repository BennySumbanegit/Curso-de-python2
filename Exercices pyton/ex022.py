nome = str(input('Digite seu nome completo:'))

semespacos = nome.replace(' ','')

dividir = nome.split(nome[0:5])

print('ola',nome,'!')
print('o seu nome tem ',len(nome) ,'çaracteres')
print('O seu nome em maiusculas fica',nome.upper())
print('o seu nome em minusculas fica',nome.lower())
print('o seu nome sem espacos fica com',len(semespacos) ,'caracteres')
print('o primeiro bloco do seu nome dividido', dividir)