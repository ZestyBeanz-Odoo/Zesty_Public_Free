from odoo import api, fields, models, _, tools

class HospitalAppointment(models.Model):

    _name = "hospital.appointment"
    _inherit =[ "mail.thread",'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_id'
    patient_id = fields.Many2one('hospital.patient',string="Patient",required=True)
    appointment_time = fields.Datetime(string='Appointment Time',default=fields.Datetime.now,required=True)
    booking_date = fields.Date(string='Booking Date',default=fields.Date.context_today,required=True)
    gender = fields.Selection( related='patient_id.gender' )
    ref = fields.Char(string='Reference',help="Reference from patient record!")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([('0', 'Normal'), ('1', 'Low'), ('2', 'High'), ('3', 'Very High')], string='Priority')

    state = fields.Selection([('draft', 'Draft'), ('in_consultation', 'In_consultation'), ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string='status',required=True)
    pharmacy_line_ids = fields.One2many('appointment.pharmacylines','appointment_id',string='Pharmacy Lines')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref

    def action_test(self):
        print("Button clicked.....!!")
        return{
            'effect': {
                'fadeout': 'slow',
                'message': 'click successful',
                'type': 'rainbow_man'
            }
        }

class AppointmentPharmacyLines(models.Model):
      _name = "appointment.pharmacylines"
      _description = "Appointment Pharmacy Lines"

      product_id = fields.Many2one('product.product')
      qty= fields.Integer(string='Quantity')
      price_unit = fields.Float(string="Price")
      appointment_id = fields.Many2one('hospital.appointment', string='Appointment')



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

