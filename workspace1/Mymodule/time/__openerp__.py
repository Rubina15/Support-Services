# -*- coding: utf-8 -*-
{
    'name': "Support Tracking",

    'summary': """
       Track service time""",

   'description': """
        Time Tracking Module for Tracking Services:
            - Initialize brought packages
            - Display brought packages
            - View package details
            - Add sessions onto brought packages
    """,


    'author': "Rubina",
    'website': "http://www.ecosoft.co.th",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/timetracking.xml',
        'security/time_security.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}