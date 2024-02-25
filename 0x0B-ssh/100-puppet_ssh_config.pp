# this script creates sn ssh config file in ~/.ssh/config

file { '/home/red/.ssh/config':
ensure  => present,
content => "\
Host *
	Hostname 54.236.28.51
	User ubuntu
	IdentityFile /home/red/.ssh/school
",
}
