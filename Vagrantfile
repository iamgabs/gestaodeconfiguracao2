# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  
  config.vm.box = "hashicorp/bionic64"
  config.vm.box_check_update = false

  # Config network for VM1
  config.vm.define :vm1 do |vm1|
    vm1.vm.network :private_network, ip: "192.168.56.10"
    vm1.vm.synced_folder "./", "/vagrant_data"
    vm1.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt install -y software-properties-common
      add-apt-repository --yes --update ppa:ansible/ansible
      apt install -y ansible
    SHELL
  end

  # Configuring VM2 for the application
  config.vm.define :vm2 do |vm2|
    vm2.vm.network :private_network, ip: "192.168.56.11"
  end

  # Configure provider
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
  end

end
