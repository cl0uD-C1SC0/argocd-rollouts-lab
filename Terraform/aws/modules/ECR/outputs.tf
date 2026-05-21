# ECR OUTPUTS
# REGISTRY PATH/URL/id/NAME

output "ecr_id" {
  value = aws_ecr_repository.argocd-ecr-repo.id
}

output "ecr_url" {
  value = aws_ecr_repository.argocd-ecr-repo.repository_url
}