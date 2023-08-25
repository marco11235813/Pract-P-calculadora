
def factorial(numero):
  """ devuelve el factorial de un numero

  """
  if numero >1:
    numero=numero*factorial(numero-1)
  return numero





class calcular:


        
    def __init__(self):
        print("\nOperaciones:\n\n+ --> Suma\n- --> Resta\n* --> Multiplicación\n/ --> División\n// --> División (cociente entero)\n! --> Factorial\n** --> Potenciación")
        self.numeros= input('\nIngresa la operacion que quieres realizar: ')



    def suma(self):
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
    def factorial(self):
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





calculadora= calcular()
calculadora.division()



## no recibe numeros tipo float, ya que directamente convierte cualquier numero ingresado en int
## optimizar para que realice mas de una operacion a la vez
## agregar mas opciones para operar(raiz, etc)
## error si ingresamos solo un valor