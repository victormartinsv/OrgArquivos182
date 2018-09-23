import struct

registroCEP = struct.Struct("72s72s72s72s2s8s2s")

f = open("cep_ordenado_mesclado.dat", "wb")
fin = open('arquivo1.dat', 'r')
fin2 = open('arquivo2.dat', 'r')

coluna = 5

fin.seek(0,2)


max_line = fin.tell() / registroCEP.size

for i in range(0, int(max_line)):
    
    fin.seek(i*registroCEP.size)
    fin2.seek(i*registroCEP.size)
    
    line1 = fin.read(registroCEP.size).encode('latin1')
    line2 = fin2.read(registroCEP.size).encode('latin1')
    
    record1 = registroCEP.unpack(line1)[coluna].decode('latin1')
    record2 = registroCEP.unpack(line2)[coluna].decode('latin1')
    
    if record1<record2:
        
        f.write(line1)
        f.write(line2)
        
    else:
        
        f.write(line2)
        f.write(line1)
        
f.close() 
fin.close()
fin2.close()
