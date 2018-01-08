# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    print("Hello World")

import gi
# import conexion
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class facturas:
    def __init__(self):
        b = Gtk.Builder()
        b.add_from_file('ventana.glade')
        self.ventana = b.get_object('ventana')
        
        dic= {'on_ventana_destroy': self.salir,
        }
    
        
        b.connect_signals(dic)
        self.ventana.show_all()
        
    def salir(self, widget):
        Gtk.main_quit()
    
        
if __name__  ==  '__main__':
    main = facturas()
    Gtk.main()