from odoo import fields, models


class EstateProperty(models.Model):
    _name = 'estate.management.property'
    _description = 'Estate Property'

    name = fields.Char(string='Property Name', required=True)
    address = fields.Char(string='Address')
    customer_id = fields.Many2one(
        comodel_name='estate.management.customer',
        string='Customer',
        ondelete='set null',
    )

