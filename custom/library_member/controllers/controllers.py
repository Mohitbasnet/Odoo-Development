# -*- coding: utf-8 -*-
# from odoo import http


# class LibraryMember(http.Controller):
#     @http.route('/library_member/library_member', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/library_member/library_member/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('library_member.listing', {
#             'root': '/library_member/library_member',
#             'objects': http.request.env['library_member.library_member'].search([]),
#         })

#     @http.route('/library_member/library_member/objects/<model("library_member.library_member"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('library_member.object', {
#             'object': obj
#         })
