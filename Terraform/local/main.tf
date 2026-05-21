resource "github_repository" "argorollouts_lab" {

  name        = var.repository_name
  visibility  = var.repository_visibility
  description = "test"

  template {
    owner      = "cl0uD-C1SC0"
    repository = "argocd-rollouts-lab-manifests"
    include_all_branches = true
  }
}