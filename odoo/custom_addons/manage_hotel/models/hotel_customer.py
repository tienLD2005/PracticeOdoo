from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Khách hàng'
    _order = 'name'

    name = fields.Char(string='Tên khách', required=True)
    identity_card = fields.Char(string='Số CMND/CCCD')
    phone = fields.Char(string='Số điện thoại')

    booking_ids = fields.One2many('hotel.booking', 'customer_id', string='Lịch sử đặt phòng')

    _sql_constraints = [
        ('identity_card_unique', 'UNIQUE(identity_card)', 'Số CMND/CCCD phải là duy nhất!'),
    ]

    @api.constrains('identity_card')
    def _check_identity_card_unique(self):
        """Kiểm tra CMND/CCCD duy nhất (chỉ khi có giá trị)"""
        for record in self:
            if record.identity_card:
                duplicates = self.search([
                    ('identity_card', '=', record.identity_card),
                    ('id', '!=', record.id)
                ])
                if duplicates:
                    raise ValidationError('Số CMND/CCCD phải là duy nhất!')

