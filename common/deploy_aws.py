from common import util

def set_aws_cluster():
    print(" ℹ️  Updating the Kubeconfig")
    util.run_command(COMMAND="aws eks update-kubeconfig --name argocd-poc-cluster --region us-east-1", shell=True)
    print(" ✅ Kubeconfig has been Updated!")