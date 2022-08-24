#include <stdio.h> 
#include <stdlib.h> 

#include <sys/types.h> 		/* para opendir() */
#include <sys/stat.h> 		/* para stat() */
#include <dirent.h> 		/* para opendir() */
#include <unistd.h> 		/* para unlink () */
#include <errno.h> 		/* para unlink () */

#include "ed-defines.h"

char * DescobreNomeArqTempSql()
{
	char tmp[BUFSIZ];
	char *ptmp=&tmp[0];
	DIR * dir;
	struct dirent * dirp;

	strcpy(tmp,TMPDIR);

	if ( ( dir=opendir(tmp) ) == NULL ) {
		return NULL;
    }

	while ( 1 ) {
		if ( ( dirp=readdir(dir) ) == NULL ) {
			return NULL;
		}

		/*	printf("\nli arquivo %s",dirp->d_name); */

		if ( ! ( strncmp ( TMPSQL, dirp->d_name , 9 ) ) ) {
			printf("\narquivo temporario=%s",dirp->d_name);
			strcpy(tmp,TMPDIR);
			strcat(tmp,"/" );
			strcat(tmp,dirp->d_name);
			return ( ptmp );
		}
	}
	return NULL;
}

int RemoveArqTemp(char * nometemp)
{
	
	struct stat buf;
	struct stat *pbuf;

	pbuf=&buf;

	printf ("\n Removendo %s\n",nometemp);
	if (access(nometemp, W_OK) == ERRO) {
		printf ("\n Erro em access() %s, errno=%d\n",nometemp,errno);
		return ERRO;
	}
	if (lstat(nometemp, pbuf) == ERRO) {
		printf ("\n Erro em lstat() %s, errno=%d\n",nometemp,errno);
		return ERRO;
	}

	if ((unlink(nometemp ) ) == ERRO ){
		printf ("\n Erro na Remocao do arquivo %s errno=%d\n",nometemp,errno);
		perror ("Erro");
		return ERRO;
	}
	else {
		printf ("\n Removido %s com sucesso! \n",nometemp);
		return OK;
	}

}

main()
{
	char cmd [BUFSIZ];
	char * nometmp; 

   if ( ( nometmp=DescobreNomeArqTempSql() )  == NULL ) {
		printf ("\nNao existe arquivo temporario /tmp/.s.PGSQL.porta do SQL<BR>\n"); 
	}
	else {
		if (  ( RemoveArqTemp(nometmp) ) == ERRO ) {
			printf("\n Erro removendo arquivo %s !!!\n",nometmp);
		}
	}
		

	strcpy ( cmd , "/etc/rc.d/init.d/postgresql start"  );
	system ( cmd );
}
