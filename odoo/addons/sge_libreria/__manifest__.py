# -*- coding: utf-8 -*-
{
    'name': "sge_libreria",
    'summary': "Fruteria",
    'description': """
Programa para una fruteria 
    """,
    'author': "Jorge Cuevas Delgado",
    'category': 'Uncategorizhed',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
