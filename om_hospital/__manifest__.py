# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital Management',
    'author': 'Sathya',
    'sequence': -100,
    'summary': 'Hospital Management System',
    'depends': ['mail','product'],
    'data': ['security/ir.model.access.csv',
             'views/menu.xml',
             'views/appointment_view.xml',
             'views/patient_view.xml',
             'views/female_patient_view.xml'
             ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False
        
}