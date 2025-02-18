# -*- coding: utf-8 -*-
# from odoo import http


# class JcdFruteria(http.Controller):
#     @http.route('/jcd__fruteria/jcd__fruteria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jcd__fruteria/jcd__fruteria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jcd__fruteria.listing', {
#             'root': '/jcd__fruteria/jcd__fruteria',
#             'objects': http.request.env['jcd__fruteria.jcd__fruteria'].search([]),
#         })

#     @http.route('/jcd__fruteria/jcd__fruteria/objects/<model("jcd__fruteria.jcd__fruteria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jcd__fruteria.object', {
#             'object': obj
#         })

