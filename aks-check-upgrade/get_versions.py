#!/usr/bin/python3
import subprocess
import platform
import os
import sys

# Dicionários para armazenar informações em chave/valor 
components_dict = {}
current_versions = {}
new_versions = {}

def get_kubectl_info():
    # Executa o comando kubectl e capture a saída
    command = "kubectl get all -l boilerplate=component -A --no-headers | grep pod | awk '{print $1\":\"$2}' | awk -F:pod/ '{print $2\":\"$1}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("\n- Componentes do Cluster \n\nNamespace x Pod\n")
    # Verificar se houve algum erro na execução do comando
    if result.returncode != 0:
        print(f"Erro ao executar o comando: {result.stderr}")
        return None

    # Divide as linhas da saída e crie o dicionário
    kubectl_output = result.stdout.strip().split('\n')
    
    for line in kubectl_output:
        key, value = line.split(':')
        components_dict[key] = value
        print(f"{value} --> {key}")
    return components_dict


#Chame a função get_kubectl_info e imprime os pods e namespaces que foram gravados no components_dict
kubectl_info = get_kubectl_info() 
if kubectl_info:
    
    #print(kubectl_info)
    print()

# Função global para procurar pods dentro do dicionário
def find_pod(name):
    for pod, namespace in components_dict.items():
        if pod.startswith(name):
            return pod, namespace
    return None, None


# Pesquisas pelas Current Versions dos componenetes Boilerplate

#=================== TESTE ==============================================

# def get_new_component(component, helm_cmd):
#     if component is not None:
#         command = {helm_cmd}
#         result = subprocess.run(command, shell=True, capture_output=True, text=True)
#         n_component = result.stdout.strip()
#         new_versions[component] = n_component
#         print(f"{component} = {n_component}")
#     else:
#         print("Nenhuma chave encontrada para {component}")






def get_current_component(filtro):
    component_key, component_value = find_pod(name)
    if component_key is not None:
        command = f"kubectl describe pod {component_key} -n {component_value} {filtro}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_component = result.stdout.strip()
        current_versions[component_key] = component_value
        print(f"{name} = {c_component}")
    else:
        print(f"Nenhuma chave encontrada para {name}")


cur_grafana_filtro = f"|grep Image: |grep grafana |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
name = 'grafana'
find_pod(name)
get_current_component(cur_grafana_filtro)

#=====================================================================================
def get_current_grafana():
    grafana_key, grafana_value = find_pod(find_grafana)
    if grafana_key is not None:
        command = f"kubectl describe pod {grafana_key} -n {grafana_value} |grep Image: |grep grafana |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_grafana = result.stdout.strip()
        current_versions["grafana"] = c_grafana
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'grafana'")

# def find_pod(name):
#     for pod, namespace in components_dict.items():
#         if pod.startswith(name):
#             return pod, namespace
#     return None, None

# find_grafana = 'grafana'
# find_pod(find_grafana)
# get_current_grafana()

#=================== monitoring/loki =================================================

def get_current_loki():
    loki_key, loki_value = find_pod(find_loki)
    if loki_key is not None:
        command = f"kubectl describe pod {loki_key} -n {loki_value} |grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_loki = result.stdout.strip()
        current_versions["loki"] = c_loki
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'loki'")

#=================== monitoring/prometheus =============================================

def get_current_prometheus():
    prometheus_key, prometheus_value = find_pod(find_prometheus)
    if prometheus_key is not None:
        command = f"kubectl describe pod {prometheus_key} -n {prometheus_value} |grep Image: |grep prometheus: |awk -Fv '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_prometheus = result.stdout.strip()
        current_versions["prometheus"] = c_prometheus
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'prometheus'")

#=================== service-mesh/istiod =============================================

def get_current_istiod():
    istiod_key, istiod_value = find_pod(find_istiod)
    if istiod_key is not None:
        command = f"kubectl describe pod {istiod_key} -n {istiod_value} |grep Image: |grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_istiod = result.stdout.strip()
        current_versions["istiod"] = c_istiod
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'istiod'")

#=================== service-mesh/istio-ingressgateway ================================

def get_current_istio_ingressgateway():
    istio_ingressgateway_key, istio_ingressgateway_value = find_pod(find_istio_ingressgateway)
    if istio_ingressgateway_key is not None:
        command = f"kubectl describe pod {istio_ingressgateway_key} -n {istio_ingressgateway_value} |grep Image: |grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_istio_ingressgateway = result.stdout.strip()
        current_versions["istio-ingressgateway"] = c_istio_ingressgateway
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'istio-ingressgateway'")

#=================== service-mesh/jaeger ==============================================

def get_current_jaeger():
    jaeger_key, jaeger_value = find_pod(find_jaeger)
    if jaeger_key is not None:
        command = f"kubectl describe pod {jaeger_key} -n {jaeger_value} |grep Image: |grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_jaeger = result.stdout.strip()
        current_versions["jaeger"] = c_jaeger
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'jaeger'")

