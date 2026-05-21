variable "vpc_name" {
    description = "VPC Name"
    type = string
    default = "argocd-vpc"
}

variable "vpc_cidr" {
  description = "VPC CIDR"
  type = string
  default = "192.168.0.0/16"
}

variable "vpc_internetgateway_name" {
  description = "Internet Gateway name"
  type = string
  default = "argocd-igw"
}

variable "vpc_natgateway_name" {
  description = "NatGateway name"
  type = string
  default = "argocd-natgw"
}

###########################
# PUB SUBNET 1 - configs  #
###########################
variable "vpc_pubsubnet_1-name" {
  description = "Name of Pubsubnet 1"
  type = string
  default = "pub-argocd-1a"
}

variable "vpc_pubsubnet_1-cidr" {
  description = "CIDR of Pubsubnet 1"
  type = string
  default = "192.168.0.0/24"
}

variable "vpc_pubsubnet_1-az" {
  description = "Availability Zone of pubsubnet 1"
  type = string
  default = "us-east-1a"
}

###########################
# PUB SUBNET 2 - configs  #
###########################
variable "vpc_pubsubnet_2-name" {
  description = "Name of Pubsubnet 2"
  type = string
  default = "pub-argocd-1b"
}

variable "vpc_pubsubnet_2-cidr" {
  description = "CIDR of Pubsubnet 2"
  type = string
  default = "192.168.1.0/24"
}

variable "vpc_pubsubnet_2-az" {
  description = "Availability Zone of pubsubnet 2"
  type = string
  default = "us-east-1b"
}

###########################
# PRIV SUBNET 1 - configs #
###########################
variable "vpc_privsubnet_1-name" {
  description = "Name of Privsubnet 1"
  type = string
  default = "priv-argocd-1a"
}

variable "vpc_privsubnet_1-cidr" {
  description = "CIDR of Privsubnet 1"
  type = string
  default = "192.168.2.0/24"
}

variable "vpc_privsubnet_1-az" {
  description = "Availability Zone of privsubnet 1"
  type = string
  default = "us-east-1a"
}

###########################
# PRIV SUBNET 2 - configs #
###########################
variable "vpc_privsubnet_2-name" {
  description = "Name of Privsubnet 2"
  type = string
  default = "priv-argocd-1b"
}

variable "vpc_privsubnet_2-cidr" {
  description = "CIDR of Privsubnet 2"
  type = string
  default = "192.168.3.0/24"
}

variable "vpc_privsubnet_2-az" {
  description = "Availability Zone of privsubnet 2"
  type = string
  default = "us-east-1b"
}

# ELASTIC IP
variable "elastic_ip-name" {
  description = "Name of Elastic IP for NAT Gateway"
  type = string
  default = "argocd-eip-natgw"
}

# Route table names
variable "rtb_pub-name" {
  description = "Name of Pub RTB"
  type = string
  default = "pub-rtb-argocd"
}

variable "rtb_priv-name" {
  description = "Name of Priv RTB"
  type = string
  default = "priv-rtb-argocd"
}