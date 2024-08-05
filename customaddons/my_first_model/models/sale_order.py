from odoo import models, fields, api

class SaleOrderInherit (models.Model):
    _inherit = 'sale.order'

    res_users_id = fields.Many2one('res.users', string="vendedor 2") 

#este comando serve para procurar os valores registados na table saleorderinherit no terminal

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        print (f"REGISTOS  DO NAME SEARCH{name}" ) 
        res = super(SaleOrderInherit, self).name_search(name, args, operator, limit)
        print(f"REGISTOS RETORNADOS {res}")
        return res


#este comando serve para mostrar os valores registados na table saleorderinherit no terminal
    def name_get(self):
        res = super(SaleOrderInherit, self).name_get()
        print(f"NOME RETORNADOS {res}")
        novos_names = []
        for res_id, name in res:
            name += " - " + self.browse(res_id).partner_id.name #com isso, o programaa vai retornar o pedido de venda associado ao nome do comprador na tela terminal
            novos_names.append((res_id, name)) #com isso, o programaa vai retornar o pedido de venda associado ao nome do comprador na tela da view
           
            
        print(f"NOMES RETORNADOS COM O VENDENDOR {novos_names}")
        return novos_names   


          