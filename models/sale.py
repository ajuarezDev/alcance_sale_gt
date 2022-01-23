# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


class Sale(models.Model):
    _inherit = 'sale.order'

    alcance_id = fields.Many2one('alcance.gt.plantilla.alcance')
    template_ids = fields.One2many('alcance.gt.sale.alcance', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)


    @api.onchange('alcance_id')
    def onchange_field(self):
        if len(self.alcance_id.ids) > 0:
            
            ids = ','.join([str(x) for x in self.alcance_id.ids])
            self.template_ids = [(6,0,[])]
            # logging.warning(ids)
            plantilla_lines = self.env['alcance.gt.plantilla.alcance'].search([('id','=',ids)])
            child_alcance = plantilla_lines.child_alcance

            for lines_child_alcance in child_alcance:
                alcance_id =  lines_child_alcance.alcance_id.id
                descricpion =  lines_child_alcance.descricpion
                tiempo = lines_child_alcance.tiempo
                udm =  lines_child_alcance.udm.id

                # logging.warning(tiempo)
            
                self.template_ids = [(0,0, {
                    'alcance_id': alcance_id,
                    'descricpion': descricpion,
                    'tiempo':tiempo,
                    'udm':udm
                })]
        else :
            self.template_ids = [(6,0,[])]
        
class SaleLine(models.Model):

    _name = 'alcance.gt.sale.alcance'
    _description = 'Detalles de los alcances desde plantilla'

    order_id = fields.Many2one('sale.order', "Order")
    alcance_id =  fields.Many2one('alcance.gt.mantenimiento.alcance', string='Alcance', required=True)
    descricpion =  fields.Html(string='Descripcion', required=True)
    tiempo = fields.Float("Tiempo")
    udm =  fields.Many2one('uom.uom', string='UdM',)
    display_type = fields.Selection([
        ('line_section', "Section"),
        ('line_note', "Note")], default=False)



