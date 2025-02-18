# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'jcd_Fruteria.Empleado'
    _description = 'Empleado'
    

    
    name = fields.Char('Nombre', required=True, help='Introduzca el nombre del empleado')
    edad = fields.Integer('Edad', help='Introduzca la edad del empleado')
    genero = fields.Selection([
        ('0', 'Hombre'),
        ('1', 'Mujer')
    ], string='"Género"')
    fechaNacimiento = fields.Date('Fecha de nacimiento',required=True, help='Introduce la fecha de nacimientos')

   
   
