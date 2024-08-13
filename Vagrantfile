# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
 
    config.vm.box = "ubuntu/jammy64"
    config.vm.box_check_update = false
  
    # Config network
    config.vm.define :vm1 do |vm1|
      vm1.vm.network :private_network, ip: "192.168.56.10"
      
      vm1.vm.provision "shell", inline: <<-SHELL
        curl http://192.168.56.11:5000
      SHELL
    end
  
    # Configuring my application to run into VM2 
    # As it is a python application, we need to install 
    # A python setup for running the app
    config.vm.define :vm2 do |vm2|
      vm2.vm.network :private_network, ip: "192.168.56.11"
  
      vm2.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update && sudo apt-get upgrade -y
        sudo apt-get install -y python3 python3-pip
        git clone https://github.com/iamgabs/gestaodeconfiguracao2.git /app
        cd /app
        pip3 install -r requirements.txt  
        flask --app src/app.py run & 
      SHELL
    end
  
    config.vm.provider "virtualbox" do |vb|
      # Display the VirtualBox GUI when booting the machine
      vb.gui = false
    
      # Customize the amount of memory on the VM:
      vb.memory = "1024"
    end
  
  end
  