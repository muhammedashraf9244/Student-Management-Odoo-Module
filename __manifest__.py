##############################################################################
#
#    Odoo Contribute Community
#    Copyright (C) 2020-2021 Tiny SPRL (<http://tiny.be>).
#    Made By Mohammed Ashraf Odoo Developer.
#    Copyright (C) 2020-2021 Muhammed Ashraf.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Student Registration Management',
    'author': 'Mohammed Ashraf@Odoo Developer',
    'website': 'https://github.com/muhammedashraf9244/Student-Management-Odoo-Module',
    'category': 'Student',
    'description': "A student registration management module",
    'depends': ['base', 'sale'],
    'data': [
        'views/student_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}