# this is a comment
ssh_authorized_key{ 'ubuntu@54.144.137.83':
  ensure => present,
  target => '~/.ssh/school',
  type   => 'ssh-rsa',
  key    => $public_key,
}
