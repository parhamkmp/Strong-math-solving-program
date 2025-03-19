# Hello this code programmed by parham karimipour

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::----------------------------::::::::::::::::::::::::::
# ::::::::::::::::: |Welcome. Please dont copy |     :::::::::::::::::::::
# :::::::::::::::::	|Hello this code programmed|     :::::::::::::::::::::
# :::::::::::::::::	|by parham karimipour(2025)|     :::::::::::::::::::::
# ::::::::::::::::::----------------------------::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# ------------ Module imports ----------
import os 
from math import sqrt
import numpy as np
from math import pi
from math import radians,sin,cos,tan,log
# ------------ Module imports ----------


while True:

	#------ cmd color -----
	os.system('color e')
	os.system('cls')
	#------ cmd color -----




	#----------------------------------------------------------------- calcuting ------------------------------------------------------------------------
	try:
		# function solve 1st eq	
		def One_st_degree_equation():
			try:
				# Give a,b,c from client/user
				a = float(input('a: '))
				b = float(input('b: '))
				c = float(input('c: '))
				# solve eq
				x_answer = (c/a) - (b/a)
				return f'x answer is : {x_answer}'
			# Manage errors
			except ValueError:
				print('\n:::::\n Please do not leave the inputs empty and only fill them with numbers \n:::::\n ')
				One_st_degree_equation()

		# function solve second eq
		def Second_degree_equation():
			try:
				# Give a,b,c from client/user
				a =  float(input('a: ')) 
				b =  float(input('b: '))
				c =  float(input('c: '))
				# Calculate Delta
				delta = (b**2)-(4*a*c)
				if delta>0:
					# print anwsers(roots)
					x1 = (-b+sqrt(delta)) / (2*a)
					x2 = (-b-sqrt(delta)) / (2*a)
					return f'\n::::\nWe have two root.\n X1 : {x1}\n x2 : {x2}\nDelta: {delta}\n::::\n'
				elif delta == 0:
					# print anwser
					x = b / 2*a
					return f'\n::::\nwe have one root. x is : {x}\nDelta:{delta}\n::::\n'
				elif delta<0:
					return 'Delta<0 - this eq not have root. '
				else:
					return 'Error !'
			# Manage errors
			except ValueError:
				print('\n:::::\n Please do not leave the inputs empty and only fill them with numbers \n:::::\n ')
				Second_degree_equation()


		# function solve derivative
		def Derivative():
			try:
				print('\n:::::\nHello, this program can finally take the derivative of the 4th degree equation\n:::::\n')
				degree_fx = int(input('Enter the degree of the function f(x): '))
				if degree_fx==1:
					# f(x) = ax+b and f'(x) = a
					print('f(x)= ax + b')
					a = float(input('Enter a: '))
					return f'f′(x) = {a}\n::::'
				elif degree_fx==2:
					# f(x) = ax^2 + bx +c
					print('f(x) = ax^2 + bx + c')
					a = float(input('Enter a: '))
					b = float(input('Enter b: '))
					return f'f′(x) = {2*a}x + {b}\n::::'
				elif degree_fx==3:
					# f(x) = ax^3 + bx^2 + cx
					print('f(x) = ax^3 + bx^2 + cx + d')
					a = float(input('Enter a: '))
					b = float(input('Enter b: '))
					c = float(input('Enter c: '))
					return f'f′(x) = {a*3}x^2 + {2*b}x + {c}\n::::'
				elif degree_fx==4:
					# f(x) = ax^4 + bx^3 + cx^2 + dx + e
					print('f(x) = ax^4 + bx^3 + cx^2 + dx + e')
					a = float(input('Enter a: '))
					b = float(input('Enter b: '))
					c = float(input('Enter c: '))
					d = float(input('Enter d: '))
					return 'f′(x) = {a*4}x^3 + {b*3}x^2 + {2*c}x\n::::'
				else:
					return'\n::::\nNot defined\n::::'
					Derivative()
			except ValueError:
				return 'Please enter number!\n::::::'
			except KeyboardInterrupt:
				return 'You select exit!\n::::::'


		# function for matrix
		def Matrix():
			try:
				Matrix_operations_selection = input(f'::::\nFirst, let me say that this program finally supports up to 3*3 matrix Which operation do you want to perform on the matrix:\n1- Multiplication of two matrices(Rand matrices such as 2x2 and 3x3)\n2- Determinant of 2*2 or 3*3 matrix\n3- Main and minor diameter\n4- Multiply the number in the matrix\n5- Addition and subtraction of two matrices\n6- Transpose matrix\nEnter: ')
				
				# Multiplication of two matrices
				if Matrix_operations_selection==str(1):
					print(f'\n::::::Note that for A*B multiplication, the number of columns of matrix A must be equal to the number of rows of matrix B')
					row_a  = int(input('Enter A matrix row: '))
					column_a  = int(input('Enter A matrix column: '))
					row_b  = int(input('Enter B matrix row: '))
					column_b  = int(input('Enter B matrix column: '))

					# A*B
					if column_a == row_b:
						# (2*2 2*2) (3*3 3*3)
						if row_a==2 and column_a==2 and row_a==2 and column_b==2:
							print(':::: MATTIX VALUES ::::')
							print('\n:::: A ::::\n')
							a11 = int(input('Enter a11: '))
							a12 = int(input('Enter a12: '))
							a21 = int(input('Enter a21: '))
							a22 = int(input('Enter a22: '))
							A = np.array([ 
							[a11,a12], [a21,a22]
							])
							print('\n:::: B ::::\n')
							b11 = int(input('Enter b11: '))
							b12 = int(input('Enter b12: '))
							b21 = int(input('Enter b21: '))
							b22 = int(input('Enter b22: '))
							B = np.array([ 
							[b11,b12], [b21,b22]
							])
							print('\n::::::::\n')

							return f'A*B:\n{A.dot(B)}\n::::::'

						elif row_a==3 and column_a==3 and row_b==3 and column_b==3:
							print(':::: MATTIX VALUES ::::')
							print('\n:::: A ::::\n')
							a11 = int(input('Enter a11: '))
							a12 = int(input('Enter a12: '))
							a13 = int(input('Enter a13: '))
							a21 = int(input('Enter a21: '))
							a22 = int(input('Enter a22: '))
							a23 = int(input('Enter a23: '))
							a31 = int(input('Enter a31: '))
							a32 = int(input('Enter a32: '))
							a33 = int(input('Enter a33: '))
							A = np.array([ 
							[a11,a12,a13], [a21,a22,a23], [a13,a23,a33]
							])
							print('\n:::: B ::::\n')
							b11 = int(input('Enter b11: '))
							b12 = int(input('Enter b12: '))
							b13 = int(input('Enter b13: '))
							b21 = int(input('Enter b21: '))
							b22 = int(input('Enter b22: '))
							b23 = int(input('Enter b23: '))
							b31 = int(input('Enter b31: '))
							b32 = int(input('Enter b32: '))
							b33 = int(input('Enter b33: '))
							B = np.array([ 
							[b11,b12,b13], [b21,b22,b23], [b13,b23,b33]
							])
							print('\n:::::::::\n')

							return f'A*B:\n{A.dot(B)}'


					elif column_a != row_b:
						return 'A and B (matrix) are not multiplied\n::::::'

					else:
						return 'Please enter 2*2 and 3*3 matrix! thanks.\n::::::'

				# det or |A|
				elif Matrix_operations_selection==str(2):
					Matrix_type = input('\n::::::\nMatrix Determinant(2*2 or 3*3)\nif your matrix 2*2 enter (2) if 3*3 enter(3)\nEnter: ')
					if Matrix_type == str(2):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))

						print('\n:::::::::\n')

						return f'det(A) / |A| = {(a11*a22) - (a12*a21)}'


					elif Matrix_type==str(3):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a13 = int(input('Enter a13: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))
						a23 = int(input('Enter a23: '))
						a31 = int(input('Enter a31: '))
						a32 = int(input('Enter a32: '))
						a33 = int(input('Enter a33: '))
						# For saros way
						a14 = a11
						a15 = a12
						a24 = a21
						a25 = a22
						a34 = a31
						a35 = a32

						print('\n::::::::\n')

						return f'det(A) / |A| = {((a11*a22*a33)+(a12*a23*a34)+(a13*a24*a35)) - ((a15*a24*a33)+(a14*a23*a32)+(a13*a22*a31))}'
					else:
						return 'Not defined !\n::::'

				# diameter
				elif Matrix_operations_selection==str(3):
					Matrix_type = input('\n::::To get the square on the main and sub diameter of the 2x2 matrix, enter the number 2 and for 3x3, enter the number 3.\nEnter: ')
					if Matrix_type==str(2):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))

						return f'Main diameter: {a11}, {a22}\nSub diameter: {a12}, {a21}'

						print('\n:::::::::\n')


					elif Matrix_type==str(3):

						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a13 = int(input('Enter a13: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))
						a23 = int(input('Enter a23: '))
						a31 = int(input('Enter a31: '))
						a32 = int(input('Enter a32: '))
						a33 = int(input('Enter a33: '))

						return f'Main diameter: {a11},{a22},{a33}\nSub diameter: {a12},{a22},{a13}'

						print('\n:::::::::\n')

					else:
						return 'Not defined!\n::::'

				# Multiply the number in the matrix
				elif Matrix_operations_selection==str(4):
					Matrix_type = input('\n::::\nFirst, enter your matrix, then multiply the number you want by it.If your matrix`s is 2x2, enter the number 2 and if it is 3x3, enter the number 3.\nEnter: ')
					Multiplicative_number = int(input('::::\nEnter the number you want to multiply in the matrix: '))
					if Matrix_type==str(2):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))
						A = np.array([ 
							[a11*Multiplicative_number,a12*Multiplicative_number], [a21*Multiplicative_number,a22*Multiplicative_number]
						])

						return f'Final matrix:\n{A}' 

						print('\n:::::::::\n')

					elif Matrix_type==str(3):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a13 = int(input('Enter a13: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))
						a23 = int(input('Enter a23: '))
						a31 = int(input('Enter a31: '))
						a32 = int(input('Enter a32: '))
						a33 = int(input('Enter a33: '))
						A = np.array([ 
							[a11*Multiplicative_number,a12*Multiplicative_number,a13*Multiplicative_number], [a21*Multiplicative_number,a22*Multiplicative_number,a23*Multiplicative_number], [a13*Multiplicative_number,a23*Multiplicative_number,a33*Multiplicative_number]
						])
						
						return f'Final matrix:\n{A}'

						print('\n::::::::\n')

					else:
						return 'Not defined!\n::::'

				# Addition and subtraction of matrices
				elif Matrix_operations_selection==str(5):
					Addition_subtraction = input('You want Addition(enter A) or subtraction(enter S) ?: ')
					if Addition_subtraction == 'A' or Addition_subtraction == 'a':
						Matrix_type = input('\n::::\nTo calculate the addition and subtraction of two matrices, both must be 2x2 or both 2x3. If they are 2x2, enter the number 2, and if they are 3x3, enter the number 3\nEnter: ')
						if Matrix_type==str(2):
							print(':::: MATTIX VALUES ::::')
							print('\n:::: A ::::\n')
							a11 = int(input('Enter a11: '))
							a12 = int(input('Enter a12: '))
							a21 = int(input('Enter a21: '))
							a22 = int(input('Enter a22: '))
							A = np.array([ 
							[a11,a12], [a21,a22]
							])
							print('\n:::: B ::::\n')
							b11 = int(input('Enter b11: '))
							b12 = int(input('Enter b12: '))
							b21 = int(input('Enter b21: '))
							b22 = int(input('Enter b22: '))
							B = np.array([ 
							[b11,b12], [b21,b22]
							])

							return f'A+B:\n{A+B}'

							print('\n:::::::::\n')

						elif Matrix_type==str(3):
							print(':::: MATTIX VALUES ::::')
							print('\n:::: A ::::\n')
							a11 = int(input('Enter a11: '))
							a12 = int(input('Enter a12: '))
							a13 = int(input('Enter a13: '))
							a21 = int(input('Enter a21: '))
							a22 = int(input('Enter a22: '))
							a23 = int(input('Enter a23: '))
							a31 = int(input('Enter a31: '))
							a32 = int(input('Enter a32: '))
							a33 = int(input('Enter a33: '))
							A = np.array([ 
							[a11,a12,a13], [a21,a22,a23], [a13,a23,a33]
							])
							print('\n:::: B ::::\n')
							b11 = int(input('Enter b11: '))
							b12 = int(input('Enter b12: '))
							b13 = int(input('Enter b13: '))
							b21 = int(input('Enter b21: '))
							b22 = int(input('Enter b22: '))
							b23 = int(input('Enter b23: '))
							b31 = int(input('Enter b31: '))
							b32 = int(input('Enter b32: '))
							b33 = int(input('Enter b33: '))
							B = np.array([ 
							[b11,b12,b13], [b21,b22,b23], [b13,b23,b33]
							])

							return f'A+B:\n{A+B}'
							print('\n:::::::::\n')
						else:
							return 'Not defined!\n::::::' 
					elif Addition_subtraction == 'S' or Addition_subtraction == 's':
						Matrix_type = input('\n::::\nTo calculate the addition and subtraction of two matrices, both must be 2x2 or both 2x3. If they are 2x2, enter the number 2, and if they are 3x3, enter the number 3\nEnter: ')
						if Matrix_type==str(2):
							print(':::: MATTIX VALUES ::::')
							print('\n:::: A ::::\n')
							a11 = int(input('Enter a11: '))
							a12 = int(input('Enter a12: '))
							a21 = int(input('Enter a21: '))
							a22 = int(input('Enter a22: '))
							A = np.array([ 
							[a11,a12], [a21,a22]
							])
							print('\n:::: B ::::\n')
							b11 = int(input('Enter b11: '))
							b12 = int(input('Enter b12: '))
							b21 = int(input('Enter b21: '))
							b22 = int(input('Enter b22: '))
							B = np.array([ 
							[b11,b12], [b21,b22]
							])

							return f'A+B:\n{A-B}'

							print('\n:::::::::\n')		

						elif Matrix_type==str(3):
							print(':::: MATTIX VALUES ::::')
							print('\n:::: A ::::\n')
							a11 = int(input('Enter a11: '))
							a12 = int(input('Enter a12: '))
							a13 = int(input('Enter a13: '))
							a21 = int(input('Enter a21: '))
							a22 = int(input('Enter a22: '))
							a23 = int(input('Enter a23: '))
							a31 = int(input('Enter a31: '))
							a32 = int(input('Enter a32: '))
							a33 = int(input('Enter a33: '))
							A = np.array([ 
							[a11,a12,a13], [a21,a22,a23], [a13,a23,a33]
							])
							print('\n:::: B ::::\n')
							b11 = int(input('Enter b11: '))
							b12 = int(input('Enter b12: '))
							b13 = int(input('Enter b13: '))
							b21 = int(input('Enter b21: '))
							b22 = int(input('Enter b22: '))
							b23 = int(input('Enter b23: '))
							b31 = int(input('Enter b31: '))
							b32 = int(input('Enter b32: '))
							b33 = int(input('Enter b33: '))
							B = np.array([ 
							[b11,b12,b13], [b21,b22,b23], [b13,b23,b33]
							])

							return f'A+B:\n{A-B}'
							print('\n:::::::::\n')	
						else:
							return 'not defined!\n::::::'
					else:
						return 'not defined!\n::::::'

				# Matrix transpose 
				elif Matrix_operations_selection==str(6):
					Matrix_type = input('\nTo calculate the transpose of a matrix, first specify the matrix.\nIf 2 is 2, enter the number 2, and if 3 is 3, enter the number 3: ')
					if Matrix_type == str(2):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))
						A = np.array([ 
						[a11,a12], [a21,a22]
						])
						return f'Transpose:\n{A.T}'
						print('\n:::::\n')

					elif Matrix_type == str(3):
						print(':::: MATTIX VALUES ::::')
						a11 = int(input('Enter a11: '))
						a12 = int(input('Enter a12: '))
						a13 = int(input('Enter a13: '))
						a21 = int(input('Enter a21: '))
						a22 = int(input('Enter a22: '))
						a23 = int(input('Enter a23: '))
						a31 = int(input('Enter a31: '))
						a32 = int(input('Enter a32: '))
						a33 = int(input('Enter a33: '))
						A = np.array([ 
							[a11,a12,a13], [a21,a22,a23], [a13,a23,a33]
						]) 
						return f'Transpose:\n{A.T}'
						print('\n:::::\n')


				else:
					return 'Not defined!\n:::'


			# errors manager
			except ValueError:
				return '\n:::\nPlease enter number !!!\n:::'	
			except KeyboardInterrupt:
				return '\n:::\nYou select exit!\n:::'


		# Calculate the perimeter of shapes
		def Perimeter():
			try:
				print('\n:::::\nWelcome to (P)erimeter calculate\n:::::')
				def square():
					a = int(input('Enter the side size'))
					return f'(P)erimeter: {a*4}'
					print('\n:::::::\n')

				def triangle():
					a = int(input('Enter a side size: '))
					b = int(input('Enter b side size: '))
					c = int(input('Enter c side size: '))
					return f'(P)erimeter: {a+b+c}'
					print('\n:::::::\n')

				def rectangle():
					length = int(input('Enter length size: '))
					width = int(input('Enter width dize: '))
					return f'(P)erimeter: {(length+width)*2}'
					print('\n:::::::\n')

				def trapezoid():
					a = int(input('Enter a side size: '))
					b = int(input('Enter b side size: '))
					c = int(input('Enter c side size: '))
					d = int(input('Enter d side size: '))
					return f'(P)erimeter: {a+b+c+d}'
					print('\n:::::::\n')

				def parallelogram():
					length = int(input('Enter length size: '))
					width = int(input('Enter width dize: '))
					return f'(P)erimeter: {(length*2) + (width*2)}'
					print('\n:::::::\n')
				
				def circle():
					Radius = int(input('Enter Radius size: '))
					return f'(P)erimeter: {2*Radius*pi}'
					print('\n:::::::\n')
				
				def rhombus():
					a = int(input('Enter a side size: '))
					return f'(P)erimeter: {a*4}'
					print('\n:::::::\n')

				mode = int(input('Perimeter Which shape do you want?\n1-square\n2-triangle\n3-rectangle\n4-trapezoid\n5-parallelogram\n6-circle\n7-rhombus\nENTER: '))
				if mode == 1:
					return square()
				elif mode == 2:
					return triangle()
				elif mode == 3:
					return rectangle()
				elif mode == 4:
					return trapezoid()
				elif mode == 5:
					return parallelogram()
				elif mode == 6:
					return circle()
				elif mode == 7:
					return rhombus()
				else:
					return '\n::::\nnot defined!\n::::'
			except ValueError:
				return 'Please enter number!\n::::::'
			except KeyboardInterrupt:
				return 'You select exit!\n::::::'


		# Calculate the area shapes
		def Area():
			try:
				print('\n:::::\nWelcome to (A)rea calculate\n:::::')
				def square():
					a = int(input('Enter a side size: '))
					return f'(S)urvey: {a*a}'
					print('\n:::::::\n')

				def triangle():
					height = int(input('Enter the height: '))
					rule = int(input('Enter the rule: '))
					return f'(S)urvey: {(height*rule)/2}'
					print('\n:::::::\n')

				def rectangle():
					length = int(input('Enter length size: '))
					width = int(input('Enter width dize: '))
					return f'(S)urvey: {length*width}'
					print('\n:::::::\n')

				def trapezoid():
					rule1 = int(input('Enter rule1 size: '))
					rule2 = int(input('Enter rule2 size: '))
					length = int(input('Enter length size: '))
					return f'(S)urvey: {((rule1+rule2)*length)/2}'
					print('\n:::::::\n')

				def parallelogram():
					height = int(input('Enter the height: '))
					rule = int(input('Enter the rule: '))
					return f'(S)urvey: {height*rule}'
					print('\n:::::::\n')
				
				def circle():
					Radius = int(input('Enter Radius size: '))
					return f'(S)urvey: {pi*Radius**2}'
					print('\n:::::::\n')
				
				def rhombus():
					Large_diameter = int(input('Enter Large diameter: '))
					Small_diameter = int(input('Enter Small diameter: '))
					return f'(S)urvey: {(Large_diameter*Small_diameter)/2}'
					print('\n:::::::\n')

				def sphere():
					Radius = int(input('Enter Radius size: '))
					return f'(S)urvey: {((Radius**2)*pi)*4}'
					print('\n:::::::\n')

				def Hemisphere_Full():
					Radius = int(input('Enter Radius size: '))
					return f'(S)urvey: {((Radius**2)*pi)*3}'
					print('\n:::::::\n')

				def Hemisphere_Empty():
					Radius = int(input('Enter Radius size: '))
					return f'(S)urvey: {((Radius**2)*pi)*2}'
					print('\n:::::::\n')

				mode = int(input('What area do you want?\n1-square\n2-triangle\n3-rectangle\n4-trapezoid\n5-parallelogram\n6-circle\n7-rhombus\n8-Hemisphere_Full\n9-Hemisphere_Empty\nENTER: '))
				if mode == 1:
					return square()
				elif mode == 2:
					return triangle()
				elif mode == 3:
					return rectangle()
				elif mode == 4:
					return trapezoid()
				elif mode == 5:
					return parallelogram()
				elif mode == 6:
					return circle()
				elif mode == 7:
					return rhombus()
				elif mode == 8:
					return Hemisphere_Full()
				elif mode == 9:
					return Hemisphere_Empty()
				else:
					return '\n::::\nnot defined!\n::::'
			except ValueError:
				return 'Please enter number!\n::::::'
			except KeyboardInterrupt:
				return 'You select exit!\n::::::'

		# Calculate the Value of shapes
		def Volume():
			try:
				def cube():
					a = int(input('Enter the size of the side of the cube: '))
					return f'(V)olume: {a**3}'
					print('\n:::::::\n')

				def Rectangular_Cube():
					length = int(input('Enter length size: '))
					width = int(input('Enter width dize: '))
					height = int(input('Enter height dize: '))

					return f'(V)olume: {height*width*length}'
					print('\n:::::::\n')

				mode = int(input('What volume do you want?\n1-Cube\n2-Rectangular_Cube\nENTER: '))
				if mode == 1:
					return cube()
				elif mode == 2:
					return Rectangular_Cube()
			except ValueError:
				return 'Please enter number!\n::::::'
			except KeyboardInterrupt:
				return 'You select exit!\n::::::'


		# Calculation of trigonometric ratios
		def Trigonometric_Ratios():
			try:
				def Sin():
					print('\n::::\nGetting the sin\n::::\n')
					angle = input('Enter the desired angle in degrees: ')
					if int(angle) == 60:
						sin_angle = '√3/2'
					elif int(angle) == 45:
						sin_angle = '√2/2'
					elif int(angle) > 1 or int(angle) < -1:
						sin_angle = 'Sin not defined !'
					else:
						sin_angle = round(sin(radians(int(angle))),3)
					
					return f'Sin{angle}: {sin_angle}'
					print('\n::::\n')

				def Cos():
					print('\n::::\nGetting the cos\n::::\n')
					angle = input('Enter the desired angle in degrees: ')
					if int(angle) == 30:
						cos_angle = '√3/2'
					elif int(angle) == 45:
						cos_angle = '√2/2'
					elif int(angle) > 1 or int(angle) < -1:
						cos_angle = 'Cos not defined !'
					else:
						cos_angle = round(cos(radians(int(angle))),3)

					return f'Cos{angle}: {cos_angle}'
					print('\n::::\n')

				def Tan():
					print('\n::::\nGetting the tan\n::::\n')
					angle = input('Enter the desired angle in degrees: ')
					if int(angle) == 30:
						tan_angle = '√3/3'
					elif int(angle) == 60:
						tan_angle = '√3'
					elif int(angle) > 1 or int(angle) < -1:
						tan_angle = 'Tan not defined !'
					else:
						tan_angle = round(tan(radians(int(angle))),3)

					return f'Tan{angle}: {tan_angle}'
					print('\n::::\n')

				def Cot():
					print('\n::::\nGetting the tan\n::::\n')
					angle = input('Enter the desired angle in degrees: ')
					if angle == 30:
						tan_angle = '√3'
					elif angle == 60:
						tan_angle = '√3/3'
					elif int(angle) > 1 or int(angle) < -1:
						cot_angle = 'Cot not defined !'
					else:
						tan_angle = round(tan(radians(int(angle))),3)

					return f'Tan{angle}: {1/tan_angle}'
					print('\n::::\n')


				def Sin_sum_differentiation_two_angles():
					print('\n::::\nThe sum and Differentiation of the sin`s of two angles: sin(α+β)\n::::')
					alpha = input('Enter α: ')
					beta = input('Enter β: ')
					sin_alpha = round(sin(radians(int(alpha))),3)
					sin_beta = round(sin(radians(int(beta))),3)
					cos_alpha = round(cos(radians(int(alpha))),3)
					cos_beta = round(cos(radians(int(beta))),3)
					if   sin_alpha > 1 and  sin_alpha < -1 and  sin_beta > 1 and  sin_beta < -1 and  cos_alpha > 1 and cos_alpha < -1 and  cos_beta > 1 and cos_alpha < -1  :
						return 'Sinα or cosα or sinβ or cosβ is undifined ! \n::::::'

					else:
						Sum = (sin_alpha*cos_beta) + (cos_alpha*sin_beta)
						Differentiation = (sin_alpha*cos_beta) - (cos_alpha*sin_beta)
						return f'\n::::\nsum: {round(Sum,3)}\nDifferentiation:{round(Differentiation,3)}\n::::'


				def Cos_sum_differentiation_two_angles():
					print('\n::::\nThe sum and Differentiation of the cose`s of two angles: cos(α+β)\n::::')
					alpha = input('Enter α: ')
					beta = input('Enter β: ')
					sin_alpha = round(sin(radians(int(alpha))),3)
					sin_beta = round(sin(radians(int(beta))),3)
					cos_alpha = round(cos(radians(int(alpha))),3)
					cos_beta = round(cos(radians(int(beta))),3)
					if  sin_alpha > 1 and  sin_alpha < -1 and  sin_beta > 1 and  sin_beta < -1 and cos_alpha > 1 and cos_alpha < -1 and cos_beta > 1 and cos_alpha < -1  :
						return 'Sinα or cosα or sinβ or cosβ is undifined ! \n::::::'
					else:
						Sum = (cos_alpha*cos_beta) - (sin_alpha*sin_beta)
						Differentiation = (cos_alpha*cos_beta) + (sin_alpha*sin_beta)
						return f'\n::::\nsum: {round(Sum,3)}\nDifferentiation:{round(Differentiation,3)}\n::::'
				

				def Tan_sum_differentiation_two_angles():
					print('\n::::\nThe sum and Differentiation of the Tan`s of two angles: tan(α+β)\n::::')
					alpha = input('Enter α: ')
					beta = input('Enter β: ')
					tan_alpha = round(sin(radians(int(alpha))),3)
					tan_beta = round(sin(radians(int(beta))),3)
					if  tan_alpha > 1 and  tan_alpha < -1  :
						return 'tan α is undifined ! \n::::::'
					else:
						Sum = (tan_alpha+tan_beta)/(1-tan_alpha*tan_beta)
						Differentiation = (tan_alpha-tan_beta)/(1+tan_alpha*tan_beta)
						return f'\n::::\nsum: {round(Sum,3)}\nDifferentiation:{round(Differentiation,3)}\n::::'




				mode = input('\n:::::\nWhich trigonometric ratio do you want?\n1-sin\n2-cos\n3-tan\n4-cot\n5-Addition and subtraction of the sin`s of two angles\n6-Addition and subtraction of the cos`s of two angles\n7-Addition and subtraction of the tan`s of two angles\nENTER: ')
				if int(mode) == 1:
					return Sin()
				elif int(mode) == 2:
					return Cos()
				elif int(mode) == 3:
					return Tan()
				elif int(mode) == 4:
					return Cot()
				elif int(mode) == 5:
					return Sin_sum_differentiation_two_angles()
				elif int(mode) == 6:
					return Cos_sum_differentiation_two_angles()
				elif int(mode) == 7:
					return Tan_sum_differentiation_two_angles()
				else:
					return 'not defined\n:::::'
			except ValueError:
				return 'Please enter number !\n::::::'
			except KeyboardInterrupt:
				return 'You select exit!\n::::::'


		# Calculation Log
		def Logarithm():
			try:
				def solve_log():
					print('\n:::::: Solve Logarithm ::::::\n')
					x = int(input('Enter the logarithm input: '))
					base = int(input('Enter the logarithm base: '))
					if x>0 and base>0 and base != 0:
						return f'Log({x}, {base}): {log(x,base)}'
					else:
						return 'Log not defined (x<0 or base<0 or base=0)!\n::::::'

				def Sum_differentiation_log():
					print('\n:::::: Sum and differentiation Logarithm ::::::\n')
					x1 = int(input('Enter the "first" logarithm input: '))
					base1 = int(input('Enter the "first" logarithm base: '))

					x2 = int(input('Enter the "second" logarithm input: '))
					base2 = int(input('Enter the "second" logarithm base: '))

					if x1>0 and base1>0 and base1 != 0 and x2>0 and base2>0 and base2 != 0:
						return f'log({x1},{base1}) + log({x2}, {base2}) = {log(x1,base1) + log(x2,base2)}\nlog({x1},{base1}) - log({x2}, {base2}) = {log(x1,base1) - log(x2,base2)}\n::::::::'
					else:
						return 'Log not defined (x<0 or base<0 or base=0)!\n::::::'


				def Multiplication_division_logarithms():
					print('\n:::::: Sum and differentiation Logarithm ::::::\n')
					x1 = int(input('Enter the "first" logarithm input: '))
					base1 = int(input('Enter the "first" logarithm base: '))

					x2 = int(input('Enter the "second" logarithm input: '))
					base2 = int(input('Enter the "second" logarithm base: '))

					if x1>0 and base1>0 and base1 != 0 and x2>0 and base2>0 and base2 != 0:
						return f'log({x1},{base1}) * log({x2}, {base2}) = {log(x1,base1) * log(x2,base2)}\nlog({x1},{base1}) / log({x2}, {base2}) = {log(x1,base1) / log(x2,base2)}\n::::::::'
					else:
						return 'Log not defined (x<0 or base<0 or base=0)!\n::::::'

				mode = input('What do yo want do:\n1-Solve log\n2-Sum and differentiation log\n3-Multiplication and division logarithms\nENTER: ')
				if int(mode) == 1:
					print(solve_log())
				elif int(mode) == 2:
					print(Sum_differentiation_log())
				elif int(mode)== 3:
					print(Multiplication_division_logarithms())
				else:
					print('\nNotdefined\n::::::')



			except ValueError:
				return 'Please enter number !\n::::::'
			except KeyboardInterrupt:
				return 'You select exit!\n::::::'



		print('\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n::::::::::::::::: Hello World! Select Operation:  :::::::::::::::::\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
		Select_Operation = input('1-1st degree equation\n2-2nd degree equation\n3-Derivative function\n4-Matrix operation\n5-Calculate the perimeter of shapes\n6-Calculate the area shapes\n7-Calculate the Value of shapes\n8-Calculation of trigonometric ratios\n9-Calculation Log\nENTER: ')

		if Select_Operation == str(1):
			print(One_st_degree_equation())
		elif Select_Operation == str(2):
			print(Second_degree_equation())
		elif Select_Operation == str(3):
			print(Derivative())
		elif Select_Operation == str(4):
			print(Matrix())
		elif Select_Operation == str(5):
			print(Perimeter())
		elif Select_Operation == str(6):
			print(Area())
		elif Select_Operation == str(7):
			print(Volume())
		elif Select_Operation == str(8):
			print(Trigonometric_Ratios())
		elif Select_Operation == str(9):
			print(Logarithm())
		else:



			print('\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n::::::::::::::::: Goodbye your command not defined  :::::::::::::::::\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
	except ValueError:
		print('\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n::::::::::::::::: please enter number :::::::::::::::::\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
	except KeyboardInterrupt:
		print('\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n::::::::::::::::: you select exit :::::::::::::::::\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
	#----------------------------------------------------------------- calcuting ------------------------------------------------------------------------




	#------ cmd color -----
	os.system('pause')
	os.system('color a')
	#------ cmd color -----
