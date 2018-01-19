# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# -*- coding: utf-8 -*-

import os
import gi
import conexion
import time
import imprfact
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
        self.entdnifac = b.get_object('entdnifac')
        self.entventa = b.get_object('entventa')
         
        self.lblfac = b.get_object('lblfac')
        self.lblprecio = b.get_object('lblprecio')
        
        self.cmbproducto = b.get_object('cmbproducto')
        
        self.treeclientes = b.get_object('treeclientes')
        self.treefac =b.get_object("treefac")
        
        self.listclient = b.get_object('listcliente')
        self.listprod = b.get_object('listproductos')
        self.listfact = b.get_object('listfact')
        self.listventa = b.get_object('listventa')
        self.listprodcmb = b.get_object('listprodcmb')
    
        
        dic= {'on_ventana_destroy': self.salir,'on_btnSalir_clicked': self.salir,
        'on_btnalta_clicked': self.insertc, 'on_btnsalirp_clicked': self.salir,
        'on_btnaltap_clicked': self.insertp,'on_notebook1_select_page': self.cargap,
        "on_treeclientes_cursor_changed": self.cargarcli, 'on_entfact_clicked': self.altafac,
        "on_entanulfac_clicked": self.bajafac, "on_treefac_cursor_changed": self.cargarfac,
        "on_btnventa_clicked": self.venta, "on_cmbproducto_changed": self.cargaprecio,
        "on_btnfac_clicked": self.impfac,
        
        }
    
        b.connect_signals(dic)
        self.ventana.show_all()
        self.listarc()
        self.listarp()
        self.listarfac()
        self.cargarcmb()
        
        
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
        
    def cargarcli(self, widget):
        model, iter = self.treeclientes.get_selection().get_selected()
#        model es el modelo de la tabla de dato, iter ese un numero que 
#        identifica que registro es
        
        if iter != None:
            sdni = model.get_value(iter, 0)
            lista = conexion.listacf(sdni)
            for registro in lista:
                self.entdni.set_text(registro[0])
                self.entnome.set_text(registro[1])
                self.entapel.set_text(registro[2])
                self.entdire.set_text(registro[3])
                self.entloc.set_text(registro[4])
                self.enttel.set_text(registro[5])
                self.entmail.set_text(registro[6])
            
                self.entdnifac.set_text(sdni)    
    
    
    #trabajamos con el producto
    
    def insertp(self, widget):
        self.prod = self.entprod.get_text()
        self.precio = float(self.entprecio.get_text())
        #self.precio = '{0:.2f}'.format(self.precio)
        self.stock = float(self.entstock.get_text())
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
            item0 = int(registro[0])
            item1 = str(registro[1])
            item2 = float(registro[2])
            item3 = float(registro[3])
            
            registro = [item0, item1, item2, item3]
            self.listprod.append(registro)
  
  # trabajamos con facturas
    def altafac (self, widget):
        self.fecha = time.strftime("%d/%m/%y")
        self.dnicli = self.entdnifac.get_text()
        registro = (self.fecha, self.dnicli)
        
        if self.dnicli != '':
            codigo = conexion.insertarfac(registro)
            self.lblfac.set_text(str(codigo[0]))
            self.listfact.clear()
            self.listarfac()
            self.facidv = self.lblfac.get_text()
            self.facnumv = self.lblfac.get_text()
            
            #registrov = [int(self.facnumv), int(self.facnumv), int(self.facnumv), float(self.facnumv), float(self.facnumv)]
            #self.listfact.append(registrov)
            
        else:
            print('Falta dni')
        
    def listarfac(self):
        lista = conexion.listafac()
        for registro in lista:
            item0 = int(registro[0])
            item1 = str(registro[1])
            item2 = str(registro[2])
            registro = [item0, item1, item2]
            self.listfact.append(registro)
        
    def bajafac(self, widget):
        self.facnumv = self.lblfac.get_text()
        if self.facnumv != "":
            conexion.bajafac(self.facnumv)
            self.listfact.clear()
            self.lblfac.set_text('')
        else:
            print "el campo matricula no puede estar vacio"
        
        self.listarfac()
        
    def cargarfac(self, widget):
        model, iter = self.treefac.get_selection().get_selected()
#        model es el modelo de la tabla de dato, iter ese un numero que 
#        identifica que registro es
        
        if iter != None:
            self.facnumv = model.get_value(iter, 0)
            sdni = model.get_value(iter, 2)
            
            self.lblfac.set_text(str(self.facnumv))
            self.facnumv = self.lblfac.get_text()
            self.entdnifac.set_text(sdni)
            self.listventa.clear()
            self.listarventa()
            
            
## EMPEZAMOS CON LAS VENTAS

    def venta(self,widget):
        self.facnumv = self.lblfac.get_text()
        self.facdniv = self.entdnifac.get_text()
        self.productov = self.idprod
        self.preciov = self.lblprecio.get_text()
        self.cantidadv = self.entventa.get_text()
        regventa = (self.facnumv,self.productov,self.cantidadv,self.preciov)
        if regventa is not None:
            conexion.grabarventa(regventa)
            self.listventa.clear()
            self.listarventa()
        
    def cargarcmb(self):
        listado = conexion.cargarprod()
        for row in listado:
            self.listprodcmb.append(row)

    def cargaprecio(self, widget):
        index = self.cmbproducto.get_active()
        model = self.cmbproducto.get_model()
        self.idprod = model[index][0]
        
        
        
        listado = conexion.precio(self.idprod)
        for row in listado:
          self.nomprod = row[0]  
          self.lblprecio.set_text(str(row[1]))
       
    def listarventa(self):
        
        listav = conexion.listav(self.facnumv)
        for registro in listav:
            item0 = int(registro[0])
            item1 = int(registro[1])
            item2 = int(registro[2])
            item3 = float(registro[3])
            item4 = float(registro[4])
            registro = [item0, item1, item2, item3, item4]
            self.listventa.append(registro)
    
    # EMPEZAMOS CON LA FACTURA
    
    def impfac(self, widget):
        factura = self.lblfac.get_text()
        cliente = self.entdnifac.get_text()
        imprfact.getFactura(factura, cliente)
        
if __name__  ==  '__main__':
    main = facturas()
    Gtk.main()