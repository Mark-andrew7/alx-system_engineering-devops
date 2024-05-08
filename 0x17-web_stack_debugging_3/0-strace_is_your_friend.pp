# 0-strace_is_your_friend.pp

exec { 'fix-apache-500-error':
  command => 'strace -o /tmp/strace.out -s 2000 -f -e trace=write curl 127.0.0.1:80 2>&1 | grep Holberton',
  path    => '/usr/bin',
  creates => '/tmp/strace.out',
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  subscribe  => Exec['fix-apache-500-error'],
}
