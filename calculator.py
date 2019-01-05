#Declaración de variables
opcion = 0

# Declaración de métodos
def suma(a, b):
	return a + b
	
def resta(a, b):
	return a - b
	
def multiplicar(a, b):
	return a * b
	
def dividir(a, b):
	return a / b
	
# Inicio del programa
while (opcion != 5):
	try:
		opcion = int(input('''Seleccione la operación a realizar: 
		1. Suma
		2. Resta
		3. Multiplicación
		4. División
		5. Salir
		'''))
		
		if (opcion == 1):
			num1 = input('Ingrese su primer número: ')
			num2 = input('Ingrese su segundo número: ')
			try:
				nums = [int(num1), int(num2)]
				print('La suma de ' + num1 + ' + ' + num2 + ' es: ' + str(suma(*nums)))
			except ValueError:
				print('Se debe introducir sólo números')
		elif (opcion == 2):
			num1 = input('Ingrese su primer número: ')
			num2 = input('Ingrese su segundo número: ')
			nums = [int(num1), int(num2)]
			print('La resta de ' + num1 + ' - ' + num2 + ' es: ' + str(resta(*nums)))
		elif (opcion == 3):
			num1 = input('Ingrese su primer número: ')
			num2 = input('Ingrese su segundo número: ')		
			try:
				nums = [float(num1), float(num2)]
				print('La multiplicación de ' + num1 + ' x ' + num2 + ' es: ' + str(multiplicar(*nums)))
			except ValueError:
				print('Se debe introducir sólo números')
		elif (opcion == 4):
			num1 = input('Ingrese su primer número: ')
			num2 = input('Ingrese su segundo número: ')
			try:
				nums = [float(num1), float(num2)]
				try:
					print('La división de ' + num1 + ' / ' + num2 + ' es: ' + str(dividir(*nums)))
				except ZeroDivisionError:
					print('No se puede dividir por 0.')
			except ValueError:
				print('Se debe introducir sólo números')
		elif ((opcion == 0) or (opcion > 5)):
			print('Opción inválida.')
		
		if (opcion != 5):
			print('Pulse enter para continuar...')
	except ValueError:
		print('Se debe introducir sólo números')
		
print('Fin del Programa')
		
