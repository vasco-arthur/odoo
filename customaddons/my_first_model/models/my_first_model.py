from odoo import models, fields, api
from odoo.exceptions import ValidationError 
from . import convert

class MyFirstModel (models.Model): #o (models.Model) faz com que o "Model" tenha acesso a base de dados
    _name = 'my.first.model' #obrigatorio ter ponto
    _description = 'este is my first model on odoo, by odoo curse brazilian'
    

#code para que add uma condicao de n aceitar numero inteiro negativo 
    @api.constrains("int2") 
    def _check_camp_int(self):
           for record in self:
                  if record.int2 < 0:
                         raise ValidationError(message="o campo inteiro n funciona com number negative")


    int2 = fields.Integer(
           string="Numero inteiro"
                       )         

    Camp_Inteiro = fields.Integer(
        string="campo_inteiro",
        default = 0,
        help="campo para digitar numeros inteiro",
        compute="_compute_var",
        store=True #com isso o mambo salva no mambo
        ) 


    @api.model_create_multi  #cria e atualiza multiplos registos ao mesmo tempo
    def create (self, val_list):
           print(f" REGISTRAR {val_list}")
           res = super(MyFirstModel, self).create(val_list)

           print (f"REGISTOS  {res}" ) 

           return res
    
    def write(self, val_list):
           print(f"ATUALIZAR REGISTOS")
           res = super(MyFirstModel, self).write(val_list)
           print(f"REGISTOS ATUALIZADOS {res}")
           return res
            
    #campos compute, n sao salvos na bd
    #PESQUISAR MAIS SOBRE COMPUTAR VALORES EM CAMPOS NO ODOO
  #  @api.depends("Camp_one2many_id") 
    def _compute_var (self):

                    for record in self:

                        print("BUMBOU")

                        record.Camp_Inteiro += 1 


        
    Camp_Bool = fields.Boolean(
        string = "campo bool",
        help = "campo booleano que tem apenas 2 values (true/fale)",
        readonly= False
    )

    Camp_Float = fields.Float(
        string= "price",
        digits= (9, 2)

    )


    def valorP (self):
            
            return "valoratualizado"
    
    Camp_char = fields.Char(
        string= "Nome",
        size = 100,
        index = True,
        translate = True,
        help = "campo para nome, mails, senhas,",
        default=valorP
    )

    Camp_TXT = fields.Text(
        string = "description",
        help = "campo para textos grandes"
    )

    Camp_Select = fields.Selection([
         ('ativo', 'Ativo'),
         ('inativo', 'inativo')
        ],
        string= "selecionar"
        
    )

#este comando faz com que mostre um dado associado a outro dado/tabela, ex.: o campo partner_id is o cliente, e o campo camp_many2one_id (ambos referenciados)
#por outra table, ent, o code abaixo, faz com que mostre o cliente associado ao pedido de venda requisitado 
    @api.onchange('Camp_Many2one_id')
    def _onchange_partner_id(self):
        for record in self:
               record.partner_id = record.Camp_Many2one_id.partner_id

    partner_id = fields.Many2one(
           'res.partner',
           string="Cliente"
    )


    Camp_Many2one_id = fields.Many2one(
        'sale.order',
        string= "registo",
        #ondelete = 'cascade', apaga os registos do campo e suas relacoes
        #ondelete = 'set null', apaga os registos do campo e mantem as relacoes
        #ondelete = 'restric', impede o user de dropar o registo
        #ondelete = 'no action', n faz p#rra nenhuma e impede a navegation
        help = "campo que vai servir de chave estangeira para relacionar 2 tables ",

        #domain = ([('cliente','=' , 'vasco')]) filtro de search que isn't muito used
    )

        #is a good pratice create a 3rd table to work w/ many to many
        #normally they junta a T1 e a T2 and finshed by _rel (table1_table2_rel)
    Camp_many2many = fields.Many2many(
        'res.country',
        string= "campo de muitos para muitos"
        
    )

        #normalmente esse campo is used to show dados em linha/tabelas (por isso ele anda sempre acompanhado de uma outra table)
    Camp_one2many_ids = fields.One2many(
          #ethis  nigga referencia o campo e a tabela
        'res.country', 'currency_id',
        string= "campo de 1 para muitos" # it's que aparece no screen 

        #this nigga don't stay on table my first model, because he's offer he's fk to the other table
    )

    datai = fields.Datetime(
         string="data inicial",
         required="True"

   )
    dataf = fields.Datetime(
         string="data final",
         required="True"

   )

  #  class LinkOneToManyLine (models.Model):
  #          _name='link.one.to.many.line',
        
   #         nome = fields.Char(string= 'nome')

    #        camp_many2onelinklinha_id = fields.Many2one('my.first.model', string= 'campo de linkar as linhas')
    
    
class my_second_model(models.Model):
    _name ="my.second.model"
    _description = "novo modulo" 


    valorRecebido = fields.Char (
        string= "Digite o valor",
        
    )

    valorex = fields.Char(
        string=" valor por extenso",
        compute="_mostrarValor",
        #store="True"
    )

 
    # @api.depends("valorex") 
    # def _mostrarValor(self):
    #        for record in self:
         
    #               record.valorex = record.valorRecebido * 5

    @api.depends("valorRecebido")
    def _mostrarValor (self):
           
           for record in self:
            
            valorTotal = str (record.valorRecebido)
            record.valorex = convert.tudo_dentro(valorTotal)

           
   
# class modelo_tarefas(models.Model):
#     _name = "modelo.tarefas"
#     _description = "Modelo de tarefas"

#     valor_compreensao = fields.Char(
#         string="Valor"
#         )
#     valor_extensao = fields.Char(
#         string="Extensao",
#         compute="coversao_de_valor"
#         )

#     @api.depends("valor_compreensao")
#     def coversao_de_valor(self):
       
#         for record in self:

#             valorExtenso = str (record.valor_compreensao)
#             record.valor_extensao = exercicio1.tudo_dentro(valorExtenso)
            

        