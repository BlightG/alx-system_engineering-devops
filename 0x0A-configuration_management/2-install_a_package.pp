exec { 'apt-get update':
  command => '/usr/bin/apt-get update',
  before => Exec[ 'python -m venv venv' ],
}

exec { 'python -m venv venv':
  command => '/usr/bin/python3 -m venv venv',
}

exec { 'source venv/bin/activate':
  source => 'venv/bin/activate',
  require => Exec[ 'python -m venv venv']
}

exec { 'pip3 install flask':
  command => 'pip3 flask=2.1.0',
  require  => Exec[ 'source venv/bin/activate' ],
}
