import requests
import csv

# Funcao para obeter a lista de itnes para um determinado tipo de produto
def obtener_lista_items(termino_busqueda):
    url = f"https://api.mercadolibre.com/sites/MLA/search"
    params = {
        'q': termino_busqueda
        
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Time da chamada
        
        # Retorno do resultado em Json
        resultados = response.json()
        
        # Extracao dos itens mediante ao resultado
        item_ids = [item['id'] for item in resultados['results']]
        
        return item_ids
    
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud para {termino_busqueda}: {e}")
        return None

# Definição dos itens a serem buscados
terminos_de_busqueda = ["Google Home", "Apple TV", "Amazon Fire TV", "chromecast"]

# Armazenamentos ites retornados
items_por_termino = {}

# Obter os ids retorandos 
for termino in terminos_de_busqueda:
    item_ids = obtener_lista_items(termino)
    if item_ids:
        items_por_termino[termino] = item_ids


detalles_items = []

# Função para obter os detalhes de um item de acordo com seu ID
def obtener_detalles_item(item_ids):
    url = f"https://api.mercadolibre.com/items/{item_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lançar uma exceção se a solicitação falhar

        detalles_producto = response.json()
        return detalles_producto

    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud para el item {item_id}: {e}")
        return None

for termino, item_ids in items_por_termino.items():
    for item_id in item_ids:
        detalles_item = obtener_detalles_item(item_id)
        if detalles_item:
            # Adicione variáveis relevantes ao dicionário
            detalle = {
                'Término de Búsqueda': termino,
                'Item ID': detalles_item['id'],
                'Título': detalles_item['title'],
                'Preco': detalles_item['price'],
                'Condicao': detalles_item['condition'],
                ##'Vendidos': detalles_item['sold_quantity']
                # Adicione mais campos conforme necessário
            }
            detalles_items.append(detalle)


nombre_archivo = 'detalles_items_mla.csv'

# Cabeçalhos para arquivo CSV
cabeceras = ['Término de Búsqueda', 'Item ID', 'Título', 'Preco', 'Condicao']

# Gravar detalhes do item em arquivo CSV
with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.DictWriter(archivo_csv, fieldnames=cabeceras)
    writer.writeheader()
    writer.writerows(detalles_items)

print(f"Archivo CSV guardado exitosamente: {nombre_archivo}")