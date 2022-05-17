import sys
import pickle #Libreria de bytes
import json #Diccionario
from tkinter import * #Interfaz
from tkinter import filedialog as fd #La wea que abre
import encoder as enc
import decoder as dec


def guardarCom(compressed,dic):
    # Lo guardamos en un archivo
    filename = fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("all files","*.*")))
    fileOut = open(filename+".bin", "wb")
    pickle.dump(compressed,fileOut)
    fileOut.close()
    # Guardamos el diccionario en otro archivo
    outf = open(filename+"_d3c0d3r.dic",'w')
    json.dump(dic,outf)
    outf.close()

def guardarDes(descompressed):
    # Lo guardamos en un archivo
    filename = fd.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("all files","*.*")))
    fileOut = open(filename+".txt", "w")
    fileOut.write(descompressed)
    fileOut.close()

def printFrec(frecuencias, total):
    for i in frecuencias.keys():
        cad = ""
        cad+= i +" -> "+ str(frecuencias[i]*total) + " | " + str(frecuencias[i]*100) + "%"
        print(cad)
#Contando las frecuencias y generando el diccionario
def compressFile():
    filename = fd.askopenfilename(initialdir="/", 
        title="Seleccione el Archivo", 
        filetypes = (("txt files","*.txt"),("all files","*.*"))) 
    fileIn = open(filename, "r")
    contenido = fileIn.read()
    fileIn.close()
    frecuencias, total = enc.listaFrecuencias(contenido)
    printFrec(frecuencias, total)    
    arbol = enc.makeTree(frecuencias)
    diccionario = enc.makeEncoder(arbol)
    cifrado = enc.encodeFile(diccionario, contenido)
    print("\n Archivo comprimido")
    guardarCom(cifrado, diccionario)

def binaryFile():
    filename = fd.askopenfilename(initialdir = "/",
        title = "Seleccione archivo a descomprimir",
        filetypes = (("bin files","*.bin"),("all files","*.*")))
    fileIn = open(filename, "rb")
    print(pickle.load(fileIn)) #Carga el archivo
    fileIn.close()

def showCompressed():
    filename = fd.askopenfilename(initialdir = "/",
        title = "Seleccione archivo a descomprimir",
        filetypes = (("bin files","*.bin"),("all files","*.*")))
    fileIn = open(filename, "rb")
    print(fileIn.read())
    fileIn.close()

def decompress():
    filename = fd.askopenfilename(initialdir = "/",
        title = "Seleccione archivo a descomprimir",
        filetypes = (("bin files","*.bin"),("all files","*.*")))
    encFile = open(filename, "rb")
    cifrado = pickle.load(encFile)
    encFile.close()
    fin = len(filename) - 4 #Le quito el .bin (4 caracteres)
    savedDic = open(filename[0:fin]+"_d3c0d3r.dic", "r")
    dic = json.load(savedDic)
    dictDecoder = {}
    for i,e in dic.items(): dictDecoder[e] = i #dic.item genera la llave y el valor porque se me olvida
    savedDic.close()
    print(cifrado)
    print(dictDecoder)
    descifrado = dec.descifra(dictDecoder,cifrado)
    print("Archivo descomprimido")
    guardarDes(descifrado)

def salirXD():
    sys.exit(1)

def fatal_error():
    print("\n\n3312! TENEMOS UN 3312! Opcion no valida\n\n")

def main():

    while(True):
        print("***********************Compresor de archivos Huffman***********************")
        print(" 1. Comprimir el archivo y mostrar tabla de frecuencias" )
        print(" 2. Mostrar archivo binario" )
        print(" 3. Mostrar archivo comprimido" )
        print(" 4. Descomprimir archivo y mostrar" )
        print(" 5. Salir" )
        choose = int(input(" Selecciona una opcion: "))
        print(choose)
        menu = {
            1: compressFile,
            2: binaryFile,
            3: showCompressed,
            4: decompress,
            5: salirXD
        }
        menu.get(choose, fatal_error)()

if __name__ == "__main__":
    main()