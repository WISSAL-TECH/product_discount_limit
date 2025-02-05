# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: ANURUDH P (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
from odoo import fields, models


class ProductCategory(models.Model):
    """Inherited product.category to add field Discount Limit"""
    _inherit = 'product.category'

    desc_limit = fields.Float(
        string="Limite de remise (%)",
        help="Si spécifié, l'utilisateur ne peut pas accorder une "
             "remise supérieure au montant"
    )
    min_limit = fields.Float(
        string="Limite minimale de remise (%)",
        help="Si spécifié, l'utilisateur ne peut pas accorder une "
             "remise inférieure à ce montant"
    )
