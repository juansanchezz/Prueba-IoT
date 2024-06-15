import json
import requests

def datos_obtenidos ():
    huella = 13458985632521
    dni = 1069759181
    datos = {"huella","dni"}
    return datos
#aca simulo la direccion donde enviaria la data mediante HTTP
cloud_url = "https://httpbin.org/post"

def envio_datos():
    if datos_obtenidos > 0:
        envio_data = datos_obtenidos()
        #print(envio_data)
        payload = json.dumps(envio_data)

        try: 
            response = request.post(cloud_url,data=payload, headers={'Content-Type':'application/json'})
        except ValueError:
            print("oops habido un problema")
        