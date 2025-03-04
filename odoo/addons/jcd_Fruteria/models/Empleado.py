from odoo import models, fields

class Empleado(models.Model):
    _name = 'jcd_fruteria.empleado'
    _description = 'Empleado'
    
    name = fields.Char(string='Nombre', required=True, help='Introduzca el nombre del empleado')
    edad = fields.Integer(string='Edad', help='Introduzca la edad del empleado')
    
 
    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer')
    ], string='Género')
    
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True, help='Introduce la fecha de nacimiento')
    
  
    proveedor_ids = fields.Many2many(
        'jcd_fruteria.proveedor', 
        'proveedor_empleado_rel',   
        'empleado_id',             
        'proveedor_id',            
        string='Proveedores'      
    )
