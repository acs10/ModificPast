import os
lista2=[]
arq1=open("Usuarios_inscritos.csv","+r")
lista=arq1.readlines()
for i in lista:
    lista2.append(i.split(';'))


for r in lista2:
    for ano in os.listdir('relatórios'):
        for mes in os.listdir('relatórios/'+ano):
            if mes:
                for nome in os.listdir('relatórios/'+ano+'/'+mes):
                    if nome:
                        if nome == r[0]:
                            os.rename('relatórios/'+ano+'/'+mes+'/'+nome,'relatórios/'+ano+'/'+mes+'/'+r[3]+' '+r[4])
                            print("OK")
                            break
                        
                        else:
                            print("Não somos iguais:"+nome+"!="+r[0])
                    else:
                        print("Não existe N/D Ake!")
                        break
                else:
                    break
            

    



