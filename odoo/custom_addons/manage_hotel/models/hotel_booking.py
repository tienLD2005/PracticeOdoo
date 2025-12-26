from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta


class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Phiếu đặt phòng'
    _order = 'check_in desc, code'

    code = fields.Char(string='Mã booking', required=True, copy=False, default=lambda self: _('New'))
    check_in = fields.Date(string='Ngày nhận phòng', required=True, default=fields.Date.today)
    check_out = fields.Date(string='Ngày trả phòng', required=True)
    duration = fields.Integer(string='Số đêm lưu trú', compute='_compute_duration', store=True, readonly=True)
    total_amount = fields.Integer(string='Tổng thành tiền', compute='_compute_total_amount', store=True, readonly=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Hoàn thành')
    ], string='Trạng thái', default='draft', required=True, readonly=True)
    
    customer_id = fields.Many2one('hotel.customer', string='Khách hàng', required=True)
    room_id = fields.Many2one('hotel.room', string='Phòng', required=True)
    service_ids = fields.Many2many('hotel.service', string='Dịch vụ thêm')

    @api.model
    def create(self, vals):
        """Tự động tạo mã booking khi tạo mới"""
        if vals.get('code', _('New')) == _('New'):
            vals['code'] = self.env['ir.sequence'].next_by_code('hotel.booking') or _('New')
        return super(HotelBooking, self).create(vals)

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        """Tính số đêm lưu trú"""
        for record in self:
            if record.check_in and record.check_out:
                delta = record.check_out - record.check_in
                record.duration = delta.days if delta.days > 0 else 0
            else:
                record.duration = 0

    @api.depends('room_id', 'room_id.price_per_night', 'duration', 'service_ids', 'service_ids.price')
    def _compute_total_amount(self):
        """Tính tổng thành tiền"""
        for record in self:
            total = 0
            if record.room_id and record.duration and record.room_id.price_per_night:
                total += record.room_id.price_per_night * record.duration
            if record.service_ids:
                for service in record.service_ids:
                    if service.price:
                        total += service.price
            record.total_amount = total

    @api.onchange('check_in')
    def _onchange_check_in(self):
        """Tự động điền ngày trả phòng khi nhập ngày nhận"""
        if self.check_in:
            self.check_out = self.check_in + timedelta(days=1)

    @api.onchange('check_out')
    def _onchange_check_out(self):
        """Trigger lại computed fields khi ngày trả thay đổi"""
        pass

    @api.onchange('room_id')
    def _onchange_room_id(self):
        """Kiểm tra trạng thái phòng khi chọn"""
        if self.room_id and self.room_id.status == 'maintenance':
            return {
                'warning': {
                    'title': 'Cảnh báo',
                    'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
                }
            }

    @api.onchange('service_ids')
    def _onchange_service_ids(self):
        """Trigger lại computed field khi dịch vụ thay đổi"""
        pass

    @api.constrains('check_in', 'check_out')
    def _check_dates(self):
        """Kiểm tra ngày trả phải lớn hơn ngày nhận"""
        for record in self:
            if record.check_in and record.check_out:
                if record.check_out <= record.check_in:
                    raise ValidationError('Ngày trả phòng không hợp lệ!')

    @api.constrains('room_id')
    def _check_room_status(self):
        """Kiểm tra phòng không được đang có người ở khi tạo booking"""
        for record in self:
            if record.room_id and record.room_id.status == 'occupied':
                raise ValidationError('Phòng này đang có khách ở!')


