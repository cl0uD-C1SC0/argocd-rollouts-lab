output "codecommit-cred-user" {
  value     = module.codecommit.codecommit-cred-user
  sensitive = true
}

output "codecommit-cred-password" {
  value     = module.codecommit.codecommit-cred-password
  sensitive = true
}