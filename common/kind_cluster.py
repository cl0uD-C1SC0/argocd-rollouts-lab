import subprocess

def remove_kind_cluster():
    cluster_name = "argorollouts-sandbox-cluster"
    command = ["kind", "delete", "cluster", "--name", cluster_name]

    try:
        print(f"Deleting cluster '{cluster_name}'...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"Successfully deleted cluster: {cluster_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting cluster: {e.stderr}")

def create_kind_cluster(config_file):
    cluster_name = "argorollouts-sandbox-cluster"
    command = ["kind", "create", "cluster", "--name", cluster_name]
    
    if config_file:
        command.extend(["--config", config_file])
    
    try:
        print(f"Creating cluster '{cluster_name}'...")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"Successfully created cluster: {cluster_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating cluster: {e.stderr}")

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")
