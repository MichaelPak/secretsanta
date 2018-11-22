resource "digitalocean_ssh_key" "public" {
  name       = "SecreSanta"
  public_key = "${file(var.public_key)}"
}

resource "digitalocean_droplet" "web" {
  image  = "ubuntu-18-04-x64"
  name   = "secretsanta"
  region = "${var.region}"
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
  name   = "secretsanta"
  value  = "${digitalocean_droplet.web.ipv4_address}"
}

resource "digitalocean_firewall" "web" {
  name = "only-22-80-and-443"

  droplet_ids = ["${digitalocean_droplet.web.id}"]

  inbound_rule = [
    {
      protocol           = "tcp"
      port_range         = "22"
      source_addresses   = ["0.0.0.0/24"]
    },
    {
      protocol           = "tcp"
      port_range         = "80"
      source_addresses   = ["0.0.0.0/0", "::/0"]
    },
    {
      protocol           = "tcp"
      port_range         = "443"
      source_addresses   = ["0.0.0.0/0", "::/0"]
    },
    {
      protocol           = "icmp"
      source_addresses   = ["0.0.0.0/0", "::/0"]
    },
  ]
}

resource "null_resource" "config" {
  triggers {
    droplet_id = "${digitalocean_droplet.web.id}"
    firewall_id = "${digitalocean_firewall.web.id}"
  }

  provisioner "local-exec" {
    command = "ansible-playbook -i ${digitalocean_droplet.web.ipv4_address}, -e ansible_python_interpreter=/usr/bin/python3 iaac/deploy.yml"
  }
}