from odoo import fields, models,api
from datetime import timedelta


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property Offer'

    price = fields.Float(string="Price")
    status = fields.Selection([
        ('accepted','Accepted'),('refused',"Refused")
        ],string="Staus")
    
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string = "Validity")
    deadline = fields.Date(string="Deadline", inverse = "_inverse_deadline")
    creation_date = fields.Date(string="Create Date")


    @api.depends("validity","creation_date")
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False
    
    def _inverse_deadline(self):
        for rec in self:
            rec.validity = (rec.deadline - rec.creation_date).days
      
    