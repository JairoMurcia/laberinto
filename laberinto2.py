class Nodo:
        def __init__(self, valor, hijos = []):
            self.valor = valor
            self.hijos = hijos

def hallar_x(matriz,iteracion=0):
	if 'x' in matriz[0]:
		return [iteracion,matriz[0].index('x')]
	return hallar_x(matriz[1:],iteracion+1)	 

          


def generar_arbol(m,x,y,a=[]):
    try:
        if m[x][y]=='0' and [x,y] not in a:
            return Nodo(m[x][y],[generar_arbol(m,x+1,y,a+[[x,y]])]+[generar_arbol(m,x-1,y,a+[[x,y]])]+[generar_arbol(m,x,y+1,a+[[x,y]])]+[generar_arbol(m,x,y-1,a+[[x,y]])])
        elif m[x][y]=='y':
            return Nodo('y')
	return None
    except IndexError:    
        return None

def buscar(arbol, valor):
            if arbol == None:
                    return False
            elif arbol.valor == valor:
                    return True
            else:
                    return buscar_Hijos(arbol.hijos, valor)

def buscar_Hijos(lista, valor):
            if lista == []:
                    return False
            else:
                    return buscar(lista[0], valor) or buscar_Hijos(lista[1:], valor)


m=[x.split() for x in open('laberinto.txt').readlines()]

i=hallar_x(m)
x,y=i

c=generar_arbol(m,x,y)

print(buscar(c,'y'))
