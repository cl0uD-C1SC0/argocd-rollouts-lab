output "repository-ssh-url" {
  value = aws_codecommit_repository.argocd-poc-repository.clone_url_ssh
}

output "repository-arn" {
  value = aws_codecommit_repository.argocd-poc-repository.arn
}

output "repository-name" {
  value = aws_codecommit_repository.argocd-poc-repository.repository_name
}

output "codecommit-cred-user" {
  value = aws_iam_service_specific_credential.codecommit-user-credentials.service_user_name
  sensitive = true
}

output "codecommit-cred-password" {
  value = aws_iam_service_specific_credential.codecommit-user-credentials.service_password
  sensitive = true
}