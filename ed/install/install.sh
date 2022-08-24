
echo "1) alterar o /etc/httpd/conf/php3.ini, linha engine=1" 
echo "2) alterar o /etc/rc.d/init.d/postgres, colocar -i na linha:
	 su postgres -c '/usr/bin/postmaster -S -i -D/var/lib/pgsql'"

echo "3) criar o usuario nobody como abaixo:
su - postgres
#createuser nobody
Enter user's postgres ID or RETURN to use unix user ID: 99 ->
Is user \"nobody\" allowed to create databases (y/n) n
Is user \"nobody\" allowed to add users? (y/n) n
createuser: nobody was successfully added
don't forget to create a database for nobody"
echo "Sempre que atualizar a maquina , executar o comando:
       initdb --pgdata=/var/lib/pgsql --pglib=/usr/lib/pgsql 
	   instalar a rpm:
	   mod_php3-pgsql-3.0.9-4cl.i386.rpm "
echo "4) Retirar a senha do usuarios postgres no /etc/passwd ou /etc/shadow,
         para os scripts paraservidor e iniciaservidor " 
echo "chmod 777 /home/httpd/html/ed/materias/"
echo "chown -R nobody.nobody /home/httpd/html/ed"
echo "Copiar o /home/httpd/html/ed/cgis/websistema.cgi para o
      /home/httpd/cgi-bin/ed/"
echo "Copiar o /home/httpd/html/ed/cgis/web-sistema.cgi /home/httpd/cgi-bin/ed/"
echo "Copiar o /home/httpd/html/ed/cgis/unescape /usr/bin/"

echo "Incrementar o /etc/httpd/conf/access.conf com as seguintes linhas :
	<Directory /home/httpd/html/ed/professores/private>
	ForceType application/x-httpd-php3
	php3_auto_prepend_file /home/httpd/html/ed/professores/private/.logon.professores.phtml
	</Directory>"

echo "Alterar no /etc/httpd/conf/srm.conf a linha :
	  DirectoryIndex index.html index.htm index.shtml index.cgi index.phtml index.php3"  

echo "Alterar no /etc/httpd/conf/access.conf 
	no <Directory /home/httpd/html>
	colocar a Options ExecCGI "
echo "adicionar .phtml na linha:
	AddType application/x-httpd-php3 .php3 .phtml 
	"
echo "Alterar: 
access.conf:
<Directory /home/mailman>
AllowOverride None
Options ExecCGI Indexes FollowSymLinks
</Directory>        

srm.conf:ScriptAlias   /mailman/       /home/mailman/cgi-bin/
srm.conf:Alias /pipermail/ /home/mailman/archives/public/   
	"
