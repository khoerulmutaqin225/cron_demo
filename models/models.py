# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test_email(models.Model):
    _name = 'test.email'
    _description = 'test email'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    partner_id = fields.Many2one("res.partner", string="Recipients")
    company_id = fields.Many2one("res.company", string="COmpany")

    def action_send_email(self):
        data = 'mutaqin'
        
        mail_template = self.env.ref('test_email.email_template')
        mail_template.email_to = 'alwanassyauqi11@gmail.com'
        mail_template.send_mail(self.id, force_send=True)