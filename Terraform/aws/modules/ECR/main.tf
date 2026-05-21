resource "aws_ecr_repository" "argocd-ecr-repo" {
  name                 = var.ecr_argocd_repo-name
  image_tag_mutability = "IMMUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}