import pandas as pd
import numpy as np
import zipfile
import os

class Municipio:
    def __init__(self, nome, uf, codigo):
        self.nome = nome
        self.uf = uf
        self.codigo = codigo

class Distancia:
    def __init__(self, org, dest, km_linear, km_rota):
        self.org = org
        self.dest = dest
        self.km_linear = km_linear
        self.km_rota = km_rota

class Hub:
    def __init__(self, nome, cod_inicial, cod_final, capacidade_entrega):
        self.nome = nome
        self.cod_inicial = cod_inicial
        self.cod_final = cod_final
        self.capacidade_entrega = capacidade_entrega

class Pedido:
    def __init__(self, id_pedido, cod_org, cod_dest):
        self.id_pedido = id_pedido
        self.cod_org = cod_org
        self.cod_dest = cod_dest
        self.processado = False

def main():
    # Listar todos os arquivos de pedidos no diretório "dados"
    arquivos_pedidos = []
    for nome_arquivo in os.listdir("dados"):
        if nome_arquivo.endswith(".csv"):
            arquivos_pedidos.append(os.path.join("dados", nome_arquivo))

    # Ler municípios
    municipios = pd.read_excel("dados/municipios.csv")
    municipios = [Municipio(row["Município - UF"], row["COD mun"]) for _, row in municipios.iterrows()]

    # Ler distâncias
    distancias = pd.read_excel("dados/distancias.csv")
    distancias = [Distancia(row["org"], row["dest"], row["km_linear"], row["km_rota"]) for _, row in distancias.iterrows()]

    # Ler hubs
    hubs = pd.read_excel("dados/hubs.csv")
    hubs = [Hub(row["Nome HUB"], row["COD inicial"], row["COD final"], row["Capacidade Entrega"]) for _, row in hubs.iterrows()]

    # Processar cada arquivo de pedidos individualmente
    for arquivo_pedidos in arquivos_pedidos:
        # Ler pedidos do arquivo
        pedidos = pd.read_excel(arquivo_pedidos, engine='openpyxl')
        pedidos = [Pedido(row["Id Pedido"], row["COD org"], row["COD dest"]) for _, row in pedidos.iterrows()]

        # Processar cada hub
        resultados_hub = []
        for hub in hubs:
            pedidos_alocados = [p for p in pedidos if p.cod_org == hub.cod_inicial]
            pedidos_redirecionados_recebidos = [p for p in pedidos if hub.cod_inicial < p.cod_org < hub.cod_final and not p.processado]
            pedidos_redirecionados_enviados = [p for p in pedidos if p.cod_dest < hub.cod_inicial and not p.processado]
            pedidos_nao_entregues = [p for p in pedidos if p not in pedidos_alocados and p not in pedidos_redirecionados_recebidos and p not in pedidos_redirecionados_enviados and not p.processado]

            total_pedidos_alocados = len(pedidos_alocados)
            total_pedidos_redirecionados_recebidos = len(pedidos_redirecionados_recebidos)
            total_pedidos_redirecionados_enviados = len(pedidos_redirecionados_enviados)
            total_pedidos_nao_entregues = len(pedidos_nao_entregues)

            # Calcular distância total da frota
            distancia_total = 0
            for p in pedidos_alocados:
                distancia = next((d.km_rota for d in distancias if d.org == p.cod_org and d.dest == p.cod_dest), None)
                if distancia is None:
                    distancia = next((d.km_rota for d in distancias if d.org == p.cod_org and d.dest == hub.cod_final), None) + next((d.km_rota for d in distancias if d.org == hub.cod_final and d.dest == p.cod_dest), None)
                distancia_total += distancia * 2

            # Calcular total de dias de entrega
            dias_entrega = np.ceil((total_pedidos_alocados + total_pedidos_redirecionados_recebidos) / hub.capacidade_entrega)

                        # Salvar resultados do hub
            resultados_hub.append({
                "Nome HUB": hub.nome,
                "Total de Pedidos Alocados": total_pedidos_alocados,
                "Total de Pedidos Redirecionados Recebidos": total_pedidos_redirecionados_recebidos,
                "Total de Pedidos Redirecionados Enviados": total_pedidos_redirecionados_enviados,
                "Total de Pedidos Não Entregues": total_pedidos_nao_entregues,
                "Total de dias de entrega": dias_entrega,
                "Distância total da frota": distancia_total
            })

            # Marcar pedidos como processados
            for p in pedidos_alocados + pedidos_redirecionados_recebidos + pedidos_redirecionados_enviados + pedidos_nao_entregues:
                p.processado = True

            # Salvar resultados em arquivo csv
            nome_arquivo_saida = os.path.splitext(os.path.basename(arquivo_pedidos))[0] + "_resultados.csv"
            with open(os.path.join("dados", nome_arquivo_saida), mode="w", encoding="cp1252", newline="") as arquivo_saida:
                escritor_csv = csv.DictWriter(arquivo_saida, fieldnames=resultados_hub[0].keys(), delimiter=";")
                escritor_csv.writeheader()
                escritor_csv.writerows(resultados_hub)

if __name__ == "__main__":
    main()
           
