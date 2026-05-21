import subprocess
import os
import shutil
from common.util import run_command


def check_required_cli_commands(package):
    tool = shutil.which(package) is not None
    if tool:
        print(f" ✅  The CLI: {package} was found on the system!")
        return True
    return False

def get_argocd_credentials(BASE_PATH):
    print(" ℹ️  Getting Argo credentials")
    get_credentials_path =  f'{BASE_PATH}/Ansible/general_playbooks/get-argocd-credentials.yml'
    result = run_command(COMMAND=f"ansible-playbook {get_credentials_path}", text=True, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    with open(f'{BASE_PATH}/argocd_credentials.txt', 'w') as file:
        for line in result.splitlines():
            if "ARGO" in line.replace(' ', ''):
                file.write(line.strip().replace('"', '').replace(",", "") +"\n")
    
    print(" ✅  Credentials are been saved on the following file: argocd_credentials.txt")
    print(f" ℹ️  To access the ArgoCD UI, please run the following command: ")
    print("------------------------------------------------------------------")
    print(f" ➡️  kubectl port-forward svc/argocd-server -n argocd 8080:443")
    print("------------------------------------------------------------------")


def install_cli_scripts(INVENTORY_INI, SCRIPTS_PATH):
    print(" 🔍  Verifying required CLI tools")
    os.chdir(SCRIPTS_PATH)
    
    SCRIPTS = os.listdir(SCRIPTS_PATH)

    for script in SCRIPTS:
        package = script.split("_")[1]
        if not check_required_cli_commands(package):
            print(f" ❌  The following package: '{package}' package was not found on System")
            print(f" ℹ️  Installing: {package} package now")
            run_command(COMMAND=f"ansible-playbook -i {INVENTORY_INI} {script}", shell=True)
    print(" ✅  All required CLI Tools are ok!")

def run_general_scripts(INVENTORY_INI, SCRIPTS_PATH):
    print(" ℹ️  Applying General Ansible scripts")
    run_command(COMMAND=f"ansible-playbook -i {INVENTORY_INI} {SCRIPTS_PATH}", shell=True)
    print(f" ✅  Script applied!")
    return " ✅  All scripts has been applied in the Environment!"
    
if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")