# - * - coding: UTF-8 - * -
import sys

import pdfkit

# Para aceptar acentos y ñ en nuestro pdf es necesario definir la codificacion utf-8
reload(sys)
sys.setdefaultencoding('utf-8')



# La funcion crea el "pedazo" de html de las filas de la tabla movimientos
def generamovs(jsonMovs):
    lista = []

    for i in jsonMovs:
        lista.append((' <tr>' + '\n' + '    <td>' + str(i["fec_mov_dia"]) + '/' +
            str(i["fec_mov_mes"]) + '/' + str(i["fec_mov_anio"]) + '    </td>' + '\n' + '   <td>' +
            str(i["descripcion"]) + '</td>' + '\n' + '   <td>' + '$' +
            str(i["monto"]) + ' </td>' + '\n' + '</tr>' + '\n'))

    return ' '.join(lista)





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
                   "descripcion": "Mac Store", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017},
                  {"monto": -5230.00, "periodo": 0, "id_disputa": 0, "fec_mov_dia": 16, "fec_mov_anio": 2017,
                   "descripcion": "Plaza de la tecnología", "fec_reg_dia": 17, "orden": 2, "fec_reg_mes": "dic",
                   "fec_mov_mes": "dic", "fec_reg_anio": 2017}

                  ]

#print(generamovs(movimietos))


html1 = '<html><head><meta charset="UTF-8"><title>Estado de cuenta</title><link rel="stylesheet" type="text/css" href="css/estilos_izq.css" media="screen" /></head><body><!--===================================== Cuadro movimientos  ==========================================--><div id="pincel_movs"><img src="file:///C:/Users/Falv/PycharmProjects/generaestados/formatos/img/pincel_movs.png" width="845"></div><div  id="movs" style=" position: absolute; top: 620px; font-size: 14px; border: 1.2px solid grey; border-radius: 5px; width:650px; left: 140px; padding-left: 75px;}><table cellspacing="9" align="center"><tr><td style="color:white;"><b>Fecha&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b></td><td style="color:white;"><b>Descripción&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b></td><td style="color:white;"><b>Monto&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</b></td></tr>'


html2 = generamovs(movimietos)

html3 =  '</table></div><!--===================================== Pie de página  ==========================================--><div id="pag"><p>Página 1</p></div><div id="pie_img"><img src="file:///C:/Users/Falv/PycharmProjects/generaestados/formatos/img/pincel2.png" width="1010"></div></body><html>'


html = html1+html2+html3

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

# En windows es necesario especificar la ruta del programa wkhtmltopdf
path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

css = 'formatos\\css\\estilos_izq.css'


#pdfkit.from_string(html,'estado3.pdf', options=options, css=css,configuration=config)

