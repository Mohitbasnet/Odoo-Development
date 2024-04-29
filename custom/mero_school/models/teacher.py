from odoo import models, fields

class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    # _inherits = {'school.student': 'related_patient_id'}
    _description = 'Teacher Record'
    _rec_name = 'ref'

    name = fields.Char(string="Name", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('fe_male', 'Female'),
    ], default='male', string="Gender")
    ref = fields.Char(string="Reference", required=True)
    active = fields.Boolean(default=True)


    def name_get(self):
        res = []
        for rec in self:
            
            res.append((rec.id,f'{rec.ref} - {rec.name}'))
        return res
