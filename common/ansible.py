import subprocess
import os
import shutil
from common.util import run_command


def check_required_cli_commands(package):
    return shutil.which(package) is not None

def get_argocd_credentials(BASE_PATH):
    print(" ℹ️  Getting Argo credentials")
    result = run_command(COMMAND="ansible-playbook get-argocd-credentials.yml", text=True, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    with open(f'{BASE_PATH}/argocd_credentials.txt', 'w') as file:
        for line in result.splitlines():
            if "ARGO" in line.replace(' ', ''):
                file.write(line.strip().replace('"', '').replace(",", "") +"\n")
    
    print(" ✅ Credentials are been saved on the following file: argocd_credentials.txt")

def install_cli_scripts(INVENTORY_INI, SCRIPTS_PATH):
    os.chdir(SCRIPTS_PATH)
    
    SCRIPTS = os.listdir(SCRIPTS_PATH)

    if SCRIPTS_PATH.endswith("cli"):
        for script in SCRIPTS:
            package = script.split("_")[1]
            if not check_required_cli_commands(package):
                print(f" ℹ️  The following package: '{package}' package was not found on System")
                print(f" ℹ️  Installing: {package} package now")
                run_command(COMMAND=f"ansible-playbook -i {INVENTORY_INI} {script}", shell=True)
        return "✅ ALL CLI Tools are ok!"

def run_ansible_script(BASE_PATH, SCRIPTS_PATH):
    os.chdir(SCRIPTS_PATH)
    SCRIPTS = os.listdir(SCRIPTS_PATH)

    for script in SCRIPTS:
        print(" ℹ️  Applying Ansible scripts")
        if script == 'get-argocd-credentials.yml':
            get_argocd_credentials(BASE_PATH)
        else:
            print(f" ℹ️  Applying Ansible script: {script}")
            run_command(COMMAND=f"ansible-playbook {script}", shell=True)
        print(f" ✅ Script applied!")
    return "✅ All scripts has been applied in the Environment!"
    
if __name__ == '__main__':
    print("Please, run init.py script located in the Root Directory of this repository")