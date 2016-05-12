import math
figura = int(input("Ingrese un numero de lados de una figura geometrica : "))

if figura == 2:
    print ('no hay figuras geometricas formadas por dos lados')

elif figura == 3:
	a = int(input("ingrese el lado 1 del triangulo: "))
	b = int(input("ingrese el lado 2 del triangulo: "))
	c = int(input("ingrese el lado 3 del triangulo: "))
	
	s = (a + b + c)/2

	def areaT():
		area = math.sqrt(s*(s - a)*(s - b)*(s - c))
		print ("Area = " + str(area))

	def perimetroT():
		per = a + b +c
		print ("Perimetro = " + str(per))

	perimetroT()
	areaT()

elif figura == 4:
	lado = int(input("Ingrese el lado del cuadrado: "))

	def areaCir():
		area = lado**2
		print ("Area = " + str(area))

	def perimetroC():
		per = lado * 4
		print("Perimetro = " + str(per))

	areaCir()
	perimetroC()

elif figura == 5:
	lado1= int (input("Ingrese el lado del pentagono:"))
	centro= int (input("Ingrese el centro del pentagono:"))
	
	def perimetro_areaP():
		Perm =5*lado1
		cn= lado1/2
		a= (centro * centro)- (cn * cn)
		b= math.sqrt(a)
		Apotema = (Perm *b)/2
		print (round(Perm,2))
		print (round(Apotema,2))
	pentagono = perimetro_areaP()
	print (pentagono)