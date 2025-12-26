from odoo import models, fields, api


class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Loại phòng khách sạn'
    _order = 'name'

    name = fields.Char(string='Tên loại', required=True)
    code = fields.Char(string='Mã loại')

    room_ids = fields.One2many('hotel.room', 'type_id', string='Danh sách phòng')

