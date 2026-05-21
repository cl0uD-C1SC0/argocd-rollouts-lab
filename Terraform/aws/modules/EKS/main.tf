resource "aws_eks_cluster" "eks-argocd" {
  depends_on = [aws_iam_role_policy_attachment.cluster_AmazonEKSClusterPolicy]

  name = var.eks_cluster-name

  access_config {
    authentication_mode = "API_AND_CONFIG_MAP"
  }

  role_arn = aws_iam_role.eks-assume-role.arn
  version  = "1.31"

  vpc_config {
    subnet_ids = var.pubsubnet
    endpoint_public_access = true
  }

  tags = {
    Name = "argocd-poc-cluster"
  }
}

resource "aws_eks_node_group" "eks-ndg-argocd" {
  depends_on = [ aws_eks_cluster.eks-argocd, aws_iam_role_policy_attachment.argocd-AmazonEC2ContainerRegistryReadOnly, aws_iam_role_policy_attachment.argocd-AmazonEKS_CNI_Policy, aws_iam_role_policy_attachment.argocd-AmazonEKSWorkerNodePolicy ]

  cluster_name      = aws_eks_cluster.eks-argocd.name
  node_group_name   = var.eks_cluster_ndg-name
  node_role_arn     = aws_iam_role.eks-argocd-ndg-role.arn

  instance_types = ["t3.medium"]

  scaling_config {
    desired_size = 2
    max_size = 2
    min_size = 1    
  }
  
  update_config {
    max_unavailable = 1
  }

  subnet_ids = var.pubsubnet
}

# ADDONS
resource "aws_eks_addon" "argocd-cluster-vpccni-addon" {
  depends_on = [ aws_eks_node_group.eks-ndg-argocd ]
  cluster_name = aws_eks_cluster.eks-argocd.name
  addon_name   = "vpc-cni"
}

resource "aws_eks_addon" "argocd-cluster-kubeproxy-addon" {
  depends_on = [ aws_eks_node_group.eks-ndg-argocd ]
  cluster_name = aws_eks_cluster.eks-argocd.name
  addon_name   = "kube-proxy"
}

resource "aws_eks_addon" "argocd-cluster-metricsserver-addon" {
  depends_on = [ aws_eks_node_group.eks-ndg-argocd ]
  cluster_name = aws_eks_cluster.eks-argocd.name
  addon_name   = "metrics-server"
}

resource "aws_eks_addon" "argocd-cluster-corends-addon" {
  depends_on = [ aws_eks_node_group.eks-ndg-argocd ]
  cluster_name = aws_eks_cluster.eks-argocd.name
  addon_name   = "coredns"
}

# Access entries
data "aws_caller_identity" "current-account" {}

resource "aws_eks_access_entry" "argocd-eks-access-entrie" {
  depends_on = [ aws_eks_cluster.eks-argocd ]
  cluster_name      = aws_eks_cluster.eks-argocd.name
  principal_arn     = data.aws_caller_identity.current-account.arn
  type              = "STANDARD"
}

resource "aws_eks_access_policy_association" "argocd-eks-access-policie" {
  depends_on = [ aws_eks_cluster.eks-argocd ]
  cluster_name = aws_eks_cluster.eks-argocd.name
  policy_arn = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"
  principal_arn = data.aws_caller_identity.current-account.arn
  access_scope {
    type = "cluster"
  }
}