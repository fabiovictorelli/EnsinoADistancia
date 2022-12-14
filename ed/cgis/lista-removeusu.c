#include <stdio.h> 
#include <stdlib.h> 

#include <errno.h> 		 	/* para unlink () */
#include <string.h> 		/* para strcpy () */
#include <unistd.h> 		/* para execl () */
			                                 

#include "ed-defines.h"

main(int argc, char ** argv)
{
	char cmd [BUFSIZ];
	char buf [BUFSIZ];
	char lista [BUFSIZ];
	char email [BUFSIZ];
	int ret;


	if ( argc < 3 ){
		printf("\nUsar %s <lista> <email>\n",argv[0]);
		exit ( 1 );
	}
	if ( strlen (argv[1] ) > TAMMAXLISTA ) {
		printf("\nNome da lista: \n[%s]\n muito grande \n",argv[1]);
		exit ( 1 );
	}
	strcpy (lista,argv[1]);
	strcpy (email,argv[2]);

	/* anti-racker =   aqui come?a uns filtros de seguran?a */
	if ( strchr (lista, '&') != NULL ) {
		printf("\nNome da lista: \n[%s]\n n?o pode conter caracter &\n",argv[1]);
		exit ( 1 );
	}
	if ( strchr (lista, '<') != NULL ) {
		printf("\nNome da lista: \n[%s]\n n?o pode conter caracter <\n",argv[1]);
		exit ( 1 );
	}
	if ( strchr (lista, '>') != NULL ) {
		printf("\nNome da lista: \n[%s]\n n?o pode conter caracter >\n",argv[1]);
		exit ( 1 );
	}

	sprintf ( buf,"/home/mailman/bin/remove_members %s %s ", lista,email);
	ret=system(buf);
	if ( ret == 0 ) {
		exit (0);
	}
	else {
		printf("\nErro na exclus?o do usu?rio\n");
		exit (1);
	}

	exit (0);

}
