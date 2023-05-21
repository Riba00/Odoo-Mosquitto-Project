# -*- coding: utf-8 -*-
from odoo import http

# class Mqtt(http.Controller):
#     @http.route('/mqtt/mqtt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mqtt/mqtt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mqtt.listing', {
#             'root': '/mqtt/mqtt',
#             'objects': http.request.env['mqtt.mqtt'].search([]),
#         })

#     @http.route('/mqtt/mqtt/objects/<model("mqtt.mqtt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mqtt.object', {
#             'object': obj
#         })