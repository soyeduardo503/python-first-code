#while

CONSTANTE_PI=3.1416
exit_var=0
while(exit_var==0):
   radio=float( input("Ingrese el radio a calcular"))
   area= radio * CONSTANTE_PI
   print(f"El area es {area}")
   exit_var=int(input("Si desea continuar presione 0 sino presione cualquier otro numero"))