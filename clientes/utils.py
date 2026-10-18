import requests


def buscar_personagem_dbz(nome):
    """
    Busca dados do personagem na Dragon Ball API pelo nome.
    """

    url = f'https://dragonball-api.com/api/characters?name={nome}'

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, list) and len(data) > 0:
                # Retorna o primeiro personagem encontrado
                return data[0]

    except Exception as e:
        print(f"Erro ao consultar Dragon Ball API: {e}")

    return None