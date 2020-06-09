#Haciendo uso de funciones, deberá determinar la Secuencia Collatz 
#de todos los números naturales, partiendo de 2, hasta llegar a un 
# número equivalente a los últimos 3 dígitos de su carnet. 
#carnet= 201344551, final de rango=551
#
'''
numero = int(input("Ingresa un numero: "))

while numero != 1:
    if numero % 2 == 0:
        print("%d," % (numero), end = "")
        numero = numero / 2
    else:
        print("%d," % (numero), end = "")
        numero = (numero * 3) + 1

    if numero == 1:
        print("1")
'''

fin_carnet=551
fin=fin_carnet+1
savecollatz=[]

for i in range(2,6):
    del savecollatz[:]
    while i != 1:
        savecollatz.append(int(i))
        if i % 2 == 0:
            print("%d," % (i), end = "")
            i = i / 2
            #savecollatz.append(int(i))
        else:
            print("%d," % (i), end = "")
            i = (i * 3) + 1
            #savecollatz.append(int(i))
        if i == 1:
            print("1")
        savecollatz.append(int(i))

print(savecollatz)
    
