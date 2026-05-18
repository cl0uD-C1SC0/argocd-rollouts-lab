import os
import time
import datetime
import platform

from common import ansible as ansible_script
from common import kind_cluster as k8s_cluster
from common import undo_environment as remove

start_time = datetime.datetime.now()

BASE_PATH = os.getcwd()

TERRAFORM_PATH      = f'{BASE_PATH}/Terraform'
KIND_CONFG          = f'{BASE_PATH}/kind-config.yaml'

AWS_PLAYBOOKS       = f'{BASE_PATH}/Ansible/playbooks_aws'
ANSIBLE_CLI_SCRIPTS = f'{BASE_PATH}/Ansible/playbooks_cli'
GENERAL_PLAYBOOKS   = f'{BASE_PATH}/Ansible/general_playbooks'
INVENTORY_INI      = f'{BASE_PATH}/inventory.ini'


APP_PATH            = f'{BASE_PATH}/Docker/'
ARGO_APPS_PATH      = f'{BASE_PATH}/Kubernetes/argo-apps'
OPERATIONAL_SYSTEM  = platform.system()

general_options = {
    'Configure Local Environment': '1',
    'Configure AWS Environment': '2',
    'Clear Environment': '0',
}

def alert_message():
    print("\n =======================================PLEASE READ THE NODES BELOW======================================== \n")
    print(" ⚠️  THIS SANDBOX WILL REWRITE YOUR KUBECONFIG FILE")
    print(" ⚠️  WHEN USING AWS ENVIRONMENT THE SANDBOX WILL USE YOUR CURRENT AWS CREDENTIALS")
    print(" ⚠️  IT'S RECOMMENDED TO CREATE A NEW AWS USER WITH AWS CREDENTIALS (WHILE USING AWS ENVIRONMENT)")
    print(" ⚠️  THE FOLLOWING CLI TOOLS WILL BE INSTALLED IF NEEDED: kubectl, docker, kind, argocd & argo rollouts CLI")
    print("\n ==========================================================================================================")

def calc_execution_time():
    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time) / 60
    print(f"\n ✅ Script takes {execution_time.total_seconds()} minutes to Done")

def init_time(message):
    timer_list = ["1️⃣", "2️⃣", "3️⃣"]
    print(" ℹ️  May this script need some manual interactions, pay attention please!")
    print(" ⚠️  Please, don't stop the script execution!\n")
    for i in timer_list:
        print(f" ℹ️  {message} the environment in {i}")
        time.sleep(1)

def clear_environment(environment, BASE_PATH, TERRAFORM_PATH, ARGO_APPS_PATH):
    if environment == 'aws':
        print(" ℹ️  Deleting AWS Environment")
        remove.undo_aws_environment(BASE_PATH, TERRAFORM_PATH, ARGO_APPS_PATH)
        print(" ✅  All AWS Environment has been cleaned!")
        return 
    print(" ℹ️  Deleting Local Environment")
    remove.undo_local_environment(BASE_PATH)
    print(" ✅  All Local Environment has been cleaned!")
    return
    
def deploy_sandbox_local(GENERAL_PLAYBOOKS, ANSIBLE_CLI_SCRIPTS, INVENTORY_INI, KIND_CONFG):
    init_time(message="Initializing")

    print(" ℹ️  Verifying required CLI tools")
    ansible_script.install_cli_scripts(INVENTORY_INI, SCRIPTS_PATH=ANSIBLE_CLI_SCRIPTS)

    print(" ℹ️  Creating k8s cluster")
    k8s_cluster.create_kind_cluster(config_file=KIND_CONFG)

    print(" ℹ️  Running general playbooks")
    ansible_script.run_ansible_script(INVENTORY_INI, SCRIPTS_PATH=GENERAL_PLAYBOOKS)

def start_execution(user_choice, BASE_PATH, ANSIBLE_PATH, ARGO_APPS_PATH):     
#     if user_choice == 1:
#         init_time(message="Initializing")

#     print(BASE_PATH)
#     print(ANSIBLE_PATH)
#     print(ARGO_APPS_PATH)
        
#         print("\n 🟢 INITIALIZING THE ENVINRONMENT 🟢\n")
#         print(" ℹ️  Configuring the environment...")
#         print(" ℹ️  Checking the required programs...")
#         util.verify_installed_tool()
#         terraform_script.init_terraform_configs(BASE_PATH, TERRAFORM_PATH)
#         set_aws_cluster()
#         argocd.init_argocd_configs(BASE_PATH, ARGO_APPS_PATH)
#         ansible_script.init_ansible_configs(BASE_PATH, ANSIBLE_PATH)
#         code_push.init_codecommit_configs(BASE_PATH)
#         ansible_script.apply_argocd_apps()

#         print(f" ✅ Environment has been created")
#         calc_execution_time()
#         return "Environment created"
#     elif user_choice == 0:
#         init_time(message="Deleting")
#         undo_environment.init_delete_environment(BASE_PATH, TERRAFORM_PATH, ARGO_APPS_PATH)
#         calc_execution_time()
#         return "Environment Deleted"
#     print(" ❌  Invalid Option, try again...")
#     return "Invalid Option, try again"
    ...

if __name__ == '__main__':
    if OPERATIONAL_SYSTEM != "Linux":
        print("⚠️  To run the Argo Rollouts Sandbox it's necessary a Linux Operational System")
        print("⚠️  Try again.")
    else:
        alert_message()
        agreement = input("\nDo you agree? (Y/N): ").lower()
        os.system('clear')
        
        if agreement == 'y':
            for option, value in general_options.items():
                print(f"Option {value}: {option}" )
            user_choice = int(input("Choose an option: "))

            if user_choice == 1:
                deploy_sandbox_local(GENERAL_PLAYBOOKS, ANSIBLE_CLI_SCRIPTS, INVENTORY_INI, KIND_CONFG)

            elif user_choice == 2:
                print("⚠️  Deploying a AWS Environment is in developing phase")
                ...

            elif user_choice == 0:
                environment = input("Qual ambiente deseja remover? (AWS/LOCAL): ").lower()
                clear_environment(environment, BASE_PATH, TERRAFORM_PATH, ARGO_APPS_PATH)

    print("\nBye!...")