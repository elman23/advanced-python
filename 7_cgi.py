#!/usr/bin/env python3

"""
sudo vim /etc/apache2/sites-enabled/000-default.conf

#DocumentRoot /var/www/html
DocumentRoot /var/www
<Directory /var/www/>
        Options ExecCGI Indexes FollowSymLinks MultiViews
        AllowOverride None
        Order allow,denyß
        allow from all
        AddHandler cgi-script .py
</Directory>
"""


def main():
    print("Content-type:text/html\r\n\r\n")
    print("<html><body>")
    print("<h1>It works!</h1>")
    for i in range(5):
        print("<p>Hello, World! Iteration " + str(i + 1) + "</p>")
    print("</body></html>")


if __name__ == '__main__':
    main()