def factorial(numero):
  """ devuelve el factorial de un numero

  """
  if numero >1:
    numero=numero*factorial(numero-1)
  return numero


 


class calcular:
        
    """Programa que funciona como calculadora, consta de las operaciones basicas e incluye algunas un poco mas complejas
    (suma,resta,multiplicacion,division,factorial,raiz,potencia
    se ingresa un numero (o numeros segun corresponda), con el simbolo de la operacion a realizar, como si fuera una sintaxis normal de operacion
    en una hoja)
    """




    def __init__(self):
        print("\nOperaciones:\n\n+ --> Suma\n- --> Resta\n* --> Multiplicación\n/ --> División\n// --> División (cociente entero)\n! --> Factorial\n** --> Potenciación\nrad --> Raíz")
        self.numeros= input('\nIngresa la operacion que quieres realizar: ')


    def suma(self):
        """se ingresan los numeros y el simbolo '+'
        entre ellos
        """

        suma= 0
        for x in self.numeros:
            if '+' in self.numeros:
                numeros= self.numeros.split('+')
                numeros= [int(x) for x in numeros]
        for numero in numeros:
            suma += numero
        print(suma)
        return
    
    def resta(self):

        """se ingresan los numeros y el simbolo '-'
        entre ellos
        """


        for x in self.numeros:
            if '-' in self.numeros:
                numeros= self.numeros.split('-')
                numeros= [int(x) for x in numeros]
        for index, nro in enumerate(numeros):
            if index == 0:
                resta = nro
            else:
                resta -= nro
        print(resta)
        return
    
    def multiplicacion(self):

        """se ingresan los numeros y el simbolo '*'
        entre ellos
        """       

        multi= 0
        for x in self.numeros:
            if '*' in self.numeros:
                numeros= self.numeros.split('*')
                numeros= [int(x) for x in numeros]
        for index, nro in enumerate(numeros):
            if index == 0:
                multi = nro
            else:
                multi *= nro
        print(multi)
        return
    
    def division(self):

        """se ingresan los numeros y el simbolo '/'
        entre ellos
        """

        div= 0
        for x in self.numeros:
            if '/' in self.numeros:
                numeros= self.numeros.split('/')
                numeros= [int(x) for x in numeros]
        for index, nro in enumerate(numeros):
            if index == 0:
                div = nro
            else:
                div /= nro
        print(div)
        return
    
    def potencia(self):

        """se ingresan los numeros y el simbolo '**'
        entre ellos
        """

        pot= 0
        for x,num in enumerate(self.numeros):
            if '**' in self.numeros:
                numeros= self.numeros.split('**')
                numeros= [int(x) for x in numeros]
        for index, nro in enumerate(numeros):
            if index == 0:
                pot = nro
            else:
                pot **= nro
        print(pot)
        return
    
    def raiz(self):

        """se ingresan los numeros y la expresion 'rad'
        entre ellos
        """

        radical= 0
        for x,num in enumerate(self.numeros):
            if 'rad' in self.numeros:
                numeros= self.numeros.split('rad')
                numeros= [int(x) for x in numeros]
        for index, nro in enumerate(numeros):
            if index == 0:
                radical = nro
            else:
                radical= radical ** (1/nro)
        print(radical)
        return
    
    def factorial(self):

        """se ingresa el numero y luego el simbolo '!'
        """

        for x in self.numeros:
            if '!' in self.numeros:
                numeros= self.numeros.split('!')
                numeros= [int(x) for x in numeros if x.isdigit()]
                for numero in numeros:
                    if int(numero) >1:
                        numero=int(numero)*factorial(int(numero)-1)
                        print(numero)
                        return
                    elif int(numero) == 1:
                        print(numero)
                        return

def interfaz():

     print("\nOperaciones:\n\n+ --> Suma\n- --> Resta\n* --> Multiplicación\n/ --> División\n! --> Factorial\n** --> Potenciación\nrad --> Raíz")
     simbolos= ['+','-','*','/','**','rad','!']
     calculadora= calcular()

     for x in simbolos:
         if x in calculadora.numeros:
             if x == '+':
                 operacion= calculadora.suma()
                 break
             elif x ==  '-':
                 operacion= calculadora.resta()
                 break
             elif x ==  '*':
                 if calculadora.numeros.count(x) == 2: 
                    operacion= calculadora.potencia()
                    break
                 else:
                     operacion= calculadora.multiplicacion()
                     break
             elif x ==  '/':
                 operacion= calculadora.division()
                 break
             elif x ==  'rad':
                 operacion= calculadora.raiz()
                 break
             elif x ==  '!':
                 operacion= calculadora.factorial()
                 break

         elif x not in calculadora.numeros:
             continue
         
             
     return operacion

     

def main():
    interfaz()
    return

main()


# if __name__ == '__main__': ### esta linea lo que evita es que, cuando importemos                      
#     main()                 ## este modulo para utilizar sus funcionalidades, se ejecute automaticamente
#                            ## sin ser el __main__.

                           
## no recibe numeros tipo float, ya que directamente convierte cualquier numero ingresado en int
## optimizar para que realice mas de una operacion a la vez
## error si ingresamos solo un valor