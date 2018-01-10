# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jcarlos"
__date__ = "$Oct 27, 2017 9:09:03 AM$"

try:
    
    #from Crypto.Cipher import DES
    import sqlite3 
    #import time
      #creamos el cifrador
    #cipher = DES.new('12345678')
    bbdd = 'facturas.sqlite'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    conex.text_factory = str
    print('conexion hecha')
   
except:
    print "Posibles errores de importacion"
    sys.exit(1)
        
        
def insertarc(filac):
    try: 
        cur.execute("insert into cliente(dni,nombre,apellido,direccion,localidad,telefono, mail) values (?,?,?,?,?,?,?)", filac)
        print('insertado')
        conex.commit()
        return True
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()
        
def listac():
    try: 
        cur.execute("select dni,apellido,nombre,telefono from cliente")
        listado = cur.fetchall()
        print('listadocli')
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()
def listacf(dni):
    try: 
        cur.execute("select * from cliente where dni = ?", (dni,))
        listado = cur.fetchall()
        print('listadoclifac')
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()
        
        
def insertarp(filap):
    try: 
        cur.execute("insert into producto(nombre,precio,stock) values(?,?,?)", filap)
        print('insertado')
        conex.commit()
        return True
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()
        
def listap():
    try: 
        cur.execute("select idproducto,nombre, precio, stock from producto")
        listado = cur.fetchall()
        print('listadopro')
        return listado
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()
       
        
def insertarfac(filafac):
    try: 
        cur.execute("insert into factura(idcliente,fecha) values(?,?)", filafac)
        print('insertado')
        conex.commit()
        cur.execute("select numfactura from factura order by numfactura asc limit 1")          
        codigo = cur.fetchone()    
        return codigo
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()
    
    