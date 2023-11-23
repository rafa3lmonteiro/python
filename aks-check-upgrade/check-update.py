#!/usr/bin/python3
# Rafael Monteiro - Nov/2023

import os

def configurar_variaveis(nome_arquivo):
    variaveis = {}

    # Abrir o arquivo em modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(':')

            chave = chave.strip()
            valor = valor.strip()

            variaveis[chave] = valor

    return variaveis

def exportar_variaveis(variaveis):

    sistema_operacional = os.name

    # Exportar variáveis para sistemas baseados em Unix/Linux
    if sistema_operacional == 'posix':
        for chave, valor in variaveis.items():
            os.environ[chave] = valor

    # Sistemas Windows
    elif sistema_operacional == 'nt':
        for chave, valor in variaveis.items():
            os.environ[chave] = valor
            os.system(f'set {chave}={valor}')

    else:
        print("Sistema operacional não suportado.")

# Configurando as variaveis do current-versions e new-versions
current_versions = 'files/current-versions'
export_current = configurar_variaveis(current_versions)
exportar_variaveis(export_current)

new_versions = 'files/new-versions'
export_new = configurar_variaveis(new_versions)
exportar_variaveis(export_new)

# Lista de variáveis - current versions e new versions
lista_variaveis = ['Grafana', 'Istio', 'Jaeger', 'Kiali', 'Prometheus', 'Loki', 'Velero', 'Cert_manager', 'Sealed_secrets', \
                   'n_grafana', 'n_istio', 'n_jaeger', 'n_kiali', 'n_prometheus', 'n_loki', 'n_velero', 'n_cert_manager', 'n_sealed_secrets']

def compara_versoes(variavel1, variavel2):
    """
    Compara os valores das duas versões.

    Args:
        variavel1 (str): Nome da primeira variável.
        variavel2 (str): Nome da segunda variável.
    """
    valor1 = os.environ.get(variavel1)
    valor2 = os.environ.get(variavel2)

    if valor1 is not None and valor2 is not None:
        try:
            valor1_float = float(valor1)
            valor2_float = float(valor2)

            if valor1_float > valor2_float:
                print(f"X - {variavel2}: Need upgrade from version: {valor2_float} to: {valor1_float}")
            else:
                print(f"✔ - {variavel2}: It's already updated in latest version: {valor2_float}")
        except ValueError:
            print("Erro ao converter valores para float. Certifique-se de que ambos são numéricos.")
    else:
        print("Uma ou ambas as variáveis não estão configuradas.")

print("\n\n----------------------------------------------------------\n")
print("- Checking which application needs upgrade on AKS cluster:\n")

# Comparando as versões dos componentes e mostrando o resultado
grafana_new = 'n_grafana'
grafana_current = 'Grafana'
compara_versoes(grafana_new, grafana_current)

istio_new = 'n_istio'
istio_current = 'Istio'
compara_versoes(istio_new, istio_current)

jaeger_new = 'n_jaeger'
jaeger_current = 'Jaeger'
compara_versoes(jaeger_new, jaeger_current)

kiali_new = 'n_kiali'
kiali_current = 'Kiali'
compara_versoes(kiali_new, kiali_current)

prometheus_new = 'n_prometheus'
prometheus_current = 'Prometheus'
compara_versoes(prometheus_new, prometheus_current)

loki_new = 'n_loki'
loki_current = 'Loki'
compara_versoes(loki_new, loki_current)

velero_new = 'n_velero'
velero_current = 'Velero'
compara_versoes(velero_new, velero_current)

cert_manager_new = 'n_cert_manager'
cert_manager_current = 'Cert_manager'
compara_versoes(cert_manager_new, cert_manager_current)

sealed_secrets_new = 'n_sealed_secrets'
sealed_secrets_current = 'Sealed_secrets'
compara_versoes(sealed_secrets_new, sealed_secrets_current)

print("\n----------------------------------------------------------")