# this is a comment
ssh_authorized_key{ 'root@magpie.example.com':
  ensure => present,
  user   => 'root',
  target => '~/.ssh/school',
  type   => 'ssh-rsa',
}
