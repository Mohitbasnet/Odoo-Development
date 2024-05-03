# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Checkout(models.Model):
        _name = "library.checkout"
        
        _description = "Checkout Request"

        member_id = fields.Many2one("library.member",required=True,)
        user_id = fields.Many2one("res.users", "Librarian", default=lambda s: s.env.user,)
        request_date = fields.Date(default=lambda s: fields.Date.today(),)
        line_ids = fields.One2many("library.checkout.line",
                                    "checkout_id",
                                    string="Borrowed Books",)


class CheckoutLine(models.Model):
        _name = "library.checkout.line"
        _description = "Checkout Request Line"

        checkout_id = fields.Many2one("library.checkout",required=True,)
        book_id = fields.Many2one("library.book",required=True)
        note = fields.Char("Notes")
        
