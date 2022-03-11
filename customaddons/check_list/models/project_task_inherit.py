from google.protobuf.unittest_custom_options_pb2 import required_enum_opt

from odoo import api, models, fields


class ProjectInherit(models.Model):
    _inherit = "project.task"
    check_list = fields.Boolean(string="Check List", default=False)
    info_check_list = fields.One2many(inverse_name='name', comodel_name='check.list', required=True,
                                      track_visibility='onchange')
    progress_rate = fields.Integer(string="Progress Rate", compute='set_rate')
    total = fields.Integer(string="Total")
    status = fields.Selection([
        ('done', 'Done'),
        ('progress', 'In Progress'),
        ('cancel', 'Cancel')
    ], string="Status", readonly=True, track_visibility='onchange')
    max_rate = fields.Integer(default=100)

    def set_rate(self):
        for rec in self:
            rec.progress_rate = 0
            total = len(rec.info_check_list)
            done = 0
            cancel = 0
            if total == 0:
                pass
            else:
                for i in rec.info_check_list:
                    if i.status == 'done':
                        done += 1
                    elif i.status == 'cancel':
                        cancel += 1
                if cancel == total:
                    rec.progress_rate = 0
                else:
                    rec.progress_rate = round(done / (total - cancel), 2) * 100
