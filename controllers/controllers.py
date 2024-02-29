# -*- coding: utf-8 -*-
# from odoo import http


# class TestEmail(http.Controller):
#     @http.route('/test_email/test_email/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_email/test_email/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_email.listing', {
#             'root': '/test_email/test_email',
#             'objects': http.request.env['test_email.test_email'].search([]),
#         })

#     @http.route('/test_email/test_email/objects/<model("test_email.test_email"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_email.object', {
#             'object': obj
#         })
