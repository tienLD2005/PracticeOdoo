from odoo import fields, models


class Customer(models.Model):
    _name = 'estate.management.customer'
    _description = 'Estate Customer'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    property_ids = fields.One2many(
        comodel_name='estate.management.property',
        inverse_name='customer_id',
        string='Properties',
    )

