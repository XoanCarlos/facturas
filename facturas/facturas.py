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
        self.dni = b.get_object('entdni')
        self.nome = b.get_object('entnome')
        self.apel = b.get_object('entapel')
        self.dir = b.get_object('entdir')
        self.loc = b.get_object('entloc')
        self.tel = b.get_object('enttel')
        self.mail = b.get_object('entmail')
        dic= {'on_ventana_destroy': self.salir,'on_btnSalir_clicked': self.salir,
        'on_btnalta_clicked': self.insertc, 'on_btnsalirp_clicked': self.salir,
        
        
        }
    
        
        b.connect_signals(dic)
        self.ventana.show_all()
        
    def salir(self, widget):
        Gtk.main_quit()
        
    def insertc(self,widget):
        self.dni = self.dni.get_text()
        self.nome = self.nome.get_text()
        self.apel = self.apel.get_text()
        self.dir = self.dir.get_text()
        self.loc = self.loc.get_text()
        self.tel = self.tel.get_text()
        self.mail = self.mail.get_text()
        registro = (self.dni, self.nome, self.apel, self.dir, self.loc, self.tel, self.mail)
        
        if self.dni != '' or self.apel !='':
            conexion.insertarc(registro)
        
        
if __name__  ==  '__main__':
    main = facturas()
    Gtk.main()