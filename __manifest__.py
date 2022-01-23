# -*- coding: utf-8 -*-
{
    'name': "Alcance - GT",
    'description': """
        Mantenimiento para ir almancenando los alcances de un proyecto
    """,
    'author': "Alexis Juarez.",
    'website': "https://www.linkedin.com/in/alexis-juarez-8bb61b214",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Rights',
    'version': '1.0',

    'depends': ['sale'],
    'data': [
        # 'data/pais.xml',
        'security/ir.model.access.csv',
        'views/alcance_implementacion_view.xml',
        'views/plantilla_alcance_view.xml',
        'views/sale_view.xml',
        'views/sale_pdf.xml',
        'views/menu_view.xml',
    ],
}
