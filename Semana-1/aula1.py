
"""
Raiz de Equação Quadrática a.x² +b.x +c"
"""
#Importação da biblioteca math para usar funções matemáticas
import math
#Essa função calcula as raízes de uma equação quadrática, tratando casos especiais.    
def zeros(a,b,c):

#exercicio 1(Passo 1 – Caso especial:a = 0)
#Serão passados os coeficientes a, b e c. Caso a = 0, resolva como uma equação do primeiro grau, e se b = 0 gere uma exceção.
#Passo 1 – Caso especial:a = 0
    if a == 0:# Se 𝑎= 0, a equação não é quadrática, mas sim linear (𝑏𝑥+𝑐=0).
        if b == 0:# Se b também for 0,não existe solução (seria 0x+c=0).
            raise ValueError("A equação não possui solução")#
        else:# Caso contrário, resolve a equação linear retornando x= -c/b. 
            return -c/b

#Passo 2 – Calcular o discriminante (delta)
    delta = b**2 - (4*a*c) #
    if delta < 0:# não há solução real.
        return None #significa que não existem raízes reais.
    
    elif delta == 0:# existe uma raiz real dupla.
        x = -b/(2*a)
        return[x,x]#calcula a única raiz e retorna duas vezes no formato [x,x]
    else:# delta > 0 existem duas raízes reais diferentes.

#calcula as duas raízes usando a fórmula de Bhaskara:
        x1 = (-b + math.sqrt(delta))/(2*a)# uma usando a biblioteca math
        x2 = (-b - delta**0.5)/(2*a)# a outra usando 0,5
        return[x1,x2]

#3. Função main()
def main():
    x= zeros(1,-5,6)#Chama a função zeros com os coeficientes a= 1,b=−5, c=6.Chama a função zeros com os coeficientes a= 1,b=−5, c=6.
    print(x)# impressão na tela do valor de x.

#4.Estrutura de execução
#Isso garante que o código dentro de main() só será executado se o arquivo for rodado diretamente, e não quando importado como módulo.
if __name__ =="__main__":
    main()

   


    

    
    

