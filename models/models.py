# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pokemon_custom(models.Model):
#     _name = 'pokemon_custom.pokemon_custom'
#     _description = 'pokemon_custom.pokemon_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

