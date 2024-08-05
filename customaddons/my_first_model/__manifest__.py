{
    'name' : 'my first model', #exibe o nome do modulo
    'version' : '1.0', #version do mesmo
    'description' : 'meu primeiro modulo odoo', #description do memo
    'summary': 'teste', #assunto
    "author": 'vasco',
    'depends': ['sale'
        
                ],
    'data' : [
        #o manifest le linha por linha de cima para baixo, ou seja, caso queiras executar um menu.xml (que normalmente is separado) tens que indicar a sequencia de execucao dos files abaixo 
        "security/ir.model.access.csv",
        "views/my_first_view.xml",
        "views/view_herdada.xml",
      
        
    ]
   }