# Rafael Monteiro
# Dezembro/2023
#!/usr/bin/python3
import subprocess


# Dicionários para armazenar as informações em chave/valor 
components_dict = {}
current_versions = {}
new_versions = {}

# Função para buscar os componentes com a Label projeto=component no cluster AKS
def get_kubectl_info():

    command = "kubectl get all -l projeto=component -A --no-headers | grep pod | awk '{print $1\":\"$2}' | awk -F:pod/ '{print $2\":\"$1}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("\n- Componentes Projeto \n\nNamespace x Pod\n")

    if result.returncode != 0:
        print(f"Erro ao executar o comando: {result.stderr}")
        return None

    kubectl_output = result.stdout.strip().split('\n')
    
    for line in kubectl_output:
        key, value = line.split(':')
        components_dict[key] = value
        print(f"{value} --> {key}")
    return components_dict

get_kubectl_info() 

# Função para procurar pods dentro do dicionário components_dict
def find_pod(name):
    for pod, namespace in components_dict.items():
        if pod.startswith(name):
            return pod, namespace
    return None, None

# Função para pesquisas de Current Versions dos componenetes Projeto
def get_current_component(filtro):
    component_key, component_value = find_pod(name)
    if component_key is not None:
        command = f"kubectl describe pod {component_key} -n {component_value} {filtro}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        c_component = result.stdout.strip()
        current_versions[name] = c_component
        print(f"{name} = {c_component}")
    else:
        print(f"Nenhuma chave encontrada para {name}")


print(f"\n- Componentes e versões rodando hoje neste cluster:\n")

# Chamada das funções Current-versions 

cur_grafana_filtro=f"|grep Image: |grep grafana |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
name = 'grafana'
find_pod(name)
get_current_component(cur_grafana_filtro)

cur_loki_filtro=f"|grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'loki'
find_pod(name)
get_current_component(cur_loki_filtro)

cur_prometheus_filtro=f"|grep Image: |grep prometheus: |awk -Fv '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'prometheus'
find_pod(name)
get_current_component(cur_prometheus_filtro)

cur_jaeger_filtro=f"|grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'jaeger-jaeger-operator'
find_pod(name)
get_current_component(cur_jaeger_filtro)
if "jaeger-jaeger-operator" in current_versions:
    current_versions["jaeger"] = current_versions.pop("jaeger-jaeger-operator")

cur_jaeger_elasticsearch_filtro=f"|grep Image: |grep elasticsearch |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'jaeger-elasticsearch'
find_pod(name)
get_current_component(cur_jaeger_elasticsearch_filtro)

cur_kiali_filtro=f"|grep Image: |grep Image: |awk -F:v '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'kiali'
find_pod(name)
get_current_component(cur_kiali_filtro)

cur_velero_filtro=f"|grep Image: |grep velero |awk -F:v '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'velero'
find_pod(name)
get_current_component(cur_velero_filtro)

cur_cert_manager_filtro=f"|grep Image: |grep cert-manager |awk '{{print $2}}' |awk -F:v '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'cert-manager'
find_pod(name)
get_current_component(cur_cert_manager_filtro)

cur_sealed_secrets_filtro=f"|grep Image: |awk -F: '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'" 
name = 'sealed-secrets'
find_pod(name)
get_current_component(cur_sealed_secrets_filtro)


print("\n- Pesquisa de novas versões nos repositórios...")

# Pesquisas das New-versions nos repositórios Helm
helm_search_grafana=f"helm search repo grafana/grafana |egrep -v \"NAME|agent\" |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_loki=f"helm search repo grafana/loki-stack |grep -v NAME |awk '{{print $3}}' |awk -Fv '{{print $2}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_prometheus=f"helm search repo prometheus-community/prometheus |grep -v NAME |awk '{{print $3}}' |head -n1 |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"
helm_search_jaeger=f"helm search repo jaegertracing/jaeger-operator |grep -v NAME |awk '{{print $3}}' |head -n1 |awk -F. '{{print $1\".\"$2}}'"
helm_search_jaeger_elastic=f"helm search repo bitnami/elasticsearch |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_kiali=f"helm search repo kiali/kiali-server |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"
helm_search_velero=f"helm search repo vmware-tanzu/velero |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"
helm_search_cert_manager=f"helm search repo jetstack/cert-manager |grep -v NAME |awk '{{print $3}}' |head -n1 |awk -F. '{{print $1\".\"$2}}' |awk -Fv '{{print $2}}'"
helm_search_sealed_secrets=f"helm search repo bitnami/sealed-secrets |grep -v NAME |awk '{{print $3}}' |awk -F. '{{print $1\".\"$2}}'"

