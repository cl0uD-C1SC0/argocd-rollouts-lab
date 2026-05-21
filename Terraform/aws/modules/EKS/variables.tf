variable "eks_cluster-name" {
  description = "EKS Cluster Name"
  type = string
  default = "argocd-poc-cluster"
}

variable "eks_cluster_ndg-name" {
  description = "EKS Nodegroup Name"
  type = string
  default = "argocd-ndg"
}

variable "eks_cluster_iam-name" {
  description = "EKS Cluster IAM AmazonEKSClusterPolicy"
  type = string
  default = "AmazonEKSClusterPolicy-argocd"
}

variable "vpc_id" {}
variable "pubsubnet" {
  type = list(string)
}