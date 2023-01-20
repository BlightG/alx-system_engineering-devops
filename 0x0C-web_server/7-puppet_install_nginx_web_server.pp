# installing and configuring an Nginx server
exec {'sed':
  provider => shell,
  command  => "sudo apt-get -y update;sudo apt-get -y install nginx;echo 'Hello World!' | sudo tee /var/www/html/index;sudo sed -i '/listen 80 default_server;/a \\tlocation /redirect_me { \n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}' /etc/nginx/sites-enabled/default; line='\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}'; echo 'Ceci n'est pas une page\n' | sudo tee /usr/share/nginx/html/custom_404.html; sudo service nginx restart",
}
