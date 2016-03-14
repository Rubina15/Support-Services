# -*- coding: utf-8 -*-
from openerp import http

# class Time(http.Controller):
#     @http.route('/time/time/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/time/time/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('time.listing', {
#             'root': '/time/time',
#             'objects': http.request.env['time.time'].search([]),
#         })

#     @http.route('/time/time/objects/<model("time.time"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('time.object', {
#             'object': obj
#         })