#=================== service-mesh/jaeger-elasticsearch ==============================================

def get_current_jaeger_elasticsearch():
    jaeger_elasticsearch_key, jaeger_elasticsearch_value = find_pod(find_jaeger_elasticsearch)
    if jaeger_elasticsearch_key is not None:
        command = f"kubectl describe pod {jaeger_elasticsearch_key} -n {jaeger_elasticsearch_value} |grep Image: |grep elasticsearch |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_jaeger_elasticsearch = result.stdout.strip()
        current_versions["jaeger-elasticsearch"] = c_jaeger_elasticsearch
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'jaeger-elasticsearch'")

#=================== service-mesh/kiali =============================================================

def get_current_kiali():
    kiali_key, kiali_value = find_pod(find_kiali)
    if find_kiali is not None:
        command = f"kubectl describe pod {kiali_key} -n {kiali_value} |grep Image: |grep Image: |awk -F:v '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_kiali = result.stdout.strip()
        current_versions["kiali"] = c_kiali
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'kiali'")

#=================== velero/velero =============================================================

def get_current_velero():
    velero_key, velero_value = find_pod(find_velero)
    if find_kiali is not None:
        command = f"kubectl describe pod {velero_key} -n {velero_value} |grep Image: |grep velero |awk -F:v '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_velero = result.stdout.strip()
        current_versions["velero"] = c_velero
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada para 'velero'")

#=================== cert/cert-manager =========================================================

def get_current_cert_manager():
    cert_manager_key, cert_manager_value = find_pod(find_cert_manager)
    if cert_manager_key is not None:
        command = f"kubectl describe pod {cert_manager_key} -n {cert_manager_value} |grep Image: |grep cert-manager |awk '{{print $2}}' |awk -F:v '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_cert_manager = result.stdout.strip()
        current_versions["cert-manager"] = c_cert_manager
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada que começa com 'cert-manager'")

#=================== secrets/sealed-secrets ====================================================

def get_current_sealed_secrets():
    sealed_secrets_key, sealed_secrets_value = find_pod(find_sealed_secrets)
    if sealed_secrets_key is not None:
        command = f"kubectl describe pod {sealed_secrets_key} -n {sealed_secrets_value} |grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_sealed_secrets = result.stdout.strip()
        current_versions["sealed-secrets"] = c_sealed_secrets
        #print(f"Current_versions: {current_versions}")
    else:
        print("Nenhuma chave encontrada que começa com 'sealed-secrets'")

#=============== chamada das funções current-version ================================

# find_grafana = 'grafana'
# find_pod(find_grafana)
# get_current_grafana()

# find_loki = 'loki'
# find_pod(find_loki)
# get_current_loki()

# find_prometheus = 'prometheus'
# find_pod(find_prometheus)
# get_current_prometheus()

# find_istiod = 'istiod'
# find_pod(find_istiod)
# get_current_istiod()

# find_istio_ingressgateway = 'istio-ingressgateway'
# find_pod(find_istio_ingressgateway)
# get_current_istio_ingressgateway()

# find_jaeger = 'jaeger-jaeger-operator'
# find_pod(find_jaeger)
# get_current_jaeger()

# find_jaeger_elasticsearch = 'jaeger-elasticsearch-master-0'
# find_pod(find_jaeger_elasticsearch)
# get_current_jaeger_elasticsearch()

# find_kiali = 'kiali'
# find_pod(find_kiali)
# get_current_kiali()

# find_velero = 'velero'
# find_pod(find_velero)
# get_current_velero()

# find_cert_manager = 'cert-manager'
# find_pod(find_cert_manager)
# get_current_cert_manager()

# find_sealed_secrets = 'sealed-secrets'
# find_pod(find_sealed_secrets)
# get_current_sealed_secrets()

print(f"Componentes e versões rodando hoje neste cluster:\n")
print("\nA buscar versões atualizadas nos repositórios...")
#======================== new-versions ===================================

helm_search_grafana=f"helm search repo grafana/grafana |egrep -v \"NAME|agent\" |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_loki=f"helm search repo grafana/loki |egrep -v \"NAME|-\" |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_prometheus=f"helm search repo prometheus-community/prometheus |grep -v NAME |awk '{{print $3}}' |head -n1 |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"
helm_search_istiod=f"helm search repo istio/istiod |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_istio_ingressgateway=f"helm search repo istio/gateway |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_jaeger=f"helm search repo jaegertracing/jaeger |grep -v NAME |awk '{{print $3}}' |head -n1 |awk -F. '{{print $1\".\"$2}}'"
helm_search_jaeger_elastic=f"helm search repo bitnami/elasticsearch |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_kiali=f"helm search repo kiali/kiali-server |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"
helm_search_velero=f"helm search repo vmware-tanzu/velero |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_cert_manager=f"helm search repo jetstack/cert-manager |grep -v NAME |awk '{{print $3}}' |head -n1 |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"
helm_search_sealed_secrets=f"helm search repo sealed-secrets/sealed-secrets |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"

