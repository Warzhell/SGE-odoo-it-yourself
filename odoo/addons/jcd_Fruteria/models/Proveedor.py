from odoo import models, fields

class Proveedor(models.Model):
    _name = 'jcd_fruteria.proveedor'
    _description = 'Proveedor'

    name = fields.Char(string='Nombre', required=True, help='Introduzca el nombre')
    email = fields.Char(string='Email')

 
    fruta_ids = fields.One2many('jcd_fruteria.fruta', 'proveedor_id', string='Frutas')

    
    empleado_ids = fields.Many2many(
        'jcd_fruteria.empleado', 
        'proveedor_empleado_rel', 
        'proveedor_id', 
        'empleado_id', 
        string='Empleados'
    )
