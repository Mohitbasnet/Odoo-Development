from odoo import fields,models,api

class Property(models.Model):
    _name = 'estate.property'
    _description = "This is the model made by mohit"

    name = fields.Char(string="Name")
    state = fields.Selection([
        ('new','New'),('received',"Offer Received"),('acceted','Offer Accepted'),('sold','Sold'),('cancel','Cancelled')
        ],default='new', string="Status")
    tag_ids = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id = fields.Many2one('estate.property.type',string="Property Type")
    offer_ids = fields.One2many('estate.property.offer', 'property_id',string="Offers")
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

    sales_id = fields.Many2one('res.users',string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company','=',True)])
    phone = fields.Char(string="Phone", related = "buyer_id.phone")
    
    

    def action_sold(self):
        self.state = 'accepted'
    
    def action_cancel(self):
        self.state = 'refused'


    @api.onchange("living_area","garden_area")
    def _onchange_total_area(self):
        
        self.total_area = self.living_area + self.garden_area

    total_area = fields.Integer(string="Total Area")

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = "Property Type"
    name =  fields.Char(string="Name", required=True)

class PropertyTag(models.Model):
    _name='estate.property.tag'
    _description="Property Tag"

    name = fields.Char(string="Name", required=True)






     

