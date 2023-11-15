# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import ipdb

from odoo import api, fields, models, _
from odoo.tools import html2plaintext


class ProjectTask(models.Model):
    _inherit = "project.task"

    note_ids = fields.Many2many('note.note', string='Notes', compute='_compute_note_ids')
    note_count = fields.Integer(compute='_compute_note_ids', string='# Notes', store=True)

    @api.depends('project_id')
    def _compute_note_ids(self):
        for rec in self:
            rec.note_ids = rec.env['note.note'].search([('project_id', '=', rec.project_id.id)]).filtered(
                lambda x: x.task_ids in rec)
            rec.note_count = len(rec.note_ids)

    def _action_view_notes(self, notes=None):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("note.action_note_note")
        action['domain'] = [('id', 'in', notes.ids)]
        if len(notes) == 1:
            action['views'] = [[False, "form"]]
            action['view_mode'] = 'form'
            action['res_id'] = notes.id
        return action

    def action_view_notes(self):
        return self._action_view_notes(notes=self.note_ids)

    def action_create_note(self):
        note_values = {
            'name': self.name,
            'project_id': self.project_id.id,
            'task_ids': [(6, 0, self.ids)],
        }
        note = self.env['note.note'].create(note_values)
        return self._action_view_notes(notes=note)
