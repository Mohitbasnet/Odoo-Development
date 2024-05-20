from odoo import fields, models


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate property Offer'

    price = fields.Float(string="Price")
    status = fields.Selection([
        ('accepted','Accepted'),('refused',"Refused")
        ],string="Staus")
    
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
      
    