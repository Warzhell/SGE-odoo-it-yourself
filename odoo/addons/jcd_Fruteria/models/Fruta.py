from odoo import models, fields

class Fruta(models.Model):
    _name = 'jcd_fruteria.fruta'
    _description = 'Fruta'

    fruta_id = fields.Char('ID', required=True)
    name = fields.Char('Nombre', required=True)
    precio = fields.Float('Precio €/KG')
    cantidad = fields.Float('Cantidad(KG)')
    estado = fields.Selection([
        ('1', 'Bueno'),
        ('2', 'Regular'),
        ('3', 'Malo')
    ], string='Estado', default='1')

    # Campo Many2one que hace la relación con Proveedor
    proveedor_id = fields.Many2one('jcd_fruteria.proveedor', string='Proveedor', help='Proveedor asociado')
    imagen = fields.Image(string='Imagen de la Fruta')
