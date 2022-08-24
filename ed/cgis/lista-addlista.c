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
	char mantenedor [BUFSIZ];
	char senha [BUFSIZ];
	int ret;


	if ( argc < 4 ){
		printf("\nUsar %s <lista> <mantenedor> <senha>\n",argv[0]);
		exit ( 1 );
	}
	if ( strlen (argv[1] ) > TAMMAXLISTA ) {
		printf("\nNome da lista: \n[%s]\n muito grande \n",argv[1]);
		exit ( 1 );
	}
	strcpy (lista,argv[1]);
	strcpy (mantenedor,argv[2]);
	strcpy (senha,argv[3]);

	/* anti-racker =   aqui começa uns filtros de segurança */
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
	printf ("<BR>Lista=%s, Mantenedor=%s, Senha=%s\n",lista,mantenedor,senha);
	sprintf ( buf,"su mailman -c \"/home/mailman/bin/newlist %s %s %s \" ",lista, mantenedor, senha );
	*/
	sprintf ( buf,"/home/mailman/bin/newlist %s %s %s ",lista, mantenedor, senha );
	ret=system(buf);
	if ( ret == 0 ) {
		exit (0);
	}
	else {
		printf("\nErro no cadastramento da lista\n");
		exit (1);
	}

}
