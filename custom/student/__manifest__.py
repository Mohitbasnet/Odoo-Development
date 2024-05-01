# -*- coding: utf-8 -*-
{
    'name': "student",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mohit basnet",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
      'data/wb.student.csv',
        'data/record_data.xml',
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'wizard/set_school_wiz.xml'
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
     "assets": {
        "web.assets_backend": [
            "student/static/src/xml/list_controller.xml",
            "student/static/src/js/list_controller.js"
        ]
}
}
