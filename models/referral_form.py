from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)


class EmployeeReferral(models.Model):
    _name = 'employee.referral'
    _description = 'Employee Referral'

    name = fields.Char(string="Candidate Name",required=True)
    contact = fields.Char(string="Contact No.",required=True)
    position = fields.Char(string="Job Position",required=True)
    notes = fields.Text(string="Add Notes")
    resume = fields.Binary(string="Upload Resume")
    status = fields.Selection([('submitted','Submitted'),('in_review','In review'),('hired','Hired'),('rejected','Rejected')],string="Status")

    @api.constrains('name')
    def _check_name(self):
        for rec in self:
            if rec.name.isdigit()==True:
                raise ValidationError("Candidate Name Cannot be Digit")
            
    @api.constrains('contact')
    def _check_contact(self):
        for rec in self:
            if rec.contact.isdigit()==False:
                raise ValidationError("Contact Number Should be Digit")
            elif len(rec.contact)<10 or len(rec.contact)>10:
                raise ValidationError("Contact Number Must have 10 Digits")
            