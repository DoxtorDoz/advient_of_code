

lista = open("input.txt", "r")

f = open("correccion.txt", "w")


reports = 0



def comprobarArchivo(l):
    for x in l:
        comprobarFila(x)
    
    f.write("\n\nReportes totales:" + str(reports))
    print("Reportes: "+str(reports))

def transformar(fila):
    return fila.split()

def escribirCorreccion(fila, conc):
    si = "Safe" if conc else "Unsafe"
    
    if conc:
        global reports
        reports += 1
        f.write(" => ".join([si, fila]))
    
    #f.write(" => ".join([si, fila]))


def comprobarFila(fila):
    valido = True

    numeros = transformar(fila)

    v1 = int(numeros[0])
    v2 = int(numeros[1])

    if comprobarAdyacencia(v1, v2) or v1 != v2:
        i = 0
        if comprobarCreci(v1, v2) :
            while i < len(numeros) -1 :
                a = int(numeros[i])
                b = int(numeros[i + 1])
                
                if  not comprobarAdyacencia(a,b) or not comprobarCreci(a,b) or a == b:
                    valido = False
                    print("INC %s y %s mal" % (str(a),str(b)))
                    break
                print("INC %s y %s bien" % (str(a),str(b)))
                i += 1
        else:
            while i < len(numeros) -1  :
                
                a = int(numeros[i])
                b = int(numeros[i + 1])

                if  not comprobarAdyacencia(b,a) or comprobarCreci(a,b) or a == b:
                    valido = False
                    print("DEC %s y %s mal" % (str(a),str(b)))
                    break
                print("DEC %s y %s bien" % (str(a),str(b)))
                i += 1
    else:
        print("FUERA %s y %s bien" % (str(v1),str(v2)))
        valido = False


        

    escribirCorreccion(fila, valido)

def comprobarCreci(x, y):
 
    return y - x > 0


def comprobarAdyacencia(x, y):
    s = abs(x - y)
   
    return s <= 3 & s >= 1

comprobarArchivo(lista)