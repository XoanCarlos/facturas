# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    print("Hello World")

import gi
import conexion
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class facturas:
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('ventana.glade')
        self.ventana = b.get_object('ventana')
        self.entdni = b.get_object('entdni')
        self.entnome = b.get_object('entnome')
        self.entapel = b.get_object('entapel')
        self.entdire = b.get_object('entdir')
        self.entloc = b.get_object('entloc')
        self.enttel = b.get_object('enttel')
        self.entmail = b.get_object('entmail')
        self.entprod = b.get_object('entpro')
        self.entprecio = b.get_object('entprecio')
        self.entstock = b.get_object('entstock')
        
        self.listclient = b.get_object('listcliente')
        self.listprod = b.get_object('listproductos')
        
        dic= {'on_ventana_destroy': self.salir,'on_btnSalir_clicked': self.salir,
        'on_btnalta_clicked': self.insertc, 'on_btnsalirp_clicked': self.salir,
        'on_btnaltap_clicked': self.insertp,'on_notebook1_select_page': self.cargap,        
        }
    
        
        b.connect_signals(dic)
        self.ventana.show_all()
        self.listarc()
        # self.listarp()
        
    def salir(self, widget):
        Gtk.main_quit()
        
    def insertc(self,widget):
        self.dni = self.entdni.get_text()
        self.nome = self.entnome.get_text()
        self.apel = self.entapel.get_text()
        self.dire = self.entdire.get_text()
        self.loc = self.entloc.get_text()
        self.tel = self.enttel.get_text()
        self.mail = self.entmail.get_text()
    
        registro = (self.dni, self.nome, self.apel, self.dire, self.loc, self.tel, self.mail)
        
        if self.dni != '' or self.apel !='':
            if conexion.insertarc(registro):
                self.limpiarc()
                self.listclient.clear()
                self.listarc()
            else:
                print 'error en alta clientes'
                
    
    def limpiarc(self):
        self.entdni.set_text('')
        self.entnome.set_text('')
        self.entapel.set_text('')
        self.entdire.set_text('')
        self.entloc.set_text('')
        self.enttel.set_text('')
        self.entmail.set_text('')
    
    
    def listarc(self):
        lista = conexion.listac()
        for registro in lista:
            self.listclient.append(registro)
        
    #trabajamos con el producto
    
    def insertp(self, widget):
        self.prod = self.entprod.get_text()
        self.precio = self.entprecio.get_text()
        self.stock = self.entstock.get_text()
        registro = (self.prod, self.precio, self.stock)
        
        if self.prod != '' or self.precio !='':
            if conexion.insertarp(registro):
                self.limpiarp()
                self.listprod.clear()
                self.listarp()
            else:
                print 'error alta producto'
    
    def cargap(self):
        self.listarp()
                
    
    def limpiarp(self):
        self.entprod.set_text('')
        self.entprecio.set_text('')
        self.entstock.set_text('')
    
    def listarp(self):
        lista = conexion.listap()
        for registro in lista:
            self.listprod.append(registro)
    
if __name__  ==  '__main__':
    main = facturas()
    Gtk.main()