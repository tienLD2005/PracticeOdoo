# -*- coding: utf-8 -*-
# from odoo import http


# class TienDepTrai(http.Controller):
#     @http.route('/tien_dep_trai/tien_dep_trai', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tien_dep_trai/tien_dep_trai/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tien_dep_trai.listing', {
#             'root': '/tien_dep_trai/tien_dep_trai',
#             'objects': http.request.env['tien_dep_trai.tien_dep_trai'].search([]),
#         })

#     @http.route('/tien_dep_trai/tien_dep_trai/objects/<model("tien_dep_trai.tien_dep_trai"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tien_dep_trai.object', {
#             'object': obj
#         })

