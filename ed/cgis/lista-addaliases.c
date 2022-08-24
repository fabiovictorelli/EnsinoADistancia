#include <stdio.h> 
#include <stdlib.h> 

#include <sys/types.h> 		/* para opendir() */
#include <sys/stat.h> 		/* para stat() */
#include <sys/time.h> 		/* para gettimeofday() */
#include <fcntl.h>			/* para open()*/
#include <dirent.h> 		/* para opendir() */
#include <unistd.h> 		/* para unlink () */
#include <errno.h> 			/* para unlink () */
#include <string.h> 		/* para strcpy () */
#include <time.h> 			/* para time () */
			                                 

#include "ed-defines.h"

main(int argc, char ** argv)
{
	char cmd [BUFSIZ];
	char buf [BUFSIZ];
	char lista [BUFSIZ];
	int fd,tam;
	char tempoaux[BUFSIZ]; 
	time_t tempo;
	struct tm *ptm;

	if ( argc < 2 ){
		printf("\nUsar %s <lista>\n",argv[0]);
		exit ( 1 );
	}
	if ( strlen (argv[1] ) > TAMMAXLISTA ) {
		printf("\nNome da lista: \n[%s]\n muito grande \n",argv[1]);
		exit ( 1 );
	}
	strcpy (lista,argv[1]);

	/* anti-racker =   aqui começa uns filtros de segurança */
	if ( strchr (lista, ' ') != NULL ) {
		printf("\nNome da lista: \n[%s]\n não pode conter caracter de espaço\n",argv[1]);
		exit ( 1 );
	}
	if ( strchr (lista, '&') != NULL ) {
		printf("\nNome da lista: \n[%s]\n não pode conter caracter &\n",argv[1]);
		exit ( 1 );
	}
	if ( strchr (lista, '<') != NULL ) {
		printf("\nNome da lista: \n[%s]\n não pode conter caracter <\n",argv[1]);
		exit ( 1 );
	}
	if ( strchr (lista, '>') != NULL ) {
		printf("\nNome da lista: \n[%s]\n não pode conter caracter >\n",argv[1]);
		exit ( 1 );
	}

/*
	printf ("Lista=%s\n",lista);
*/

	if ( ( fd = open( ALIASES, O_RDWR |O_APPEND ,0644) ) < 0 ) {
   		printf("\nErro abrindo  arquivo %s  ",ALIASES);
		exit ( 1 );
	}                                         
	
	if ( ( tempo=time(NULL) ) == (time_t)-1 ) {
   		printf("\nErro da data do sistmea  ");
		exit ( 1 );
	}                                         
	ptm=localtime(&tempo);
	sprintf(tempoaux,"%d/%02d/%d %d:%d hs",ptm->tm_mday,ptm->tm_mon+1,ptm->tm_year,ptm->tm_hour,ptm->tm_min);
	//printf("%s",tempoaux);


	sprintf ( buf , "

## %s mailing list
## criado por: %s  mailman
%s:                  \"|/home/mailman/mail/wrapper post %s\"
%s-admin:            \"|/home/mailman/mail/wrapper mailowner %s\"
%s-request:          \"|/home/mailman/mail/wrapper mailcmd %s\"
owner-%s:            %s-admin
%s-owner:            %s-admin

",lista,tempoaux,lista,lista,lista,lista,lista,lista,lista,lista,lista,lista);
            
	tam=strlen(buf);                             
	if ( write( fd, buf, tam ) != tam ) {
		printf("\nErro escrevendo no arq. %s ",ALIASES);
		exit ( 1 );
	}    
	close ( fd );   

	exit (0);

}
