# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.tools import html2plaintext


class Note(models.Model):
    _inherit = 'note.note'

    project_id = fields.Many2one(comodel_name='project.project', string='Project')
    task_ids = fields.Many2many(comodel_name='project.task', column1='note_id', column2='task_id', string='Tasks',
                                domain="[('project_id', '=', project_id)]")
