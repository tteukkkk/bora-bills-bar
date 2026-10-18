import requests
from django.shortcuts import render
import random
from api.utils import previsao_tempo, obter_lat_lon_por_cidade

def home(request):
    cidade = request.GET.get(
        'cidade',
        'São Paulo'
    )

    latitude, longitude = (
        obter_lat_lon_por_cidade(cidade)
        if cidade
        else (-23.5505, -46.6333)
    )

    clima = None

    if latitude is not None and longitude is not None:
        weather = previsao_tempo(
            latitude,
            longitude
        )

        if weather:
            temp = weather.get('temperature')
            wind = weather.get('windspeed')
            weathercode = weather.get('weathercode')

            descricao = {
                0: "céu limpo ☀️",
                1: "principalmente limpo ⛅",
                2: "parcialmente nublado 🌤️",
                3: "nublado ☁️",
                45: "neblina 🌫️",
                48: "gelo/neblina ❄️",
                51: "chuvisco leve 🌦️",
                53: "chuvisco moderado 🌦️",
                55: "chuvisco denso 🌧️",
                61: "chuva leve 🌧️",
                63: "chuva moderada 🌧️",
                65: "chuva intensa ⛈️",
                80: "aguaceiro leve 🌦️",
                81: "aguaceiro moderado 🌧️",
                82: "aguaceiro forte ⛈️",
            }.get(
                weathercode,
                "indefinido"
            )

            clima = (
                f"{descricao}, "
                f"{temp}°C, "
                f"vento {wind} km/h"
            )
        else:
            clima = "Não foi possível obter a previsão do tempo."
    else:
        clima = "Cidade não encontrada."

    return render(
        request,
        'menu/home.html',
        {
            'clima': clima,
            'cidade': cidade,
        }
    )

def cardapio(request):
    # Pega o termo digitado na URL (?busca=...)
    busca = request.GET.get('busca', '')

    drinks = []

    if busca:
        url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={busca}'

        data = _get_json(url) or {}

        drinks = data.get('drinks', [])

    range_ingredientes = [str(i) for i in range(1, 16)]  # 1 a 15

    return render(
        request,
        'menu/cardapio.html',
        {
            'drinks': drinks,
            'range_ingredientes': range_ingredientes,
            'busca': busca,
            'buscou': bool(busca),  # define se o usuário buscou algo
        }
    )
    
def curiosidade(request):
    busca = request.GET.get('busca', '').strip()

    personagem = None
    curiosidade = None

    # Buscar personagens pela API
    url = 'https://dragonball-api.com/api/characters'
    params = {'limit': 150}

    data = _get_json(url, params=params) or {'items': []}

    lista_personagens = (
        data['items']
        if isinstance(data, dict) and 'items' in data
        else data
    )

    if busca:
        # Busca pelo nome do personagem
        personagem = next(
            (
                p for p in lista_personagens
                if busca.lower() in p['name'].lower()
            ),
            None
        )
    elif lista_personagens:
        personagem = random.choice(lista_personagens)

    if personagem:
        curiosidades = []

        if personagem.get('race'):
            curiosidades.append(
                f"Raça: {personagem['race']}"
            )

        if personagem.get('originPlanet'):
            curiosidades.append(
                f"Planeta de origem: {personagem['originPlanet']}"
            )

        if personagem.get('gender'):
            curiosidades.append(
                f"Gênero: {personagem['gender']}"
            )

        if personagem.get('ki'):
            curiosidades.append(
                f"Ki: {personagem['ki']}"
            )

        if personagem.get('affiliation'):
            curiosidades.append(
                f"Afiliação: {personagem['affiliation']}"
            )

        if personagem.get('saga'):
            curiosidades.append(
                f"Saga(s): {', '.join(personagem['saga']) if personagem.get('saga') else '-'}"
            )

        if personagem.get('transformation'):
            curiosidades.append(
                f"Transformações: {', '.join(personagem['transformation']) if personagem.get('transformation') else '-'}"
            )

        curiosidade = (
            random.choice(curiosidades)
            if curiosidades
            else "Este personagem é um mistério até para o Bills!"
        )

    return render(
        request,
        'menu/curiosidades.html',
        {
            'personagem': personagem,
            'curiosidade': curiosidade,
            'busca': busca,
        }
    )

def _get_json(url, **kwargs):
    try:
        response = requests.get(url, timeout=7, **kwargs)
        response.raise_for_status()
        data = response.json()
        return data if isinstance(data, dict) else None
    except (requests.RequestException, ValueError):
        return None
