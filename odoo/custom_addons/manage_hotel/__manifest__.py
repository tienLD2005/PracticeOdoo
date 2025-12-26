{
    'name': 'Quản lý Khách sạn',
    'version': '17.0.1.0.0',
    'category': 'Hotel',
    'summary': 'Module quản lý phòng và đặt phòng khách sạn',
    'description': """
        Module Quản lý Khách sạn
        ========================
        - Quản lý phòng khách sạn và loại phòng
        - Quản lý đặt phòng (Booking)
        - Quản lý khách hàng
        - Quản lý dịch vụ đi kèm
        - Tính toán tự động tổng tiền
    """,
    'author': 'Hotel Management',
    'depends': ['base'],
    'data': [
        'security/hotel_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/hotel_room_type_views.xml',
        'views/hotel_service_views.xml',
        'views/hotel_customer_views.xml',
        'views/hotel_room_views.xml',
        'views/hotel_booking_views.xml',
        'views/hotel_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

