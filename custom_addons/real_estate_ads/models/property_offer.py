from odoo import fields, models,api
from datetime import timedelta
from odoo.exceptions import ValidationError


class PropertyOffer(models.Model):
    _name = 'estate.property.offer' 
    _description = 'Estate property Offer'


    @api.depends('partner_id', 'property_id')
    def _compute_name(self):
        for rec in self:
            if rec.property_id and rec.partner_id:
                rec.name = f"{rec.partner_id.name} - {rec.property_id.name}"
            else:
                rec.name = False

    name  = fields.Char(string="Description", compute='_compute_name')
    price = fields.Float(string="Price")
    status = fields.Selection([
        ('accepted','Accepted'),('refused',"Refused")
        ],string="Staus")
    
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string = "Validity")
    deadline = fields.Date(string="Deadline", inverse = "_inverse_deadline", compute="_compute_deadline")



    # @api.model
    # def _set_create_date(self):
    #     return fields.Date.today()
    
    creation_date = fields.Date(string="Create Date")
    
    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline  and rec.creation_date:

                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = False

    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get("creation_date"):
                rec['creation_date'] = fields.Date.today()
        return super(PropertyOffer,self).create(vals)


    @api.depends("validity","creation_date")
    def _compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    @api.constrains('deadline', 'creation_date')
    def _check_validity(self):
        for rec in self:
            if rec.deadline and rec.creation_date and rec.deadline <= rec.creation_date:
                raise ValidationError('Deadline cannot be before creation date')

    

    
    # _sql_constraints = [
    #     ('check_validity', 'check(validity > 0)','Deadline cannot be before creation date')
    # ]
    
    
      
    