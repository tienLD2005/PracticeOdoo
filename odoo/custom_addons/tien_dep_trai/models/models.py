# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class tien_dep_trai(models.Model):
#     _name = 'tien_dep_trai.tien_dep_trai'
#     _description = 'tien_dep_trai.tien_dep_trai'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

