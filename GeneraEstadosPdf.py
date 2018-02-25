# - * - coding: UTF-8 - * -
import sys

import pdfkit
from jinja2 import Environment, FileSystemLoader

reload(sys)
sys.setdefaultencoding('utf-8')


def generamovs(jsonMovs):
    lista = []

    for i in jsonMovs:
        lista.append((' <tr>' + '\n' + '    <td>' + str(i["fec_mov_dia"]) + '/' +
            str(i["fec_mov_mes"]) + '/' + str(i["fec_mov_anio"]) + '    </td>' + '\n' + '   <td>' +
            str(i["descripcion"]) + '</td>' + '\n' + '   <td>' + '$' +
            str(i["monto"]) + ' </td>' + '\n' + '</tr>' + '\n'))

    return ' '.join(lista)


def parsehtml(rutahtml,nombrehtml,diccionario):
    env = Environment(loader=FileSystemLoader(rutahtml))
    template = env.get_template(nombrehtml)
    string = template.render(diccionario)
    return string

def exportopdf(rutacss,html,nombrehtml):
    path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': "UTF-8"
    }

    pdfkit.from_string(html,nombrehtml, options=options, css=rutacss,configuration=config)



def creaprimerapag(jsonPlanes,jsonMovs):

    inicio = parsehtml("formatos","formato_base.html",jsonPlanes)
    medio = parsehtml("formatos","formato_movs.html",{}) + generamovs(jsonMovs[0:17]) + '</table>' + '\n' + '</div>'
    fin = parsehtml("formatos","formato_cierre.html",{"pag": "Página " + str(1)})
    html = inicio + medio + fin

    return html


def creanuevapag(jsonMovs,start,topMovs,topPincelMovs,topPag,numPag,topPie):
    inicio = parsehtml("formatos","formato_movs.html",{"top_pincel_movs" : topPincelMovs, "top_movs" : topMovs}) + generamovs(jsonMovs[start:start+35]) + '</table>' + '\n' + '</div>'
    fin = parsehtml("formatos","formato_cierre.html",{"pag": "Página " + str(numPag), "top_pag" : topPag, "top_pie": topPie})
    html = inicio + fin
    return html



def generaestados(jsonPlanes,jsonMovs):
    html1 = creaprimerapag(jsonPlanes,jsonMovs)
    h = []
    longitud = len(jsonMovs)-17
    start =17
    topMovs = 1400
    topPincelMovs = 1370
    topPag = 2540
    numPag=2
    topPie = 2560
    while(longitud > 0):
        h.append(creanuevapag(jsonMovs,start,topMovs,topPincelMovs,topPag,numPag,topPie))
        numPag+=1
        start+=35
        longitud-=35
        topMovs+=1300
        topPincelMovs+=1308
        topPag+=1300
        topPie+=1308

    for i in h:
        html1 = html1 + i

    #print(html1 + '  </body>' + '\n' + '<html>')
    return html1 + '  </body>' + '\n' + '<html>'



datos = {

        'nombre' : 'Juan Pérez',
        'calle_numero' : 'Dr. Díaz Arellano #41',
        'colonia' : '12 de Diciembre',
        'ciudad' : 'CDMX',
        'cp' : '09877',
        'saldo_anterior' : 1500.56,
        'com_ret_men' :  200321.31,
        'comisiones_cobr' : 2345.87,
        'intereses' : 235.56,
        'iva' : 23.56,
        'pag_rem_dev' : 2345.67,
        'al_corte' : 1200.56,
        'pagos_diferidos' : 12345.65,
        'total' : 12345.65
}

movimietos = [    {"monto": 376.45, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 15, "fec_mov_anio": 2017,
                   "descripcion": "Primero.", "fec_reg_dia": 18, "orden": 1, "fec_reg_mes": "dic",
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
                   "descripcion": "Ultimo", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017}

                  ]

s = 1500.56
print('{:9,.2f}'.format(s))



estado = generaestados(datos,movimietos)
#estado = creaprimerapag(datos,movimietos)[0] + '  </body>' + '\n' + '<html>'
exportopdf('formatos\\css\\estilos_izq.css',estado,'prueba24.pdf')







