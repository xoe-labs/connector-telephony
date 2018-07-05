# -*- coding: utf-8 -*-
# © 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class BaseConfigSettings(models.TransientModel):
    _inherit = 'base.config.settings'

    import wdb; wdb.set_trace()  # breakpoint aa2d57b6 //
    number_of_digits_to_match_from_end = fields.Integer(
        related='company_id.number_of_digits_to_match_from_end')
