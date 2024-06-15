#Codigo para buscar la CC de la cadena de caracteres
capture="01ICCOLO01121047415001<<<<<<<<<< 9210181M3110278COL1030432234<2PEPITO<PEREZ<<DIOMEDES<DANIEL<<<<"
array_capture = list(capture)
#Busqueda del caracter de inicio
position_l1=capture.find("L")
#print(position_1)
position_l2=capture.find("L",position_l1 + 1)
#print(position_2)
dni_a = position_l2 + 1
#busqueda del caracter final
position_a1=capture.find("<")
#print(position_a1)
position_a2=capture.find("<",position_a1 + 10)
#print(position_a2)
dni_b = position_a2
#imprimo el rango del caracter inicial y caracter final
dni_dio=array_capture[dni_a:dni_b]
el_dni_de_diomedes=''.join(dni_dio)
print(el_dni_de_diomedes)
###### Esta podria ser otra forma sin buscar el otro "caracter antes del DNI y teniendo cuenta la longitud del DNI"####
#En esta linea tengo en cuenta que el tamaño de la CC es de 10 digitos.
#dni_b= dni_a + 10
#dni_diomedes_a=array_capture[dni_a:dni_b]
#el_dni_de_diomedes=''.join(dni_diomedes_a)
#print(el_dni_de_diomedes)
