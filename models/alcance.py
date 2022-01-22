# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alcance(models.Model):

    _name = 'alcance.gt.mantenimiento.alcance'
    _description = "Matenimiento para almacenar proyectos"

    alcance = fields.Char("Alcance", required=True)
    activo = fields.Boolean("Activo", default=True)
    company_id =  fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company)
    descricpion =  fields.Html(string='Descripcion')
    multi_company = self.env['res.config.settings'].sudo().search([])

    


