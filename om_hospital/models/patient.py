from datetime import date
import dateutil.utils
from odoo import api, fields, models, _, tools

class HospitalPatient(models.Model):

    _name = "hospital.patient"
    _inherit =["mail.thread",'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True)
    ref =  fields.Char(string='Reference')
    date_of_birth = fields.Date (string='Date of Birth')
    age = fields.Integer(String="Age" , compute='_compute_age')
    gender = fields.Selection ([('Male','Male'),('female','female')], string='Gender')
    active = fields.Boolean(string="Active",default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointments")


    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today=date.today()
            if rec.date_of_birth:
                rec.age = today.year  - rec.date_of_birth.year
            else:
             rec.age=0





    # name = fields.Char(string='Account Type', required=True, translate=True)
    # include_initial_balance = fields.Boolean(string="Bring Accounts Balance Forward", help="Used in reports to know if we should consider journal items from the beginning of time instead of from the fiscal year only. Account types that should be reset to zero at each new fiscal year (like expenses, revenue..) should not have this option set.")
    # type = fields.Selection([
    #     ('other', 'Regular'),
    #     ('receivable', 'Receivable'),
    #     ('payable', 'Payable'),
    #     ('liquidity', 'Liquidity'),
    # ], required=True, default='other',
    #     help="The 'Internal Type' is used for features available on "\
    #     "different types of accounts: liquidity type is for cash or bank accounts"\
    #     ", payable/receivable is for vendor/customer accounts.")