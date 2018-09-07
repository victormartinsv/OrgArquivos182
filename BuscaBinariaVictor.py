import struct

cep = input("Digite um CEP para iniciar a busca: ")

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
coluna = 5
f = open("cep_ordenado.dat", "r")

esq = 0
f.seek(0,2)

dir = f.tell() / registroCEP.size

itercount = 0

while esq <= dir:
	    
    itercount = itercount + 1
    valorMeio = int(esq + ((dir - esq) / 2))
    f.seek(valorMeio * registroCEP.size)
    line = f.read(registroCEP.size).encode('latin1')
    record = registroCEP.unpack(line)
    if int(record[coluna]) == int(cep):
        for i in range(0, len(record) - 1):
            print(record[i].decode('latin1'))
        break
    elif int(record[coluna]) < int(cep):
        esq = valorMeio + 1
    elif int(record[coluna]) > int(cep):
        dir = valorMeio - 1

print("Número de iteracoes: " + str(itercount))

if esq > dir:
	print("Cep nao encontrado")
