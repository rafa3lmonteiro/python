#!/usr/bin/python3
import subprocess
import platform

def install_helm():
    os = platform.system()
    if os == "Darwin":
        subprocess.run(["brew", "update"], check=True)
        subprocess.run(["brew", "install", "helm"], check=True)
    elif os == "Linux":
        subprocess.run(["curl", "-fsSL", "-o", "get_helm.sh", "https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3"])
        subprocess.run("chmod 700 get_helm.sh && ./get_helm.sh", shell=True, check=True)
        subprocess.run(["./get_helm.sh"])
    elif os == "Windows":
        subprocess.run(["choco", "install", "kubernetes-helm"], check=True)
    else:
        print("Helm not supported for this OS is not supported.")


def config_helm_repos():
# Helm charts repository configuration
    subprocess.run(["helm", "repo", "add", "vmware-tanzu", "https://vmware-tanzu.github.io/helm-charts"]) 
    subprocess.run(["helm", "repo", "add", "istio", "https://istio-release.storage.googleapis.com/charts"])
    subprocess.run(["helm", "repo", "add", "grafana", "https://grafana.github.io/helm-charts"])
    subprocess.run(["helm", "repo", "add", "prometheus-community", "https://prometheus-community.github.io/helm-charts"])
    subprocess.run(["helm", "repo", "add", "kiali", "https://kiali.org/helm-charts"])
    subprocess.run(["helm", "repo", "add", "mongodb", "https://mongodb.github.io/helm-charts"])
    subprocess.run(["helm", "repo", "add", "jaegertracing", "https://jaegertracing.github.io/helm-charts"])
    subprocess.run(["helm", "repo", "add", "jetstack", "https://charts.jetstack.io"])
    subprocess.run(["helm", "repo", "add", "weaviate", "https://weaviate.github.io/weaviate-helm"])
    subprocess.run(["helm", "repo", "add", "bitnami", "https://charts.bitnami.com/bitnami"])


 # precisa de um helm update

def install_kubectl():
    os = platform.system()
    if os == "Darwin":
        subprocess.run(["brew", "update"], check=True)
        subprocess.run(["brew", "install", "kubectl"], check=True)
    elif os == "Linux":
        subprocess.run("curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl", shell=True, check=True)
        subprocess.run("chmod +x ./kubectl && mkdir -p ~/.local/bin && mv ./kubectl ~/.local/bin/kubectl", shell=True, check=True)
    elif os == "Windows":
        subprocess.run(["choco", "install", "kubernetes-cli"], check=True)
    else:
        print("Kubectl not supported for this OS.")


print("Installing Helm...")
install_helm()
config_helm_repos()
print("Helm installed and repos configured")

print("Installing Kubectl...")
install_kubectl()
print("Kubectl installed")