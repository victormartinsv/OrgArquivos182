import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")

f = open("cep_ordenado.dat", "rb")
fout = open('arquivo1.dat', 'wb')
fout2 = open('arquivo2.dat', 'wb')

f.seek(0,2)

for i in range(0, 500000):
    
    f.seek(i*registroCEP.size)    
    line = f.read(registroCEP.size)
    
    if i%2==0:

        fout.write(line)        

    if i%2!=0:

        fout2.write(line)
f.close()
fout.close()
fout2.close()
