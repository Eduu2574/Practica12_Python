import requests

def obtener_cita():
    try:
        response = requests.get("https://api.quotable.io/random", verify=False)  # Cambiado: verify=False
        if response.status_code == 200:
            cita = response.json()
            print(f'Cita motivacional: "{cita["content"]}" - {cita["author"]}')
        else:
            print(f"Error en la petición. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición HTTP: {e}")