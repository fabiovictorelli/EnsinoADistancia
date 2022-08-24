#include <stdio.h> 
#include <stdlib.h> 

main()
{
	char cmd [BUFSIZ];
	strcpy ( cmd , "/etc/rc.d/init.d/postgresql stop");
	system ( cmd );
	strcpy ( cmd , "rm -rf /tmp/.s.PGSQL.*");
	system ( cmd );
}
