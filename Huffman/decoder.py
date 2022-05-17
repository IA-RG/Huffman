def descifra(dic, encoded): #diccionario para decifrar y los caracteres
    res = [] #Lista
    length = encoded.bit_length() - 1 #Verifica que sea un archivo admisible
    if encoded >> length != 1: #El archivo tiene que tener al menos un elemento o c muere
        raise Error("Corrupt file!")
    done = False
    while length > 0 and not done:
        shift = length - 1 #Fin del archivo
        while True:
            num = encoded >> shift #En la posicion shift
            bitnum = bin(num)[3:] #Convierte a binario el numero que recorre hasta la posicion shift e inicia el descifrado
            if bitnum not in dic: #Aqui se la fumo y le metio ingenieria inversa :v
                shift -= 1 
                continue
            char = dic[bitnum] #Obtiene el caracteer
            if char == 'fin': 
                done = True
                break
            res.append(char) #Lista con la respuesta
            encoded = encoded - ((num - 1) << shift) #Quitamos los elementos del archivo codificado
            length = shift 
    return ''.join(res) # lo hace cadena
