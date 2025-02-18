# -*- coding: utf-8 -*-
{
    'name': "Librería",

    'summary': "Módulo de ejemplo de Sistemas de Gestión Empresarial",

    'description': """
Descripción larga<br/>
Se puede leer yendo a Inicio > Aplicaciones<br/>
Quitando el filtro Aplicaciones y buscando sge<br/>
Entrando a Más información sobre sge_libreria este nombre técnico
viene dado por el nombre del directorio cuando lo creamos con odoo scaffold
    """,

    'author': "Jorge Cuevas Delgado",
    'website': "https://aulavirtual33.educa.madrid.org/ies.elcanaveral.mostoles/course/view.php?id=347",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/menu.xml',
        'views/Cliente.xml',
        'views/Fruta.xml',
        'views/Empleado.xml',
        'views/Proveedor.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}


#{
#    'name': "jcd_Fruteria",
#    'summary': "Fruteria",
#    'description': """
#Programa para una fruteria 
#    """,
#    'author': "Jorge Cuevas Delgado",
#    'category': 'Uncategorizhed',
#    'version': '0.1',
#    'depends': ['base'],
#    'data': [
#        'security/ir.model.access.csv',
#        'views/views.xml',
#        'views/templates.xml',
#    ],
#    'demo': [
#        'demo/demo.xml',
#    ],
#    'installable': True,
#    'application': True,
#}
