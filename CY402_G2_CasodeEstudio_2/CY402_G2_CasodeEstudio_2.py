import os
import hashlib

def hasb_sha256(ruta):
    sha256 = hashlib.sha256()
    with open(ruta, "rb") as f: # Abrir el archivo en modo binario
        for bloque in iter(lambda: f.read(4096), b""):
            sha256.update(bloque) # Lee el archivo en bloques de 4096 bytes y actualiza el hash
    return sha256.hexdigest() # Devuelve el hash en formato hexadecimal


directorio = os.getcwd() # ruta del directorio actual


original = os.path.join(directorio, "original.txt") 
archivo_crackeado = os.path.join(directorio, "crackeado.txt") 
# Es necesario crear un archivo txt en la carpeta del script !
print("Directorio actual:", directorio)


if not os.path.exists(original):
    print(f" El archivo ORIGINAL no existe: {original}")
elif not os.path.exists(archivo_crackeado):
    print(f"El archivo CRACKEADO no existe: {archivo_crackeado}")
else:
    # Calcular hashes
    hash1 = hasb_sha256(original)
    hash2 = hasb_sha256(archivo_crackeado)

 
    print("\n Resultados del Analisis:")
    print("Hash archivo original  :", hash1)
    print("Hash archivo crackeado :", hash2)

    if hash1 == hash2:
        print("Archivos idénticos (no modificados)") #si el contenido de los archivos es el mismo. imprime el mensaje
    else:
        print(" Diferencias detectadas (posible alteración del archivo)") #si el contenido de los archivos es diferente. imprime el mensaje
#Para alterar, se modifico el archivo txt crackeado - se le agrego test modificado dentro del arhivo