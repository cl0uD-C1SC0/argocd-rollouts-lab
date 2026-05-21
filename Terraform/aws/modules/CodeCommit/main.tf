resource "aws_codecommit_repository" "argocd-poc-repository" {
  repository_name = "flask-app"
  description     = "Repository of APP"
  default_branch = "master"
}

resource "aws_codecommit_repository" "flask-app-canary-repo" {
  repository_name = "flask-app-canary"
  description     = "Repository of manifests for flask-app-canary"
  default_branch = "master"
}

resource "aws_codecommit_repository" "flask-app-bluegreen-repo" {
  repository_name = "flask-app-bluegreen"
  description     = "Repository of manifests for flask-app-canary"
  default_branch = "master"
}

# CREATING AWS IAM GIT CREDENTIALS
resource "aws_iam_service_specific_credential" "codecommit-user-credentials" {
  service_name = "codecommit.amazonaws.com"
  user_name    = var.codecommit-credentials-user
}
