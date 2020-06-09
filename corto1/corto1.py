#Haciendo uso de funciones, deberá determinar la Secuencia Collatz 
#de todos los números naturales, partiendo de 2, hasta llegar a un 
# número equivalente a los últimos 3 dígitos de su carnet. 
#carnet= 201344551, final de rango=551
#
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
            savecollatz.append(int(i))
        else:
            print("%d," % (i), end = "")
            i = (i * 3) + 1
            savecollatz.append(int(i))
        if i == 1:
            print("1")
        savecollatz.append(int(i))
    print(savecollatz)
    
#print(savecollatz)
'''
def fileAppend(fileName = 'collatz.txt'):
    archivo = open(fileName,'a') #Abrir para agregar a archivo existente
    archivo.write('\n\nNuevo evento de append...\n')
    print('Espere, agregando datos al archivo...')
    for i in range(6):
        archivo.write(str(savecollatz)

    archivo.close() #Siempre cerrar el archivo al finalizar la escritura
    print('\n\nAppend finalizado')
'''

