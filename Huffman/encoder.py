import heapq #heap 
from collections import Counter

def listaFrecuencias(content):
    total = len(content) + 1 
    c = Counter(content) #Nos facilita la agrupación
    res = {}
    for char,count in c.items():
        #Calcula la madre porcentual
        res[char] = float(count)/total
    res['fin'] = 1.0/total #Indica el caracter final (lo pone porque puede epsilon)
    return res, total #Regresa los caracteres y el contenido

#Le paso el diccionario de la frecuencia copmo parametro :v
def makeTree(frecs):
    q = []
    #Pasa la lista por caracter y prioridad en cada item 1
    for ch,pr in frecs.items(): #item
        heapq.heappush(q,(pr,0,ch)) #Lista heapq ordena por frecuencia y profundidad (arbol perfecto)

    while len(q) > 1:  
        e1 = heapq.heappop(q) #Acomoda los elementos en un pila heap de menor a mayor y por profundidad
        e2 = heapq.heappop(q)
        nw_e = (e1[0]+e2[0],max(e1[1],e2[1])+1,[e1,e2]) #Nodo que almacena la suma de estas pilas para cifrarlo
        heapq.heappush(q,nw_e)  #Un push acomodado de modo heap
    return q[0]

def makeEncoder(tree):
    res = {}
    search_stack = []
    search_stack.append(tree+("",)) 
    while len(search_stack) > 0:#Asignando 0 a la rama izquierda y 1 a la derecha
        elm = search_stack.pop()
        if type(elm[2]) == list: #Recorremos el arbol
            prefix = elm[-1]
            search_stack.append(elm[2][1]+(prefix+"0",)) #Aqui esta el cero del de la izquierda 
            search_stack.append(elm[2][0]+(prefix+"1",)) #Aqui esta el 1 de la derecha
            continue #Uno, el otro, tal vez los 2, nunca se sabe
        else:
            res[elm[2]] = elm[-1] #Genera el indice del diccionario (llave, valor)
        pass
    return res #Devuelve el diccionario descifrado

def encodeFile(dic,content): #Pide el diccionario y regresa la cadena cifrada
    res = ""
    for ch in content:
        code = dic[ch] #Caracter a buscar
        res = res + code
    res = '1' + res + dic['fin'] #1 al inicio para no perder los ceros, busca en el diccionario el caracter y lo guarda en la cadena
    res = res + (len(res) % 8 * "0") #Bloques de multiplos de 8 bits porque binario salu2
    return int(res,2) #Regresamos el numero binario (la wea, la base)

    