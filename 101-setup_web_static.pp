# shell to puppet

exec { 'update':
    provider => shell,
    command => 'sudo apt-get -y update',
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
    provider => shell,
    command => 'rm /data/web_static/current',
}

exec { 'create_symbolic':
    provider => shell,
    command => 'sudo ln -s /data/web_static/releases/test/ /data/web_static/current',
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
    provider => shell,
    command => 'sudo chown -R ubuntu:ubuntu /data/',
    require => File['/data/'],
}

exec { 'start_nginx':
    provider => shell,
    command => 'sudo service nginx restart',
    require => File['/etc/nginx/sites-available/default'],
}
