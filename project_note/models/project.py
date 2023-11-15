# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, _
from odoo.tools import html2plaintext


class ProjectProject(models.Model):
    _inherit = "project.project"

    note_count = fields.Integer(compute='_compute_project_notes')

    def _compute_project_notes(self):
        for rec in self:
            note_ids = rec.env['note.note'].search([('project_id', '=', rec.id)])
            rec.note_count = len(note_ids)

    def action_project_notes(self):
        self.ensure_one()
        note_ids = self.env['note.note'].search([('project_id', '=', self.id)])
        action = self.env["ir.actions.actions"]._for_xml_id("note.action_note_note")
        action['domain'] = [('id', '=', note_ids.ids)]
        if len(note_ids) == 1:
            action['views'] = [[False, "form"]]
            action['view_mode'] = 'form'
            action['res_id'] = note_ids.id
        if not note_ids:
            action['context'] = {'default_project_id': self.id}
        return action
