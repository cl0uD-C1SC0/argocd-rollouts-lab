output "repository_name" {
  value = github_repository.argorollouts_lab.name
}

output "repository_url" {
  value = github_repository.argorollouts_lab.html_url
}

output "clone_url" {
  value = github_repository.argorollouts_lab.http_clone_url
}