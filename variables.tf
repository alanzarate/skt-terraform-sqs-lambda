variable "region" {
    default = "us-west-2"
    description = "AWS Region to deploy to"
}
variable "app_env" {
    default = "alanProd"
    description = "Common prefix for all Terraform created resources"
}