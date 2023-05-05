# -*- coding: utf-8 -*-
# from odoo import http


# class HelloW(http.Controller):
#     @http.route('/hello_w/hello_w', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hello_w/hello_w/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hello_w.listing', {
#             'root': '/hello_w/hello_w',
#             'objects': http.request.env['hello_w.hello_w'].search([]),
#         })

#     @http.route('/hello_w/hello_w/objects/<model("hello_w.hello_w"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hello_w.object', {
#             'object': obj
#         })
