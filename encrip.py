#! /usr/bin/python
#####encriptar un archivo por el metodo de encriptacion DES


from pyDes import des

def encriptaFichero():
    
    fichero="archivo.txt"#archivo a encriptar
    user_pass="micontra"#contrasena 8 caracteres (8bytes)

    f = open(fichero, 'rb+')
    d = f.read()
    f.close()

    k = des(user_pass)


    d = k.encrypt(d, ' ')
    f = open(fichero, 'wb+')
    f.write(d)
    f.close()
    print  "se realizo con exito"
    return True

def desencriptaFichero():
    
    fichero="archivo.txt"#fichero a desencriptar
    user_pass="micontra"#contrasena 8 caracteres (8bytes)

    f = open(fichero, 'rb+')
    d = f.read()
    f.close()


    k = des(user_pass)

    d = k.decrypt(d, ' ')
    f = open(fichero, 'wb+')
    f.write(d)
    f.close()
    print "archivo "+fichero+" desencriptado"
    return True




