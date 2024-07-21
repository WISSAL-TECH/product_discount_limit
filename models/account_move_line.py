from odoo import api, exceptions, models, _


class AccountMoveLine(models.Model):
    """Inherited account.move.line for checking the limit of discount
    allowed for product and category"""
    _inherit = 'account.move.line'

    @api.onchange('discount')
    def _onchange_discount(self):
        """Checking the limit of discount allowed for products and category"""
        if not self.env.user.allow_discount:
            desc_limit = self.product_id.product_tmpl_id.desc_limit or \
                         self.product_id.categ_id.desc_limit
            min_limit = self.product_id.product_tmpl_id.min_limit or \
                         self.product_id.categ_id.min_limit
            if desc_limit and self.discount > desc_limit:
                raise exceptions.UserError(
                    _('Vous n\'êtes pas autorisé à appliquer une remise de plus de %s '
                        'sur %s. Veuillez contacter votre '
                        'administrateur',
                      desc_limit,
                      'ce produit' if self.product_id.product_tmpl_id else
                      'cet catégorie'))
            if min_limit and min_limit > self.discount and self.discount != 0:
                raise exceptions.UserError(
                    _('Vous n\'êtes pas autorisé à appliquer une remise de moins de %s '
                        'sur %s. Veuillez contacter votre '
                        'administrateur',
                      min_limit,
                      'ce produit' if self.product_id.product_tmpl_id else
                      'cet catégorie'))
