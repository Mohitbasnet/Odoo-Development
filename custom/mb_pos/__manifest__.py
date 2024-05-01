# -*- coding: utf-8 -*-
{
    'name': "Mohit Point of Sale",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohit Basnet",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
    ],
    'assets':{
        'point_of_sale.assets':[
            "mb_pos/static/src/js/mb_sample_button.js",
            "mb_pos/static/src/js/clearall_button.js",
            "mb_pos/static/src/xml/mb_button.xml",
            "mb_pos/static/src/xml/clearall_button.xml"
        ]
    }
  
}
