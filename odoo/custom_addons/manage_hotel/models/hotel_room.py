from odoo import models, fields, api


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Phòng khách sạn'
    _order = 'name'

    name = fields.Char(string='Số phòng', required=True)
    floor = fields.Integer(string='Tầng')
    price_per_night = fields.Integer(string='Giá thuê 1 đêm')
    status = fields.Selection([
        ('available', 'Trống'),
        ('occupied', 'Đang ở'),
        ('maintenance', 'Bảo trì')
    ], string='Trạng thái', default='available', required=True)
    
    type_id = fields.Many2one('hotel.room.type', string='Loại phòng', required=True)
    
    booking_ids = fields.One2many('hotel.booking', 'room_id', string='Lịch sử đặt phòng')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Số phòng phải là duy nhất!'),
        ('price_positive', 'CHECK(price_per_night > 0)', 'Giá phòng phải lớn hơn 0!'),
    ]

