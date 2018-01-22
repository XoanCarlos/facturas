# -*- coding: utf-8 -*-
from fpdf import FPDF
import os

import conexion

class PDF(FPDF):
    def header(self):
        self.image('factura.png', 15, 8, 20)
        self.set_font('Arial', 'B', 12)
        self.cell(80)
        titulo = "FRUTAS VIGO, S.L"
        self.cell(60, 5, titulo, 1, 1, 'C')
        self.ln(10)
        self.set_font('Arial', 'I', 10)
        titulo2 = "El sabor amigo"
        self.cell(60, 5, titulo2, 0, 1, 'L')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'UI', 8)
        self.cell(0, 6, "NIF: B0000000", 0, 0, 'C')
        
        
def getFactura(factura, cliente):
    pdf = PDF('P', 'mm', 'A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial','B', 12)
    #nomCli, apeCli, dirCli, locCli, telCli, emailCli = conexion.datosCliente(cliente)
    pdf.cell(0,8,"Factura : " + str(factura), 0, 1, 'C')
    detallesVenta = conexion.listav(factura)
    detallesCliente = conexion.listacf(cliente)
    for row in detallesCliente:
        pdf.cell(0,8, "DATOS CLIENTE", 0, 1, 'R')
        pdf.cell(0,8,"DNI/CIF : " + str(row[0]), 0,1,'R')
        pdf.cell(0,8, "Nombre: " + str(row[2]) + "  " +  str(row[1]), 0,1,'R')
        pdf.cell(0,8,"Direccion : " + str(row[3]) + "     Localidad: " + row[4], 0,1,'R')
        pdf.cell(0,8,"Telefono : " + str(row[5]) + "    Mail:" + row[6], 0,1,'R')

    cabecera = "Producto                     Cantidad                     Precio Unitario                 Precio Total"
    pdf.cell(0,40, cabecera , 0, 1, 'C')
    pdf.line(164, 50, 200, 50)
    pdf.line(20, 100, 190, 100)
    pdf.line(20, 106, 190, 106)
    suma = 0
    iva = 0.21
    cuotaIVA = 0
    total = 0
    x = 10
    y = 110
    for item in detallesVenta:
        
        pdf.set_font('Arial','', 10)
        #texto = texto + conexion.nombreProducto(str(item[2]))
        prodnom = conexion.verprod(str(item[2]))
        cantidad = "{0:.2f}".format(float(item[3]))
        precio = float(item[4])
        subtotalv = float(item[3]) * float(item[4])
        x= 20
        pdf.text(x,y, "  |  " + str(prodnom[0]))
        x = x + 50
        pdf.text(x,y, "  |  " + str(cantidad))
        x = x + 40
        pdf.text(x,y, "  |  " + str(precio))
        x = x + 55
        pdf.text(x,y, "  |  " + str(subtotalv))
        x = x + 15
        pdf.text(x,y, "  |  " )
        y = y + 5
        #texto = texto + '\n'
        suma = suma + subtotalv
        
      
    iva = suma * 0.21
    total = iva + suma
    suma = "{0:.2f}".format(suma)  
    iva = "{0:.2f}".format(iva)
    total = "{0:.2f}".format(total)
    pdf.ln(70)
    pdf.set_font('Arial','B', 10)
    lineatotal = "Suma de conceptos                 IVA %                Cuota IVA                   Importe Total"
    pdf.cell(0, 7, lineatotal, 1, 1, 'C')
    pdf.text (115,210,str(iva) + " Euros")
    pdf.text(155,210, str(total) + " Euros" )
    
 
    archivo = 'dos.pdf'

    pdf.output(archivo, 'F')

    os.system("evince " + archivo)
