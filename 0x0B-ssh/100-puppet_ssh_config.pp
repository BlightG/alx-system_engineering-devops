# this is a comment
class ssh{
  file{ '/etc/ssh/sshd_config':
    ensure => present,
    owner  => 'root',
	group  => 'root',
	mode   => '0644',
  }
  service { 'ssh':
	ensure => 'running',
	enable => 'true',
  }
}
