from odoo import models, fields
class Cliente(models.Model):
    _name = 'jcd_fruteria.cliente' 
    _description = 'Clientes'
    _rec_name = 'nombre'  
    nombre = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Email')
    nacionalidad_id = fields.Many2one('res.country', string='Nacionalidad')