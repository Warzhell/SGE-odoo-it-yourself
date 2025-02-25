# -*- coding: utf-8 -*-
{
    'name': "Fruteria",

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

    'category': 'Sales',
    'version': '17.0.0.1',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/Cliente.xml',
        'views/Fruta.xml',
        'views/Empleado.xml',
        'views/Proveedor.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}

