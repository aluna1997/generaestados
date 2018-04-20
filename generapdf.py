# - * - coding: UTF-8 - * -
import sys

import pdfkit
from jinja2 import Environment, FileSystemLoader


def generamovs(jsonMovs):
    lista = []

    for i in jsonMovs:
        lista.append((' <tr>' + '\n' + '    <td>' + str(i["fec_mov_dia"]) + '/' +
            str(i["fec_mov_mes"]) + '/' + str(i["fec_mov_anio"]) + '    </td>' + '\n' + '   <td>' +
            str(i["descripcion"]) + '</td>' + '\n' + '   <td>' + '$' +
            str(i["monto"]) + ' </td>' + '\n' + '</tr>' + '\n'))

    return ' '.join(lista)






'''
def generamovs(jsonMovs):
    lista = []
    env = Environment(loader=FileSystemLoader("formatos"))
    template_movs = env.get_template("formato_movs.html")

    if(len(jsonMovs) <= 17):

        top = {'top_pincel_movs' : 590,'top_movs' : 620}
        html_movs = template_movs.render(top)

        for i in jsonMovs:
            lista.append((' <tr>' + '\n' + '    <td>' + str(i["fec_mov_dia"]) + '/' +
                str(i["fec_mov_mes"]) + '/' + str(i["fec_mov_anio"]) + '    </td>' + '\n' + '   <td>' +
                str(i["descripcion"]) + '</td>' + '\n' + '   <td>' + '$' +
                str(i["monto"]) + ' </td>' + '\n' + '</tr>' + '\n'))

        return html_movs + ' '.join(lista) + '</table>'

'''





reload(sys)
sys.setdefaultencoding('utf-8')

#path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
#config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

# Creamos un entorno
env = Environment(loader=FileSystemLoader("formatos"))

# Tomamos el primer "pedazo" de html
template_inicio = env.get_template("formato_base.html")

datos = {

        'nombre' : 'Juan Pérez',
        'calle_numero' : 'Dr. Díaz Arellano #41',
        'colonia' : '12 de Diciembre',
        'ciudad' : 'CDMX',
        'cp' : '09877'
}

inicio = template_inicio.render(datos)


# El "pedazo" de en medio será la tabla de movimientos

movimietos = [    {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 15, "fec_mov_anio": 2017,
                   "descripcion": "Su pago... Gracias.", "fec_reg_dia": 18, "orden": 1, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Suburbia", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Mixup", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Mac Store", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Plaza de la tecnología", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 15, "fec_mov_anio": 2017,
                   "descripcion": "Su pago... Gracias.", "fec_reg_dia": 18, "orden": 1, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Suburbia", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Mixup", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Mac Store", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Plaza de la tecnología", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 15, "fec_mov_anio": 2017,
                   "descripcion": "Su pago... Gracias.", "fec_reg_dia": 18, "orden": 1, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Suburbia", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Mixup", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Mac Store", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017}

                  ]


medio = generamovs(movimietos)

#print(medio)



# Tomamos el ultimo "pedazo" de html
template_fin = env.get_template("formato_cierre.html")
pag = {'pag' : 'Página 1'}
fin = template_fin.render(pag)



#El html completo entonces será
html = inicio + medio + fin

print html




# Estas son las confiuraciones del pdf, donde damos un margen muy pequeño y
# la codificacion utf-8
options = {

    'page-size': 'Letter',
    'margin-top': '0.05in',
    'margin-right': '0.05in',
    'margin-bottom': '0.05in',
    'margin-left': '0.05in',
    'encoding': "UTF-8"
}



pdfkit.from_string(html,'estado.pdf', options=options)





