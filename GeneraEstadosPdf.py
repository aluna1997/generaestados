# - * - coding: UTF-8 - * -
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pdfkit
from jinja2 import Environment, FileSystemLoader



def generamovs(jsonMovs):
    lista = []

    for i in jsonMovs:
        lista.append(('\n' +'<tr>' + '\n' + '<td>' + str(i["fec_mov_dia"]) + '/' +
            str(i["fec_mov_mes"]) + '/' + str(i["fec_mov_anio"]) + '</td>' + '\n' + 
            '<td>' + str(i["descripcion"]) + '</td>' + '\n' +
            '<td style="text-align:left;">$</td>' + '\n' +
            '<td style="text-align:right; padding-right:105px;">' + str(i["monto"]) + '</td>' + '\n' +
            '</tr>' + '\n'))

    #print ' '.join(lista)
    return ' '.join(lista)


def parsehtml(rutahtml,nombrehtml,diccionario):
    env = Environment(loader=FileSystemLoader(rutahtml))
    template = env.get_template(nombrehtml)
    string = template.render(diccionario)
    return string

def exportopdf(rutacss,html,nombrehtml):
    #path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    #config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

    options = {
        'page-size': 'Letter',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': "UTF-8"
    }

    pdfkit.from_string(html,nombrehtml, options=options, css=rutacss)



def creaprimerapag(jsonPlanes,jsonMovs):

    inicio = parsehtml("formatos","formato_base.html",jsonPlanes)
    medio = parsehtml("formatos","formato_movs.html",{}) + generamovs(jsonMovs[0:17]) + '</table>' + '\n' + '</div>'
    fin = parsehtml("formatos","formato_cierre.html",{"pag": "Página " + str(1)})
    html = inicio + medio + fin

    #print html
    return html


def creanuevapag(jsonMovs,start,topMovs,topPincelMovs,topPag,numPag,topPie):
    inicio = parsehtml("formatos","formato_movs.html",{"top_pincel_movs" : topPincelMovs, 
                                                       "top_movs" : topMovs}) + generamovs(jsonMovs[start:start + 35]) + '</table>' + '\n' + '</div>'
    fin = parsehtml("formatos","formato_cierre.html",{"pag": "Página " + str(numPag), 
                                                      "top_pag" : topPag, 
                                                      "top_pie": topPie})
    html = inicio + fin
    #print html
    return html


def creaultimapag(numPag,topPag,topPie):
    ultima_pag = parsehtml("formatos", "formato_info.html", {"top_escudo_vexi" : topPag,
                                                             "top_call_vexi" : topPag + 250,
                                                             "top_glos_vexi" : topPag + 450,
                                                             "top_prof_vexi" : topPag + 605,
                                                             "top_extra_vexi": topPag + 825})
    ultima_pag = ultima_pag + parsehtml("formatos","formato_cierre.html",{"pag": "Página " + str(numPag),
                                                                          "top_pag" : topPag + 1150,
                                                                          "top_pie" : topPie + 1150})
    return ultima_pag


def generaestados(jsonPlanes,jsonMovs):
    
    # Primera pagina (logo,cuandros generales,17 movimientos y pie de pagina)
    html1 = creaprimerapag(jsonPlanes,jsonMovs)
    longitud = (len(jsonMovs)-17)
    start = 17
    topMovs = 1350
    topPincelMovs = 1325
    topPag = 2540
    numPag = 2
    topPie = 2560
    h = []
    
    while (longitud > 0):
        h.append(creanuevapag(jsonMovs, start, topMovs, topPincelMovs, topPag, numPag, topPie))
        longitud -= 35
        start += 35
        topMovs += 1350
        topPincelMovs += 1350
        topPag += 1300
        numPag += 1
        topPie += 1300
            
    for i in h:
        html1 = html1 + i
    
    html1 = html1 + creaultimapag(numPag, topPag -1150, topPie -1150)

    #print html1 + '  </body>' + '\n' + '<html>'
    return html1 + '  </body>' + '\n' + '<html>'

def generaestadopdf(datos_generales,movimientos):
    estado = generaestados(datos_generales, movimientos)
    exportopdf('/home/falv/vexi_workspace/generaestados/formatos/css/estilos_izq.css',estado,'prueba_estado.pdf')
    
    
if __name__ == '__main__':

    datos = {
            
            'nombre_cte' : 'Juan Pérez',
            'calle_numero' : 'Dr. Díaz Arellano #41',
            'colonia' : '12 de Diciembre',
            'ciudad' : 'CDMX',
            'cp' : '09877',
            'saldo_anterior' : '{:9,.2f}'.format(10000000.45),
            'com_ret_men' :  '{:9,.2f}'.format(200321.31),
            'comisiones_cobr' : '{:9,.2f}'.format(2345.87),
            'intereses' : '{:9,.2f}'.format(235.56),
            'iva' : '{:9,.2f}'.format(23.56),
            'pag_rem_dev' : '{:9,.2f}'.format(2345.67),
            'saldo_al_corte' : '{:9,.2f}'.format(1200.56),
            'saldo_vencido' : '{:9,.2f}'.format(12345.65),
            'saldo_pagos_diferidos' : '{:9,.2f}'.format(12345.65),
            'saldo_total' : '{:9,.2f}'.format(12345.65),
            'saldo_prom_diario' : '{:9,.2f}'.format(12345.65),
            'fec_lim_pago' : '{:9,.2f}'.format(12345.65),
            'pago_min' : '{:9,.2f}'.format(12345.65),
            'pago_para_no_int' : '{:9,.2f}'.format(12345.65),
            'cat' : '91.00 %',
            'tasa_ord_diaria' : '0.18',
            'tasa_ord_anual' : '65',
            'tasa_mor_diaria': '0.28',
            'tasa_mor_anual' : '45.5',
            'tarjeta_fisica' : '547588847485856686',
            'tarjeta_online' : '475888474858566868',
            'rfc' : '5475888HDKD856686'
    }
    
    movimietos = [    {"monto": 376.45, "fec_mov_dia": 15,"fec_mov_mes": "dic", "fec_mov_anio": 2017,
                       "descripcion": "Primero."},
                       
                       
                       
                       
                       
                      {"monto": 10000000.45, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                       "descripcion": "Holi", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
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
                       "descripcion": "Mixup", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                       "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                      {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                       "descripcion": "Mac Store", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                       "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                      {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 15, "fec_mov_anio": 2017,
                       "descripcion": "Su pago... Gracias.", "fec_reg_dia": 18, "orden": 1, "fec_reg_mes": "dic",
                       "fec_mov_mes": "dic", "fec_reg_anio": 2017}
    
                ]
    
    
    
    generaestadopdf(datos, movimietos)
    







