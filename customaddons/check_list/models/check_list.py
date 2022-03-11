from odoo import api, models, fields


class checkList(models.Model):
    _name = "check.list"
    name = fields.Char(string="name")
    name_work = fields.Char(string="Name Work",track_visibility='onchange')
    description = fields.Char(string="Description")
    status = fields.Selection(selection=[
        ('done', 'Done'),
        ('progress', 'In Progress'),
        ('cancel', 'Cancel')
    ], string="Status", readonly=True, track_visibility='onchange')

    def set_done(self):
        self.write({
            'status': 'done',
        })

    def set_progress(self):
        self.write({
            'status': 'progress',
        })

    def set_cancel(self):
        self.write({
            'status': 'cancel',
        })

    def reset(self):
        self.write({
            'status': '',
        })
