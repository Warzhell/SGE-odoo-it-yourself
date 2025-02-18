

from odoo import models, fields, api

class Libro(models.Model):
    _name ='sge_libreria.libro'
    _description ='libro'

    name = fields.Char('Titulo',required=True)
    precio = fields.Float('Precio')
    ejemplares = fields.Integer('Ejemplares')
    fecha_compra = fields.Date('Fecha de compra')
    segmano = fields.Boolean('Segunda mano')
    estado = fields.Selection([
    ('1', 'Bueno'),
    ('2', 'Regular'),
    ('3', 'Malo')
], string='Estado', default='1')

    