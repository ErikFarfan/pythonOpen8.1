
lista=[
    'primer dato\n',
    'segundo dato\n',
    'tercer dato\n'
]

f=open('archivo.txt','w')
f.writelines(lista)
f.close()

