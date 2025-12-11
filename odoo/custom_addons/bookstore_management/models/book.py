from odoo import fields, models


class Book(models.Model):
    _name = 'bookstore.management.book'
    _description = 'Book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    price = fields.Float(string='Price', default=0.0, required=True)
    publish_date = fields.Date(string='Publish Date')

