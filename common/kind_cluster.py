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

def validate_kind_cluster_exists():
    cluster_name = "argorollouts-sandbox-cluster"
    command = ["kind", "get", "clusters"]

    print(f" 🔍  Verifying if a kind cluster called: {cluster_name} exists")
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        cluster = result.stdout.replace("\n", "")
        if cluster == cluster_name:
            print(f" ✅  Bypassing! Found a kind cluster with the name {cluster_name}")
            return True
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error validate cluster: {e.stderr}")
        return True

def create_kind_cluster(config_file):
    cluster_name = "argorollouts-sandbox-cluster"
    command = ["kind", "create", "cluster", "--name", cluster_name]

    if not validate_kind_cluster_exists():
        if config_file:
            command.extend(["--config", config_file])
        try:
            print(f" ℹ️  Creating cluster '{cluster_name}'...")
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(f" ✅  Successfully created cluster: {cluster_name}")
            return
        except subprocess.CalledProcessError as e:
            print(f"Error creating cluster: {e.stderr}")
            return

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")
