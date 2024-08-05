
# Aqui utilizamos recurso a biblioteca INFLACT que permite converter numero por compreensao para para extenso 
# E a biblioteca DEE_TRANSLATOR que utilizando o GOOGLETRANSLATOR realiza a traducao de um idioma para outro
import inflect
from deep_translator import GoogleTranslator # Esta biblioteca pode depender de uma conexão com a internet estável
def tudo_dentro(texto):
        
    def converter_numero_por_extenso(numero):
        p = inflect.engine()
        return p.number_to_words(numero)

    frase = None

    

    # Verifica se o texto contém "USD" para dólares ou "Kz" para kwanzas. Apenas aceita duas opções
    # Neste trecho de codigo pode se adicionar mais moedas seguindo o mesmo padrao

    
    if "USD" in texto.upper():
        moeda = "Dólares"
        texto = texto.upper().replace("USD", "").strip()
    elif "KZ" or "Kz" or "kz" or "kZ"in texto.upper() or "AOA" in texto.upper():
        moeda = "Kwanzas"
        texto = texto.upper().replace("KZ", "").replace("AOA", "").strip()
    else:
        moeda = None

    # Verifica se o numero digitado está composto por pontos e virgula

    texto = texto.replace('.', '').replace(',', '.')

    # Estamos a verificar se a string resultante é um número válido
    if all(caractere.isdigit() or caractere == '.' for caractere in texto):

        # Converte para um número de ponto flutuante
        numero = float(texto)

        # Estamos a separar a parte inteira e a parte decimal
        parte_inteira = int(numero)
        parte_decimal = int(round((numero - parte_inteira) * 100))

        # Faz a conversão da parte inteira e a parte decimal em palavras por extenso
        parte_inteira_extenso = converter_numero_por_extenso(parte_inteira)
        parte_decimal_extenso = converter_numero_por_extenso(parte_decimal)

        # Utiliza a biblioteca deep_translator e traduz para o português 
        translator = GoogleTranslator(source='en', target='pt')
        parte_inteira_traduzida = translator.translate(parte_inteira_extenso)
        parte_decimal_traduzida = translator.translate(parte_decimal_extenso)

        # Monta a frase completa (parte intira e decimal)
        frase = f"{parte_inteira_traduzida} {moeda}"
        if parte_decimal > 0:
            frase += f" e {parte_decimal_traduzida} céntimos"
            
        #print(type(texto),' TIPO DE TEXTO DE SAIDA')
        return frase
    
        
    else:
        #print(type(texto),' TIPO DE TEXTO DE SAIDA')
        return frase



  