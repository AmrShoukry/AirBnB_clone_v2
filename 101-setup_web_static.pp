# shell to puppet

exec { 'update':
    command => 'sudo apt-get -y update',
    path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['update'],
}

file { '/data/':
    ensure => 'directory',
}

file { '/data/web_static/':
    ensure => 'directory',
}

file { '/data/web_static/releases/':
    ensure => 'directory',
}

file { '/data/web_static/shared/':
    ensure => 'directory',
}

file { '/data/web_static/releases/test/':
    ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
    ensure => 'file',
    content => "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
"
}

exec { 'remove_symbolic':
    command => 'rm /data/web_static/current',
    path    => ['/usr/bin', '/bin'],
}

exec { 'create_symbolic':
    command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
    path    => ['/usr/bin', '/bin'],
    require => Exec['remove_symbolic'],
}

file { '/etc/nginx/sites-available/default':
    ensure => 'file',
    content => "
        server {
            listen 80 default_server;
            listen [::]:80 default_server;

            root /var/www/;
            index index.html index.htm index.nginx-debian.html;
            server_name _;

            location /hbnb_static {
                alias /data/web_static/current/;
            }
        }"
}

exec { 'set_ownership':
    command => 'sudo chown -R ubuntu:ubuntu /data/',
    path    => ['/usr/bin', '/bin'],
    require => File['/data/'],
}

exec { 'start_nginx':
    command => 'sudo service nginx restart',
    path    => ['/usr/bin', '/bin'],
    require => File['/etc/nginx/sites-available/default'],
}
