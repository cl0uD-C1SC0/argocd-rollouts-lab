output "vpc_id" {
  value = aws_vpc.vpc_argocd.id
}

output "private_subnets" {
  value = [
    for s in [aws_subnet.privsubnet-1, aws_subnet.privsubnet-2] : s.id
  ]
}

output "public_subnets" {
  value = [
    for s in [aws_subnet.pubsubnet-1, aws_subnet.pubsubnet-2] : s.id
  ]
}