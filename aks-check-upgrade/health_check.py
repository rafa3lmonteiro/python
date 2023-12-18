# Rafael Monteiro
# Dezembro/2023
#!/usr/bin/python3
import subprocess

components = {}

# Função para buscar os componentes com a Label projeto=component no cluster AKS
def get_kubectl_info():

    command = "kubectl get all -l project=component -A --no-headers | grep pod | awk '{print $1\":\"$2}' | awk -F:pod/ '{print $2\":\"$1}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Erro ao executar o comando: {result.stderr}")
        return None

    kubectl_output = result.stdout.strip().split('\n')
    
    for line in kubectl_output:
        key, value = line.split(':')
        components[key] = value
        
    return components


# Função para verificar se os componentes do Projeto estão Running depois do Upgrade e atribuindo em problem_found o resultado
def check_pod_status(components):
    problem_found = False

    for key, value in components.items():
        command = f"kubectl describe pod {key} -n {value} | grep Status:"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        problem = False

        if result.returncode == 0:
            status_line = result.stdout.strip()
            status = status_line.split(":")[1].strip() if ":" in status_line else None
            
            if status == "Running":
                print(f"{key} --> OK")
            else:
                print(f"{key} --> Com problema (Status: {status})")
                problem = True
        else:
            print(f"Erro ao executar o comando para {key} - {value}:\n{result.stderr}")
            problem = True

        # Ao longo das iterações com o for, acumula informações se ocorrer pelo menos um "problem = True" ao problem_found, ficando "True" tambem
        problem_found |= problem

    print('-'*50)
    print(f"\nproblem_found = {problem_found}")    
    return problem_found


# Chamada das funções
get_kubectl_info() 
check_pod_status(components)
