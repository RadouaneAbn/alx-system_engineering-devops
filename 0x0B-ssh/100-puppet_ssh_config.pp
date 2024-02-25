# this script creates sn ssh config file in ~/.ssh/config

exec { 'ssh_config':
  command => 'echo "Match ubuntu\n  Host *\n    User ubuntu\n    Hostname 54.236.28.51\n    IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config',
  provider => 'shell'
}
