from operator import length_hint

nombre_length=0
str_fila=""
str_ast=""


filas_para_triangulo=int(input("Escribe tu filas_para_triangulo: "))
for fila in range(filas_para_triangulo):
    str_fila=""
    str_ast=""

    while str_fila.__len__()+(fila-2)<0:
        str_fila=str_fila+" "
    #for col in range(fila+2):
    #    str_fila=str_fila+"_"
    for col in range(0,2*fila+1):
        str_ast=str_ast+"*"
    print(str_fila+str_ast)
    #cadena_asterisco
