exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
}

file {'~/flask_folder':
  ensure => 'directory',
  cwd =>'~/flask_folder',
}

exec {
  
}

package { 'flask':
  ensure   => '2.1.0'
  provider => 'pip'
  require  => Exec['apt-get update'],
}
