from odoo import fields,models

class Property(models.Model):
    _name = 'estate.property'
    _description = "This is the model made by mohit"

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available from")
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(srting="Selling Price")
    best_offer = fields.Float(string="Best Offer")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(String="Facades")
    garage = fields.Boolean(string="Garage",default =False)
    garden = fields.Boolean(string="Garden", default = False) 
    garden_area = fields.Integer(string="Garden Area")
    garden_orientaion = fields.Selection([
        ('north','North'),('west',"West"),('east','East'),('south','South')
        ],string="Garden Orientation",default='north')
     


     

