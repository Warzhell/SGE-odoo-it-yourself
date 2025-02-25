from odoo import models, fields
class Empleado(models.Model):
    _name = 'jcd_fruteria.empleado'  # Corregido guion bajo
    _description = 'Empleado'
    name = fields.Char(string='Nombre', required=True, help='Introduzca el nombre del empleado')
    edad = fields.Integer(string='Edad', help='Introduzca la edad del empleado')
    genero = fields.Selection([
        ('0', 'Hombre'),
        ('1', 'Mujer')
    ], string='Género')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True, help='Introduce la fecha de nacimiento')