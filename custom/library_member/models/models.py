# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):
    _inherit = "library.book"
    is_available=fields.Boolean("Is Available?")
    isbn = fields.Char(help="should be 5 digit or 6 digit that starts")
    publisher_id = fields.Many2one(index=True)

    @api.constrains('isbn')
    def check_isbn(self):
        self.ensure_one()
        if len(self.isbn) == 6:
            if self.isbn[0] == "A":
                return True
            else:
                raise ValidationError("Can only be 5 be digits or 6 if starts with A")

        else:
            return super().check_isbn()
