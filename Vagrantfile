# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  
  config.vm.box = "hashicorp/bionic64"
  config.vm.box_check_update = false

  # Config network for VM1
  config.vm.define :vm1 do |vm1|
    vm1.vm.network :private_network, ip: "192.168.33.10"
    vm1.vm.synced_folder "./", "/vagrant_data"
  end

  # Configuring VM2 for the application
  config.vm.define :vm2 do |vm2|
    vm2.vm.network :private_network, ip: "192.168.33.11"
    vm2.vm.network "forwarded_port", guest: 5000, host: 5000
    vm2.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt install -y software-properties-common
      sudo apt-get update && sudo apt-get upgrade -y
      sudo apt-get install -y python3 python3-pip
      git clone https://github.com/iamgabs/gestaodeconfiguracao2.git /app
      cd /app
      pip3 install -r requirements.txt 
      FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 flask run
    SHELL
  end

  # Configure provider
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
  end

end
