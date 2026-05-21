variable "github_token" {
  description = "GitHub Personal Access Token"
  type        = string
  sensitive   = true
}

variable "repository_name" {
  description = "Repository to be created in user account"
  type        = string

  default = "argorollouts-lab-manifests"
}

variable "repository_visibility" {
  type    = string
  default = "public"
}