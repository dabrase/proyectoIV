require 'yaml'

current_dir    = File.dirname(File.expand_path(__FILE__))
variables = YAML.load_file("#{current_dir}/variables.yml")

Vagrant.configure(2) do |config|

  	config.vm.box = "azure"  
	config.vm.network "public_network"
	config.vm.network "forwarded_port", guest: 80, host: 80
	config.vm.provider :azure do |azure, override|

  		azure.mgmt_certificate = File.expand_path("azure.pem")
        azure.mgmt_endpoint    = 'https://management.core.windows.net'
        azure.subscription_id = variables['SUBSCRIP']
        azure.vm_name     = variables['MAQUINAV']
        azure.vm_image    = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
        azure.vm_size     = 'Small'
        config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
        azure.cloud_service_name = variables['MAQUINAV']

		azure.vm_user = variables['USUARIO'] # defaults to 'vagrant' if not provided
        azure.vm_password = variables['PASSW']
        azure.vm_location = 'Central US'
        azure.ssh_port = '22'
		azure.tcp_endpoints = '80:80'

  	end
	
	config.ssh.username = variables['USUARIOSSH']
  	config.ssh.password = variables['PASSWSSH']
	config.vm.synced_folder ".", "/vagrant",disabled:true

  	config.vm.provision "ansible" do |ansible|
		ansible.raw_arguments=["-vvvv"]
		ansible.sudo = true        
		ansible.playbook = "configuracion_ansible.yml"
		ansible.verbose = "v"
		ansible.host_key_checking = false
	end
  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end
