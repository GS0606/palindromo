

def eh_palindromo(palavra):
    palavra = palavra.lower() 
    palavra = palavra.replace(" ", "")  
    return palavra == palavra[::-1]

palavra_digitada = input("Digite uma palavra: ")
if eh_palindromo(palavra_digitada):
    print(f"{palavra_digitada} é um palíndromo!")
else:
    print(f"{palavra_digitada} não é um palíndromo.")