# Função para buscar a nova versão por componente
def get_new_component(component, helm_cmd):
    if component is not None:
        command = {helm_cmd}
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        n_component = result.stdout.strip()
        new_versions[component] = n_component
        print(f"{component} = {n_component}")
    else:
        print(f"Nenhuma chave encontrada para {component}")

print()

grafana_new = 'grafana'
get_new_component(grafana_new, helm_search_grafana)

loki_new = 'loki'
get_new_component(loki_new, helm_search_loki)

prometheus_new = 'prometheus'
get_new_component(prometheus_new, helm_search_prometheus)

jaeger_new = 'jaeger'
get_new_component(jaeger_new, helm_search_jaeger)

jaeger_elasticsearch_new = 'jaeger-elasticsearch'
get_new_component(jaeger_elasticsearch_new, helm_search_jaeger_elastic)

kiali_new = 'kiali'
get_new_component(kiali_new, helm_search_kiali)

velero_new = 'velero'
get_new_component(velero_new, helm_search_velero)

cert_manager_new = 'cert-manager'
get_new_component(cert_manager_new, helm_search_cert_manager)

sealed_secrets_new = 'sealed-secrets'
get_new_component(sealed_secrets_new, helm_search_sealed_secrets)
print()

# Resultados  
# Função de compara_versoes entre current_versions e new_versions

print("-" * 50)
print("\n- Resultado:\n")

arquivo_saida='to_upgrade.txt'
with open(arquivo_saida, 'w') as arquivo_limpo:
    arquivo_limpo.truncate(0)

def compara_versoes(current_versions, new_versions, cur_component, new_component, arquivo_saida='to_upgrade.txt'):
    cur_version = current_versions.get(cur_component)
    new_version = new_versions.get(new_component)

    if cur_version is None or new_version is None:
        print(f'Chave "{cur_component}" não encontrada em pelo menos um dos dicionários.')
        return

    if not cur_version or not new_version:
        print(f'Chave "{cur_component}" tem um valor vazio em pelo menos um dos dicionários.')
        return

    if cur_version < new_version:
        resultado = f'X - {cur_component}: Precisa de atualização da versão: {cur_version} para: {new_version}'
        print(resultado)
        with open(arquivo_saida, 'a') as arquivo:
            arquivo.write(cur_component + '\n')

    else:
        resultado = f'✔ - {cur_component}: Já esta na versão mais atual: {new_version}'
        print(resultado)


# Chamada das funções de compara versão por componente (Istio e Ingress-Gateway por enquanto fora do Update)
compara_versoes(current_versions, new_versions, cur_component='grafana', new_component='grafana')
compara_versoes(current_versions, new_versions, cur_component='loki', new_component='loki')
compara_versoes(current_versions, new_versions, cur_component='prometheus', new_component='prometheus')
compara_versoes(current_versions, new_versions, cur_component='jaeger', new_component='jaeger')
compara_versoes(current_versions, new_versions, cur_component='jaeger-elasticsearch', new_component='jaeger-elasticsearch')
compara_versoes(current_versions, new_versions, cur_component='kiali', new_component='kiali')
compara_versoes(current_versions, new_versions, cur_component='velero', new_component='velero')
compara_versoes(current_versions, new_versions, cur_component='cert-manager', new_component='cert-manager')
compara_versoes(current_versions, new_versions, cur_component='sealed-secrets', new_component='sealed-secrets')
print()

# Imprimindo os dicionarios para debug
#print(f"current versions: {current_versions}")
#print(f"new versions: {new_versions}")
