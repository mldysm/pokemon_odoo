# -*- coding: utf-8 -*-
{
    'name': "Pokemon List",

    'summary': "Manage Pokémon in Odoo",

    'description': """
Long description of the module's purpose.
    """,

    'author': "Your Company",
    'website': "https://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'installable': True,
    'application': True,
    'sequence':'1',

    'depends': ['base', 'contacts'],

    'data': [
        'views/pokemon.xml',
        'views/res_partner.xml',
        'security/ir.model.access.csv',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'images': [
        'static/description/icon.png',
    ],
}
