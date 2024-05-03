# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryCheckout(http.Controller):
#     @http.route('/library_checkout/library_checkout', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_checkout/library_checkout/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_checkout.listing', {
#             'root': '/library_checkout/library_checkout',
#             'objects': http.request.env['library_checkout.library_checkout'].search([]),
#         })

#     @http.route('/library_checkout/library_checkout/objects/<model("library_checkout.library_checkout"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_checkout.object', {
#             'object': obj
#         })
