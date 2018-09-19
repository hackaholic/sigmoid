echo mysql-server-5.7 mysql-server/root_password password helloroot | debconf-set-selections
echo mysql-server-5.7 mysql-server/root_password_again password helloroot | debconf-set-selections
