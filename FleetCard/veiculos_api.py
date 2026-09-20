import requests

from django.core.cache import cache

BASE_URL = "https://vpic.nhtsa.dot.gov/api"


def buscar_carros():
    url = f"{BASE_URL}/vehicles/GetModelsForMake/honda?format=json"

    resposta = requests.get(url, timeout=1)

    resposta.raise_for_status()

    dados = resposta.json()

    return dados["Results"][:15]


def buscar_motos():
    url = f"{BASE_URL}/vehicles/GetModelsForMake/honda?format=json"

    resposta = requests.get(url, timeout=1)

    resposta.raise_for_status()

    dados = resposta.json()

    resultados = dados["Results"]

    motos = []

    for veiculo in resultados:
        nome = veiculo["Model_Name"].lower()

        if any(palavra in nome for palavra in [
            "cb",
            "cbr",
            "crf",
            "pcx",
            "shadow",
            "rebel",
            "vfr",
            "vtx",
            "vt",
        ]):
            motos.append(veiculo)

    return motos[:15]


def buscar_caminhoes():
    url = f"{BASE_URL}/vehicles/GetModelsForMake/ford?format=json"

    resposta = requests.get(url, timeout=1)

    resposta.raise_for_status()

    dados = resposta.json()

    resultados = dados["Results"]

    caminhoes = []

    for veiculo in resultados:
        nome = veiculo["Model_Name"].lower()

        if any(palavra in nome for palavra in [
            "f-",
            "f150",
            "f250",
            "f350",
            "f450",
            "f550",
            "super duty",
        ]):
            caminhoes.append(veiculo)

    return caminhoes[:15]


if __name__ == "__main__":

    carros = buscar_carros()
    motos = buscar_motos()
    caminhoes = buscar_caminhoes()

    print("\n🚗 CARROS")
    print(f"Quantidade: {len(carros)}")

    for veiculo in carros:
        print(veiculo["Make_Name"], "-", veiculo["Model_Name"])

    print("\n🏍️ MOTOS")
    print(f"Quantidade: {len(motos)}")

    for veiculo in motos:
        print(veiculo["Make_Name"], "-", veiculo["Model_Name"])

    print("\n🚛 CAMINHÕES")
    print(f"Quantidade: {len(caminhoes)}")

    for veiculo in caminhoes:
        print(veiculo["Make_Name"], "-", veiculo["Model_Name"])



# ==============================
# BUSCAR IMAGEM
# ==============================
def buscar_imagem(marca, modelo, tipo="car"):

    # ==============================
    # DEFINE O TIPO DO VEÍCULO
    # ==============================

    if tipo == "moto":
        termo_busca = f"{marca} {modelo} motorcycle"

    elif tipo == "caminhao":
        termo_busca = f"{marca} {modelo} truck"

    else:
        termo_busca = f"{marca} {modelo} car"


    # ==============================
    # CACHE
    # ==============================

    cache_key = (
        f"imagem_veiculo_{tipo}_{marca}_{modelo}"
        .lower()
        .replace(" ", "_")
    )

    imagem_cache = cache.get(cache_key)

    if imagem_cache:
        return imagem_cache


    # ==============================
    # WIKIMEDIA
    # ==============================

    url = "https://commons.wikimedia.org/w/api.php"

    parametros = {
        "action": "query",
        "generator": "search",
        "gsrsearch": termo_busca,
        "gsrnamespace": 6,
        "gsrlimit": 5,
        "prop": "imageinfo",
        "iiprop": "url",
        "iiurlwidth": 600,
        "format": "json",
    }

    headers = {
        "User-Agent": "FleetCard/1.0 (Projeto Educacional)"
    }


    try:

        resposta = requests.get(
            url,
            params=parametros,
            headers=headers,
            timeout=10
        )

        if resposta.status_code == 429:

            print(
                f"Wikimedia bloqueou temporariamente: "
                f"{termo_busca}"
            )

            return None


        resposta.raise_for_status()

        dados = resposta.json()

        paginas = (
            dados
            .get("query", {})
            .get("pages", {})
        )


        if not paginas:
            print(f"Nenhuma imagem encontrada: {termo_busca}")
            return None


        pagina = next(
            iter(paginas.values())
        )

        imagens = pagina.get(
            "imageinfo",
            []
        )


        if not imagens:
            print(f"Imagem não encontrada: {termo_busca}")
            return None


        imagem = (
            imagens[0].get("thumburl")
            or imagens[0].get("url")
        )


        # ==============================
        # SALVA NO CACHE
        # ==============================

        if imagem:

            cache.set(
                cache_key,
                imagem,
                60 * 60 * 24
            )


        return imagem


    except requests.RequestException as erro:

        print(
            f"Erro ao buscar imagem "
            f"{termo_busca}: {erro}"
        )

        return None