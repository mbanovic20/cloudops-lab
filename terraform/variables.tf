variable "subscription_id" {
  description = "Azure subscription that will hold the resources."
  type        = string
}

variable "prefix" {
  description = "Name prefix shared by all resources."
  type        = string
  default     = "cloudopslab"
}

variable "location" {
  description = "Azure region."
  type        = string
  default     = "westeurope"
}

variable "node_count" {
  description = "Number of worker nodes in the AKS cluster."
  type        = number
  default     = 1
}

variable "node_vm_size" {
  description = "VM size of the AKS worker nodes."
  type        = string
  default     = "Standard_B2s"
}
