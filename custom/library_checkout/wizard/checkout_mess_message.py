
from odoo import fields, models

from odoo.exceptions import UserError

class CheckoutMassMessage(models.TransientModel):
        _name = "library.checkout.massmessage"
        _description = "Send Message to Borrowers"

        checkout_ids = fields.Many2many("library.checkout",string="Checkouts",)
        message_subject = fields.Char()
        message_body = fields.Html()


        def button_send(self):
                self.ensure_one()

                if not self.checkout_ids:
                        raise exceptions.UserError(
                                "No checkouts were selected."
                        )
                if not self.message_body:
                        raise exceptions.UserError(
                                "A message body is required"

        
                        )  
                return True 