# -*- coding: utf-8 -*-

from odoo import models, fields


class openacademy(models.Model):
     _name = 'openacademy.cursos'
     _description = 'openacademy.cursos'

     curso = fields.Char(string="Curso")
     codigo = fields.Integer(string="Codigo")


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
