# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError
class library_app(models.Model):
    _name = 'library.book'
    _description = 'Books'
   
  

    name = fields.Char("Title", 
                       required=True)
    isbn = fields.Char("ISBN")
    active = fields.Boolean("Active?", default=True)
    date_published = fields.Date()
    image = fields.Binary("Cover")
    publisher_id = fields.Many2one("res.partner",
                                    string="Publisher")
    author_ids = fields.Many2many("res.partner",
                                  srting="Authors")
    

    @api.constrains('isbn')
    def check_isbn(self):
        for book in self:
            if not book.isbn:
                raise ValidationError("Please provide an ISBN for %s" %book.name)
            if book.isbn and not len(book.isbn) == 5:
                raise ValidationError("%s ISBN is invalid\nNeeds to be five digits only" %book.isbn)
            return True
        
    # book_type = fields.Selection(
    #     [
    #         ("paper","Paperback"),
    #         ("hard","Hardcover"),
    #         ("electronic","Electronic"),
    #         ("other","Other")

    #     ],
    #     "Type"
    # )

#     notes = fields.Text("Internal Notes")
#     descr = fields.Html("Description")

#     copies = fields.Integer(default=1)
#     avg_rating = fields.Float("Average Rating", (3,2))
#     price=fields.Monetary("Price","currency_id")
    
#     currency_id = fields.Many2one("res.currency")

   
#     last_borrow_date=fields.Datetime(
#         "Last Borrowed On",
#         default=lambda self: fields.Datetime.now()
#     )
# #
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
