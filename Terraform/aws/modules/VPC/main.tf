resource "aws_vpc" "vpc_argocd" {
  cidr_block       = var.vpc_cidr
  instance_tenancy = "default"

  tags = {
    Name = var.vpc_name
  }
}

resource "aws_internet_gateway" "vpc_internetgateway" {
  depends_on = [ aws_vpc.vpc_argocd ]
  vpc_id = aws_vpc.vpc_argocd.id

  tags = {
    Name = var.vpc_internetgateway_name
  }
}

# PUB SUBNETS
resource "aws_subnet" "pubsubnet-1" {
  depends_on = [ aws_vpc.vpc_argocd ]
  vpc_id = aws_vpc.vpc_argocd.id
  cidr_block = var.vpc_pubsubnet_1-cidr
  availability_zone = var.vpc_pubsubnet_1-az
  map_public_ip_on_launch = true
  tags = {
    Name = var.vpc_pubsubnet_1-name
  }
}

resource "aws_subnet" "pubsubnet-2" {
  depends_on = [ aws_vpc.vpc_argocd ]
  vpc_id = aws_vpc.vpc_argocd.id
  cidr_block = var.vpc_pubsubnet_2-cidr
  availability_zone = var.vpc_pubsubnet_2-az
  map_public_ip_on_launch = true
  tags = {
    Name = var.vpc_pubsubnet_2-name
  }
}

# PRIV SUBNETS
resource "aws_subnet" "privsubnet-1" {
  depends_on = [ aws_vpc.vpc_argocd ]
  vpc_id = aws_vpc.vpc_argocd.id
  cidr_block = var.vpc_privsubnet_1-cidr
  availability_zone = var.vpc_privsubnet_1-az
  tags = {
    Name = var.vpc_privsubnet_1-name
  }
}

resource "aws_subnet" "privsubnet-2" {
  depends_on = [ aws_vpc.vpc_argocd ]
  vpc_id = aws_vpc.vpc_argocd.id
  cidr_block = var.vpc_privsubnet_2-cidr
  availability_zone = var.vpc_privsubnet_2-az
  tags = {
    Name = var.vpc_privsubnet_2-name
  }
}

# NATGATEWAY
resource "aws_eip" "elastic_ip-ntgw" {
  tags = {
    Name = var.elastic_ip-name
  }
}

resource "aws_nat_gateway" "natgateway" {
  depends_on = [ aws_vpc.vpc_argocd, aws_subnet.pubsubnet-1, aws_eip.elastic_ip-ntgw ]
  allocation_id = aws_eip.elastic_ip-ntgw.id
  subnet_id = aws_subnet.pubsubnet-1.id

  tags = {
    Name = var.vpc_natgateway_name
  }
}

# Route table
resource "aws_route_table" "pub-rtb" {
  depends_on = [
    aws_vpc.vpc_argocd,
    aws_subnet.privsubnet-1,
    aws_subnet.privsubnet-2,
    aws_subnet.pubsubnet-1,
    aws_subnet.pubsubnet-2
  ]
  vpc_id = aws_vpc.vpc_argocd.id
  tags = {
    Name = var.rtb_pub-name
  }
}

resource "aws_route_table" "priv-rtb" {
  depends_on = [
    aws_vpc.vpc_argocd,
    aws_subnet.privsubnet-1,
    aws_subnet.privsubnet-2,
    aws_subnet.pubsubnet-1,
    aws_subnet.pubsubnet-2
  ]
  vpc_id = aws_vpc.vpc_argocd.id
  tags = {
    Name = var.rtb_priv-name
  }
}

# Routes to RTBs
resource "aws_route" "route_internetgateway" {
  depends_on = [ aws_route_table.pub-rtb, aws_internet_gateway.vpc_internetgateway ]
  route_table_id = aws_route_table.pub-rtb.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.vpc_internetgateway.id
}

resource "aws_route" "route_natgateway" {
  depends_on = [ aws_route_table.priv-rtb, aws_nat_gateway.natgateway ]
  route_table_id = aws_route_table.priv-rtb.id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id = aws_nat_gateway.natgateway.id
}

# Subnet associations
# PUBs
resource "aws_route_table_association" "pub1a_association" {
  depends_on = [ aws_route_table.pub-rtb, aws_subnet.pubsubnet-1 ]
  subnet_id = aws_subnet.pubsubnet-1.id
  route_table_id = aws_route_table.pub-rtb.id
}

resource "aws_route_table_association" "pub1b_association" {
  depends_on = [ aws_route_table.pub-rtb, aws_subnet.pubsubnet-2 ]
  subnet_id = aws_subnet.pubsubnet-2.id
  route_table_id = aws_route_table.pub-rtb.id
}

# Privs
resource "aws_route_table_association" "priv1a_association" {
  depends_on = [ aws_route_table.priv-rtb, aws_subnet.privsubnet-1 ]
  subnet_id = aws_subnet.privsubnet-1.id
  route_table_id = aws_route_table.priv-rtb.id
}

resource "aws_route_table_association" "priv2a_association" {
  depends_on = [ aws_route_table.priv-rtb, aws_subnet.privsubnet-2 ]
  subnet_id = aws_subnet.privsubnet-2.id
  route_table_id = aws_route_table.priv-rtb.id
}