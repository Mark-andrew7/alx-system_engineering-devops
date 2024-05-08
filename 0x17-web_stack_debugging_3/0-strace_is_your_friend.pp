# 0-strace_is_your_friend.pp

exec { 'fix-apache-500-error':
  command => 'curl -sI 127.0.0.1:80',
  path    => ['/usr/bin'],
  creates => '/tmp/curl_output.txt',
}

file { '/tmp/curl_output.txt':
  ensure => file,
}

service { 'apache2':
  ensure    => 'running',
  enable    => true,
  subscribe => File['fix-apache-500-error'],
}
