from odoo import models, fields, api
import requests, random

class PokemonList(models.Model):
    _name = 'pokemon.list'
    _description = 'Pokemon'

    name = fields.Char(string='Pokemon ID', help='ID of the Pokemon', readonly=True)
    pokemon_name = fields.Char(string='Pokemon Name', help='Name of the Pokemon')
    game_versions = fields.Text(string='Pokemon Games', help='Games of the Pokemon')
    partner_id = fields.One2many(
        'res.partner',
        'pokemon_id',
        string='Partner ID',
        help='Partner associated with Pokémon'
    )
    
    partner_name = fields.Char(
        related='partner_id.name',
        string = 'Partner',
        help='Name of the Partner associated with the Pokémon'
    )