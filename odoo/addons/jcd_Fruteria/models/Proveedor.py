from odoo import models, fields
class Proveedor(models.Model):
    _name = 'jcd_fruteria.proveedor'  # Corregido guion bajo
    _description = 'Proveedor'
    name = fields.Char(string='Nombre', required=True, help='Introduzca el nombre')
    email = fields.Char(string='Email')
    fruta_id = fields.Char(string='Fruta', required=True, help='Introduce el ID de la fruta')