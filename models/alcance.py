# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alcance(models.Model):

    _name = 'alcance.gt.mantenimiento.alcance'
    _rec_name = 'alcance'
    _description = "Matenimiento para almacenar proyectos"

    alcance = fields.Char("Alcance", required=True)
    activo = fields.Boolean("Activo", default=True)
    company_id =  fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company, required=True,)
    descricpion =  fields.Html(string='Descripcion')

    


class PlantillaAlcance(models.Model):

    _name = 'alcance.gt.plantilla.alcance'
    _description = "pueda definir una plantilla para alcances"
    _rec_name = 'plantilla_alcances'

    plantilla_alcances = fields.Char("Plantilla de alcances", required=True)
    activo = fields.Boolean("Activo", default=True)
    company_id = fields.Many2one('res.company', string='Compañia', default=lambda self: self.env.company, required=True,)
    descricpion = fields.Html(string='Notas')
    child_alcance = fields.One2many('alcance.gt.child.plantilla.alcance', 'plantilla_alcance', string="Alcances")


class ChildPlantillaAlcance(models.Model):
    
    _name = 'alcance.gt.child.plantilla.alcance'

    plantilla_alcance = fields.Many2one('alcance.gt.plantilla.alcance',string='Embarque')
    alcance_id =  fields.Many2one('alcance.gt.mantenimiento.alcance', string='Alcance', required=True)
    descricpion =  fields.Html(string='Descripcion', required=True)
    tiempo = fields.Float("Tiempo")
    udm =  fields.Many2one('uom.uom', string='UdM',)

