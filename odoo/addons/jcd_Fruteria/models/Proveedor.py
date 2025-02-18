from odoo import models, fields, api

class Proveedor(models.Model):
    _name = 'jcd_Fruteria.Proveedor'
    _description = 'Proveedor'
    
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre ')
    email = fields.Char(string ='Email')
    fruta_id = fields.Char('Fruta', required=True, help='Introduce el ID de la fruta')
    
    