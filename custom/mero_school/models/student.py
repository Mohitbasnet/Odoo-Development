from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SchoolStudent(models.Model):
    _name = "school.student"
    _description = 'Student Information'
    _inherit = ['mail.thread']

    name = fields.Char(string="Name",required=True, tracking=True)
    age = fields.Integer(string='Age',tracking=True)
    is_child = fields.Boolean(string="Is Child ?",tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender',tracking=True)
    address = fields.Text(string='Address',tracking=True)
    phone = fields.Char(string='Phone',tracking=True)
    email = fields.Char(string='Email',tracking=True)
    capitalized_name = fields.Char(string="Capitalized Name", compute='_compute_captalized_name',store=True)
    ref = fields.Char(string="Reference", default=lambda self:_('New')) 
    teacher_id = fields.Many2one('school.teacher',string="Teacher")
    tag_ids = fields.Many2many('res.partner.category', 'school_student_tag_rel','student_id' ,'tag_id', string="Tags")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'] .next_by_code('school.student')
        return super(SchoolStudent, self).create(vals_list)

    @api.depends('name')
    def _compute_captalized_name(self):
        for rec in self:
           if rec.name:
               rec.capitalized_name = rec.name.upper()
           else:
               rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        if self.age <=10:
            self.is_child = True
        else:
            self.is_child = False
    

    @api.constrains('is_child','age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
               raise ValidationError(_("Age has to be Recorded"))