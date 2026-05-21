module "vpc" {
  source = "./modules/VPC"

  vpc_cidr = "10.0.0.0/16" # Default = 192.168.0.0/16

  # PUBSUBNET 1
  vpc_pubsubnet_1-az   = "us-east-1a"  # Default = us-east-1a
  vpc_pubsubnet_1-cidr = "10.0.0.0/24" # Default = 192.168.0.0/24

  # PUBSUBNET 2
  vpc_pubsubnet_2-az   = "us-east-1b"  # Default = us-east-1b
  vpc_pubsubnet_2-cidr = "10.0.1.0/24" # Default = 192.168.1.0/24

  # PRIVSUBNET 1
  vpc_privsubnet_1-az   = "us-east-1a"  # Default = us-east-1a
  vpc_privsubnet_1-cidr = "10.0.2.0/24" # Default = 192.168.2.0/24

  # PRIVSUBNET 2
  vpc_privsubnet_2-az   = "us-east-1b"  # Default = us-east-1b
  vpc_privsubnet_2-cidr = "10.0.4.0/24" # Default = 192.168.3.0/24

}

module "eks" {
  source = "./modules/EKS"

  vpc_id    = module.vpc.vpc_id
  pubsubnet = module.vpc.public_subnets
}

module "ecr" {
  source = "./modules/ECR"
}

module "codecommit" {
  source = "./modules/CodeCommit"

  # Change the value below if you want to use another aws user
  # Don't forget change in iam policy, look for: iam:ListServiceSpecificCredentials
  # and change the line: "arn:aws:iam::<ACCOUNT_ID:user/<AWS_USER>"
  # ex: "arn:aws:iam::1234567891:user/cloud_user" 
  codecommit-credentials-user = "YOUR_AWS_USER" # Default: argocd_user

}