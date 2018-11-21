resource "digitalocean_ssh_key" "public" {
  name       = "SecreSanta"
  public_key = "${file(var.public_key)}"
}

resource "digitalocean_droplet" "web" {
  image  = "ubuntu-18-04-x64"
  name   = "secretsanta"
  region = "ams3"
  size   = "s-1vcpu-1gb"
  ssh_keys = ["${digitalocean_ssh_key.public.fingerprint}"]

  provisioner "remote-exec" {
    connection {
      host = "${digitalocean_droplet.web.ipv4_address}"
      user = "root"
      private_key = "${file(var.private_key)}"
    }
    inline = ["echo 'sshd is up'"]
  }
}

resource "digitalocean_record" "www" {
  domain = "pak.digital"
  type   = "A"
  name   = "secresanta"
  value  = "${digitalocean_droplet.web.ipv4_address}"
}