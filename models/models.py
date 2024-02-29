# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test_email(models.Model):
    _name = 'test.email'
    _description = 'test email'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    status = fields.Selection([
        ('cancel', 'Cancel'),
        ('open', 'Open'),
        ('close', 'Close'),
        ('finish', 'Finish'),
    ], string='Status', default='open') 
    
    
    pic_perusahaan = fields.Char()
    jenis_po = fields.Char()
    nama_customer = fields.Char()
    kode_customer = fields.Char()
    tanggal_konfirm_user = fields.Char()
    tanggal_terima_po = fields.Char()
    name = fields.Char()
    tanggal_permintaan = fields.Char()
    requested_by = fields.Char()
    vessel_divisi = fields.Char()
    project_unit = fields.Char()
    kode_budget = fields.Char()
    prioritas = fields.Char()
    nama_produk = fields.Char()
    jenis_tipe = fields.Char()
    vol = fields.Char()
    satuan = fields.Char()
    supply = fields.Char()
    kode_unit_barang = fields.Char()
    status_list = fields.Char()
    nomor_do = fields.Char()
    tanggal_do = fields.Char()
    est_date = fields.Char()
    nama_penerima = fields.Char()
    remark = fields.Char()
    date_remark = fields.Char()
    remark_2 = fields.Char()
    date_remark_2 = fields.Char()
    remark_3 = fields.Char()
    date_remark_3 = fields.Char()
    remark_4 = fields.Char()
    date_remark_4 = fields.Char()
    remark_5 = fields.Char()
    date_remark_5 = fields.Char()


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
    partner_id = fields.Many2one("res.partner", string="Recipients")
    company_id = fields.Many2one("res.company", string="COmpany")

    def action_send_email(self):
        data = 'mutaqin'
        
        mail_template = self.env.ref('cron_demo.email_template')
        mail_template.email_to = 'khoerulmutaqin529@yahoo.com'
        mail_template.email_from = 'khoerulmutaqin225@gmail.com'
        mail_template.send_mail(self.id, force_send=True)