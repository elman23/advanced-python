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

Put this script in /var/www
GET on http://IP/7_cgi_2.py
"""


import cgi


def main():
    print("Content-type:text/html\r\n\r\n")
    print("<html><body>")
    print("<h1>It works!</h1>")
    
    form = cgi.FieldStorage()
    
    if form.getvalue("name"):
        name = form.getvalue("name")
        print("<p> Hello " + name + "!</p>")
    else:
        print("<p> Hello unknown!</p>")

    if form.getvalue("happy"):
        print("<p>I'm glad that you're happy!</p>")

    if form.getvalue("sad"):
        print("<p>I'm so sorry that you're sad...</p>")

    print("<form method='post' action='7_cgi_2.py'>")
    print("<p>Name: <input type='text' name='name' /></p>")
    print("<input type='checkbox' name='happy' /> Happy")
    print("<input type='checkbox' name='sad' /> Sad")
    print("<input type='submit' name='Submit' />")
    print("</form>")

    print("</body></html>")


if __name__ == '__main__':
    main()