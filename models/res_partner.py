from odoo import models, fields, api
import requests
import random

class ResPartner(models.Model):
    _inherit = 'res.partner'

    pokemon_id = fields.Many2one('pokemon.list', string='Pokemon ID', help='ID of the Pokemon', readonly=True, ondelete='set null')
    pokemon = fields.Char(related='pokemon_id.name', string='Pokemon Name', help='Name of the Pokemon')
    pokemon_name = fields.Char(related='pokemon_id.pokemon_name', string='Pokemon Name', help='Name of the Pokemon')
    game_versions = fields.Text(related='pokemon_id.game_versions', string='Pokemon Games', help='Games of the Pokemon')

    def write(self, vals):
        if 'is_company' in vals and not vals['is_company']:
            if self.pokemon_id:
                old_pokemon = self.pokemon_id
                self.pokemon_id = None
                old_pokemon.unlink()
        return super(ResPartner, self).write(vals)
    
    def generate_random_number(self):
        return random.randint(1, 100)

    def get_unique_random_number(self):
        used_numbers = self.env['res.partner'].search([('pokemon_id', '!=', False)]).mapped('pokemon_id.id')
        random_number = random.randint(1, 100)
        while random_number in used_numbers:
            random_number = random.randint(1, 100)

        return random_number

    def get_pokemon(self):
        random_number = self.get_unique_random_number()
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_number}/')
        data = response.json()

        pokemon_name = data['name']
        pokemon_id = data['id']
        game_indices = data['game_indices']
        game_versions = '\n'.join([f"{index['version']['name']}: {index['game_index']}" for index in game_indices])

        if self.pokemon_id:
            old_pokemon = self.pokemon_id
            self.pokemon_id = None
            old_pokemon.unlink()
            
        pokemon = self.env['pokemon.list'].create({
            'name' : str(pokemon_id),
            'pokemon_name' : pokemon_name,
            'game_versions' : game_versions,
        })
        self.pokemon_id = pokemon.id