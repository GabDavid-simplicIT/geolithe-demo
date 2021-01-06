# -*- coding: utf-8 -*-
{
    'name': "SIT - Roles list",

    'summary': """
        Module that links projects, tasks templates with roles""",

    'description': """
    Module that links projects, tasks templates with roles
    """,

    'author': "SimplicIT",
    'website': "https://www.simplicit.pro",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['task_template', 'planning'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/task_template_views.xml',
        'views/project_task_views.xml',
        'wizard/create_role.xml'
    ],
}
