# installing and configuring an Nginx server

package {'nginx':
  ensure => 'present',
}

file {'/var/www/html/index':
  ensure  => 'present',
  content => 'Hello World!',
}

file {'/usr/shar/nginx/html/custom_404':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n",
}

exec {'sed':
  path    => 'usr/bin/sed',
  command => "sed -i '/listen 80 default_server/a \\tlocation /redirect_me { \n \t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4' /etc/nginx/sites-enabled/default",
}
exec {'sed':
  path    => 'usr/bin/sed',
  command => "sed -i '3-0i\\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}' /etc/nginx/sites-enabled/default"
}
