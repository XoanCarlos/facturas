__author__ = "a12cristiance"
__date__ = "$17-ene-2018 11:19:28$"

from fpdf import FPDF
import os

import conexion

class PDF(FPDF):
    def header(self):
        self.image('factura.png', 10, 8, 33)
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        titulo = "Factura"
        self.cell(30, 5, titulo, 1, 1, 'C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'UI', 8)
        self.cell(0, 6, "Autor : Cristian", 0, 0, 'C')
        
        
def getFactura(factura, cliente):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    #nomCli, apeCli, dirCli, locCli, telCli, emailCli = conexion.datosCliente(cliente)
    detallesFactura = conexion.listav(factura)
    
    pdf.cell(0,9,"Producto  Cantidad  Precio Unitario  Precio Total",0,1,'C')
    suma = 0
    iva = 0.21
    cuotaIVA = 0
    total = 0
    
    texto = ''
    for item in detallesFactura:
        #texto = texto + conexion.nombreProducto(str(item[2]))
        texto = texto + ' ' + str(item[3])
        texto = texto + ' ' + str(item[4])
        precio_total = item[3] * item[4]
        texto = texto + ' ' + str(precio_total)
        texto = texto + '\n'
        suma = suma + precio_total
        
    
    
    print("\n\nSuma de conceptos   IVA %    Cuota IVA    Importe Total")
    
    cuotaIVA = suma * iva
    total = suma + cuotaIVA
    
    print(str(suma) + '\t' + "21,00" + '\t' +  str(cuotaIVA)+ '\t' + str(total))
    
    pdf = PDF('P', 'mm', 'A4')

    pdf.alias_nb_pages()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)

   

    pdf.cell(180, 220, texto, 1, 2, 'C')

    archivo = 'dos.pdf'

    pdf.output(archivo, 'F')

    os.system("evince " + archivo)
