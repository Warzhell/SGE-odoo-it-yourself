# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Categoria(models.Model):
    _name = 'sge_libreria.categoria'#jcd_juego.nombre 
    _description = 'Categoria'

    name = fields.Char('Categoria',required=True,help='Introduzca nombre de categoria')
    description = fields.Char('Categoria')

