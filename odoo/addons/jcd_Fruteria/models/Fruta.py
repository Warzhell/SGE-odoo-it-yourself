

from odoo import models, fields, api

class Fruta(models.Model):
    _name ='jcd_Fruteria.fruta'
    _description ='fruta'

    fruta_id = fields.Char('ID',required=True)
    name = fields.Char('Nombre',required=True)
    precio = fields.Float('Precio €/KG')
    cantidad = fields.Float('Cantidad(KG)')
    estado = fields.Selection([
    ('1', 'Bueno'),
    ('2', 'Regular'),
    ('3', 'Malo')
], string='Estado', default='1')

    