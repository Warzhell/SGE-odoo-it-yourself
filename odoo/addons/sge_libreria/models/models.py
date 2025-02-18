from odoo import models , fields

class Cliente(models.Model):
    _name ='model.clientes'
    _description = 'Clientes'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre',required=True)
    email = fields.Char(string ='Email')
    posicion = fields.Char(string= 'Posicion')
    tipo_cliente = fields.Many2one(
        'model.categorias',
        string ='Tipo de cliente'
    )