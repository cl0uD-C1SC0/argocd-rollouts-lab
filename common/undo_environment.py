from common.util import run_command, change_directory, remove_directory, remove_file
from common.kind_cluster import remove_kind_cluster
import os
import re

def delete_credentials_argo_apps(ARGO_APPS_PATH):
    change_directory(ARGO_APPS_PATH)
    for argo_app in os.listdir():
        with open(argo_app, 'r') as file:
            print(f" ℹ️  Removing CodeCommit credentials of {argo_app}")
            content = file.read()
        
        content = re.sub(r'(username:\s*)".*?"', r'\1{git-username}', content)
        content = re.sub(r'(password:\s*)".*?"', r'\1{git-password}', content)

        with open(argo_app, 'w') as file:
            file.write(content)

    print(" ✅ Successful")

def delete_k8s_resources():
    print(" ℹ️  Deleting k8s resources")
    namespaces_to_delete = ["argocd", "ingress-nginx", "flask-app-hml"]
    for ns in namespaces_to_delete:
        print(f" ℹ️  Deleting the entire resources in the following namespace: {ns}")
        run_command(f"kubectl delete namespace {ns}", shell=True)
        print(f" ✅ Successful to remove the entire {ns} namespace") 

def delete_tf_files():
    print(" ℹ️  Removing Terraform Files...")
    files_to_delete = [".terraform.lock.hcl", "terraform.tfstate", "terraform.tfstate.backup"]
    
    for file in files_to_delete:
        remove_file(file)
    remove_directory(PATH="./.terraform")
    print(" ✅ Terraform files has been removed!") 

def delete_output_files(BASE_PATH):
    change_directory(BASE_PATH)
    files_to_delete = ["argocd_credentials.txt", "terraform_outputs"]
    for file in files_to_delete:
        remove_file(FILE=f"./{file}")

def destroy_terraform_env():
    print(" ℹ️  Deleting Terraform Environment...")
    result = run_command("terraform destroy --auto-approve", shell=True)
    print(result)
    print(" ✅ Terraform Environment has been deleted!")

def undo_local_environment(BASE_PATH):
    remove_kind_cluster()

def undo_aws_environment(BASE_PATH, TERRAFORM_PATH, ARGO_APPS_PATH):
    delete_credentials_argo_apps(ARGO_APPS_PATH)
    change_directory(TERRAFORM_PATH)
    delete_k8s_resources()
    destroy_terraform_env()
    delete_tf_files()
    delete_output_files(BASE_PATH)
    

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")