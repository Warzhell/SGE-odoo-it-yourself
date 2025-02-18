from odoo import models, fields, api

class Proveedor(models.Model):
    _name = 'jcd_Fruteria.Proveedor'
    _description = 'Proveedor'
    
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre ')
    edad = fields.Integer('Edad', help='Introduzca la edad ')
    fruta = fields.Char('Fruta', required=True, help='Introduce el nombre de la fruta')
    
    