def get_new_component(component, helm_cmd):
    if component is not None:
        command = {helm_cmd}
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        n_component = result.stdout.strip()
        new_versions[component] = n_component
        print(f"{component} = {n_component}")
    else:
        print("Nenhuma chave encontrada para {component}")

print()

grafana_new = 'grafana'
get_new_component(grafana_new, helm_search_grafana)

# loki_new = 'loki'
# get_new_component(loki_new, helm_search_loki)

# prometheus_new = 'prometheus'
# get_new_component(prometheus_new, helm_search_prometheus)

# istiod_new = 'istiod'
# get_new_component(istiod_new, helm_search_istiod)

# istio_ingressgateway_new = 'istio-ingressgateway'
# get_new_component(istio_ingressgateway_new, helm_search_istio_ingressgateway)

# jaeger_new = 'jaeger'
# get_new_component(jaeger_new, helm_search_jaeger)

# jaeger_elasticsearch_new = 'jaeger-elasticsearch'
# get_new_component(jaeger_elasticsearch_new, helm_search_jaeger_elastic)

# kiali_new = 'kiali'
# get_new_component(kiali_new, helm_search_kiali)

# velero_new = 'velero'
# get_new_component(velero_new, helm_search_velero)

# cert_manager_new = 'cert-manager'
# get_new_component(cert_manager_new, helm_search_cert_manager)

# sealed_secrets_new = 'sealed-secrets'
# get_new_component(sealed_secrets_new, helm_search_sealed_secrets)

#print(f"Novas versões disponiveis para os componentes:\n{new_versions}")

#======================== check-update ===================================
print("\n----------------------------------------------------------\n")

# Função global para procurar pods dentro do dicionário
def find_c_version(name):
    for component, version in current_versions.items():
        if component.startswith(name):
            print(f"{component} ----> current: {version} | new app: {n_grafana}")
            return component, version
    return None, None




# Configurando as variaveis do current-versions e new-versions
# current_versions = 'files/current-versions'
# export_current = configurar_variaveis(current_versions)
# exportar_variaveis(export_current)

# new_versions = 'files/new-versions'
# export_new = configurar_variaveis(new_versions)
# exportar_variaveis(export_new)


with open('files/to-upgrade', 'w') as saida:
    pass

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
                with open('files/to-upgrade', 'a') as saida:
                # Redireciona a saída padrão para o arquivo
                    sys.stdout = saida
                    saida.write(f"{variavel2}\n")
                sys.stdout = sys.__stdout__

                mensagem = f"X - {variavel2}: Need upgrade from version: {valor2_float} to: {valor1_float}"
                print(mensagem)
                
            else:
                print(f"✔ - {variavel2}: It's already updated in latest version: {valor2_float}")
        except ValueError:
            print("Erro ao converter valores para float. Certifique-se de que ambos são numéricos.")
    else:
        print("Uma ou ambas as variáveis não estão configuradas.")

#print("\n\n----------------------------------------------------------\n")
#print("- Checking which application needs upgrade on AKS cluster:\n")


# Comparando as versões dos componentes e mostrando o resultado

#compara_versoes(grafana_new, grafana_current)

# # Comparando as versões dos componentes e mostrando o resultado
# grafana_new = 'n_grafana'
# grafana_current = 'Grafana'
# compara_versoes(grafana_new, grafana_current)

# istio_new = 'n_istio'
# istio_current = 'Istio'
# compara_versoes(istio_new, istio_current)

# jaeger_new = 'n_jaeger'
# jaeger_current = 'Jaeger'
# compara_versoes(jaeger_new, jaeger_current)

# kiali_new = 'n_kiali'
# kiali_current = 'Kiali'
# compara_versoes(kiali_new, kiali_current)

# prometheus_new = 'n_prometheus'
# prometheus_current = 'Prometheus'
# compara_versoes(prometheus_new, prometheus_current)

# loki_new = 'n_loki'
# loki_current = 'Loki'
# compara_versoes(loki_new, loki_current)

# velero_new = 'n_velero'
# velero_current = 'Velero'
# compara_versoes(velero_new, velero_current)

# cert_manager_new = 'n_cert_manager'
# cert_manager_current = 'Cert_manager'
# compara_versoes(cert_manager_new, cert_manager_current)

# sealed_secrets_new = 'n_sealed_secrets'
# sealed_secrets_current = 'Sealed_secrets'
# compara_versoes(sealed_secrets_new, sealed_secrets_current)

#print("\n----------------------------------------------------------")