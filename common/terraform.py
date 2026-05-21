import time
from common.util import run_command, change_directory

def terraform_resources_to_apply_info():
    resources = [
        ("AWS Virtual Private Cloud", "argocd-vpc"),
        ("AWS Public Subnets", "pub-argocd-1a and pub-argocd-1b"),
        ("AWS Private Subnets", "priv-argocd-1a and priv-argocd-1b"),
        ("AWS Route Tables", "pub-rtb-argocd and priv-rtb-argocd"),
        ("AWS Internet Gateway", "argocd-igw"),
        ("AWS NAT Gateway", "argocd-natgw"),
        ("AWS Elastic Kubernetes Service", "argocd-poc-cluster"),
        ("AWS Elastic Container Registry", "flask-app"),
        ("Correctly routes in the Route tables", "")
    ]
    print(" ℹ️  The Terraform will create the following resources in AWS Cloud:")
    print("   |---------------------------------------|-------------------------------------|")
    print("   | {:<37} | {:<35} |".format("AWS RESOURCE", "RESOURCE NAME"))
    print("   |---------------------------------------|-------------------------------------|")
    for res, name in resources:
        print("   | {:<37} | {:<35} |".format(res, name))

    print("   |---------------------------------------|-------------------------------------|\n")

def init_terraform_environment():
    print(" ℹ️  Initializying Terraform Environment ")
    run_command(COMMAND="terraform init", shell=True)
    print(" ✅ Terraform has been initialized")

def apply_terraform_environment():
    terraform_resources_to_apply_info()
    print(" ℹ️  Applying Terraform Environment ")
    print(" ℹ️  Wait a few minutes...")
    run_command(COMMAND="terraform apply --auto-approve", shell=True)
    print(" ✅ Terraform has been applied!")

def save_terraform_output(BASE_PATH):
    print(f" ℹ️  Saving Terraform outputs on: {BASE_PATH}/terraform_outputs.json")
    time.sleep(2)
    run_command(COMMAND=f"terraform output codecommit-cred-user >> {BASE_PATH}/terraform_outputs", shell=True)
    run_command(COMMAND=f"terraform output codecommit-cred-password >> {BASE_PATH}/terraform_outputs", shell=True)
    print(" ✅ Saved the Terraform outputs ")


def init_terraform_configs(TERRAFORM_PATH):
    change_directory(TERRAFORM_PATH)
    init_terraform_environment()
    apply_terraform_environment()
    #save_terraform_output(BASE_PATH)
    #change_directory(BASE_PATH)
    return "Terraform Environment Applied"

if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")