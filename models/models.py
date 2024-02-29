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
    
    
    pic_perusahaan = fields.Char(string='Perusahaan PIC')
    jenis_po = fields.Char(string='Jenis PO')
    nama_customer = fields.Char(string='Nama Customer')
    kode_customer = fields.Char(string='Kode Customer')
    tanggal_konfirm_user = fields.Char(string='Tanggal Konfirmasi User')
    tanggal_terima_po = fields.Char(string='Tanggal Terima PO')
    name = fields.Char(string='Nama')
    tanggal_permintaan = fields.Char(string='Tanggal Permintaan')
    requested_by = fields.Char(string='Requested By')
    vessel_divisi = fields.Char(string='Vessel Divisi')
    project_unit = fields.Char(string='Project Unit')
    kode_budget = fields.Char(string='Kode Budget')
    prioritas = fields.Char(string='Prioritas')
    nama_produk = fields.Char(string='Nama Produk')
    jenis_tipe = fields.Char(string='Jenis Tipe')
    vol = fields.Char(string='Volume')
    satuan = fields.Char(string='Satuan')
    supply = fields.Char(string='Supply')
    kode_unit_barang = fields.Char(string='Kode Unit Barang')
    status_list = fields.Char(string='Status List')
    nomor_do = fields.Char(string='Nomor DO')
    tanggal_do = fields.Char(string='Tanggal DO')
    est_date = fields.Char(string='Estimasi Date')
    nama_penerima = fields.Char(string='Nama Penerima')
    remark = fields.Char(string='Remark')
    date_remark = fields.Char(string='Tanggal Remark')
    remark_2 = fields.Char(string='Remark 2')
    date_remark_2 = fields.Char(string='Tanggal Remark 2')
    remark_3 = fields.Char(string='Remark 3')
    date_remark_3 = fields.Char(string='Tanggal Remark 3')
    remark_4 = fields.Char(string='Remark 4')
    date_remark_4 = fields.Char(string='Tanggal Remark 4')
    remark_5 = fields.Char(string='Remark 5')
    date_remark_5 = fields.Char(string='Tanggal Remark 5')


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