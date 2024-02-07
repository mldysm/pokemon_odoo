# -*- coding: utf-8 -*-
# from odoo import http


# class PokemonCustom(http.Controller):
#     @http.route('/pokemon_custom/pokemon_custom', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pokemon_custom/pokemon_custom/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pokemon_custom.listing', {
#             'root': '/pokemon_custom/pokemon_custom',
#             'objects': http.request.env['pokemon_custom.pokemon_custom'].search([]),
#         })

#     @http.route('/pokemon_custom/pokemon_custom/objects/<model("pokemon_custom.pokemon_custom"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pokemon_custom.object', {
#             'object': obj
#         })

