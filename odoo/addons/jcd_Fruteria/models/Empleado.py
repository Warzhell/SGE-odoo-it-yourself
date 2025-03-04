from odoo import models, fields

class Empleado(models.Model):
    _name = 'jcd_fruteria.empleado'
    _description = 'Empleado'
    
    name = fields.Char(string='Nombre', required=True, help='Introduzca el nombre del empleado')
    edad = fields.Integer(string='Edad', help='Introduzca la edad del empleado')
    
    # Usamos valores más descriptivos para el género
    genero = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer')
    ], string='Género')
    
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True, help='Introduce la fecha de nacimiento')
    
    # Relación Many2many con el modelo Proveedor
    proveedor_ids = fields.Many2many(
        'jcd_fruteria.proveedor',  # Modelo con el que se establece la relación
        'proveedor_empleado_rel',   # Tabla intermedia (si no existe, Odoo la crea automáticamente)
        'empleado_id',             # Campo que referencia al Empleado en la tabla intermedia
        'proveedor_id',            # Campo que referencia al Proveedor en la tabla intermedia
        string='Proveedores'       # Nombre que aparecerá en la interfaz
    )
