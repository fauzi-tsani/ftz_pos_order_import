# -*- coding: utf-8 -*-
{
    'name': "ftz_pos_order_import",

    'description': """
    """,

    'author': "Fauzi Tsani Zharfan - PT. Walden Global Service",
    'website': "https://www.wgs.co.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        'views/pos_order_import.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}