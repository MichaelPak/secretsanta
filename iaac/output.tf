output "web_external_ip" {
  value = "${digitalocean_droplet.web.ipv4_address}"
}