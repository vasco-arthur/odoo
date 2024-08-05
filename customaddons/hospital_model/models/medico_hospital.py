from odoo import models, fields 

class MedicoHospital (models.Model):
    _name = "medico.hospital"
    _description = "info do medico"

    nome = fields.Char(

        string= "Nome",
        size = 150,
        help = "campo para digitar o seu nome, Doutor",
        required=True
         )

    morada = fields.Char(
        string= "Morada",
        size = 1000,
        help = "descreva onde vive ",
        required=True
    )

    contacto = fields.Char(
        string="Mail",
        size = 30,
        required=True
    )

    datacadastro = fields.Date(
        string = "Data de registo",
        default = (fields.Date.today), 
        required=True,
        readonly=True
    )

    sexo = fields.Selection(
        [
         ('1', 'Masculino'),
         ('2', 'Feminino'),
        ],
        string= "Sexo",
        required=True
    )


class PacienteHospital (models.Model):
    _name = "paciente.hospital"
    _description = "insira as info do paciente"

    nome = fields.Char(
        string= "digite o nome do paciente",
        size = 150
    )

    morada = fields.Char(
        string= "informe a sua morada",
        size = 1000,
        help = "descreva onde vive "
    )

    contacto = fields.Char(
        string="insira o seu mail",
        size = 30
    )

    datanas = fields.Date(
        string= "insira a data de nascimento do paciente"

    )
    idade = fields.Integer(
        string="idade do paciente"
    )

    peso = fields.Float(
        string="insira o seu peso",
        digits= (9,2)
    )

    sexo = fields.Selection(
        [
         ('1', 'Masculino'),
         ('2', 'Feminino'),
        ],
        string= "selecionar o sexo do paciente"
    )

    
class Medicamentos (models.Model):
    _name = "medicamentos"
    _description = "info dos medicamentos"

    nome = fields.Char(string="Nome do medicamento")
    dataven = fields.Date(string="Data de vencimento do medicamento")
    fornecedor = fields.Char(string="Fornecedor")
    

class ConsultaHerdade (models.Model):
    _name = "consulta"
    _description = "info das consultas"


    datadaconsulta = fields.Date(
        string= "informe a data da consulta", 
        default= fields.Date.today
        )
