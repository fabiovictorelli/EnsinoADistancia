#!/bin/sh

echo Content-type: text/html
echo

# crialista.cgi
# fabio@conectiva.com.br 
# qui mai  6 20:14:05 EST 1999
# Criação listas sistema de Educação a Distancia
# 

#
#-------------------1. LENDO  QUERY_STRING -----------------------------------#
#
#--Captura dados da entrada padrao e armazena QUERY_STRING--#
#--Recurso usado pelo metodo POST--#
read QUERY_STRING 


# ligar debug para teste
#
debug=0

TMP=/tmp/crialista.$$

Cabec () {
	echo "<BODY BGCOLOR=#FFFFFF>"
	echo "<H2>Criação de Listas </H2>"
}

TRACE()
{
	echo "Inicio do TRACE"
	echo "TITULO \nQUERY_STRING=$QUERY_STRING <BR>"
	echo "Lista=$Lista <BR>"
	echo "Mantenedor=$Mantenedor <BR>"
	echo "Senha=$Senha <BR>"
	echo "Fim do TRACE<BR>"
}
#
#-------------------2. LENDO AS VARIAVEIS -----------------------------------#

Cabec

aux=`echo $QUERY_STRING | sed -e 's/&/ /g' `

if [ $debug = "1" ]; then
	echo "aux=$aux"
fi


for var in $aux 
do
	NameVar=`echo $var | cut -d"=" -f1`
	ConteudoVar=`echo $var | cut -d"=" -f2`
	
	if [ "$NameVar" = "lista" ]; then
		Lista=`echo $ConteudoVar | unescape`
	fi

	if [ "$NameVar" = "maintainer" ]; then
		Mantenedor=`echo $ConteudoVar | unescape`
	fi

	if [ "$NameVar" = "senha" ]; then
		Senha=`echo $ConteudoVar | unescape`
	fi

done

if [ $debug = "1" ]; then
	TRACE
fi

Debug () {
	if [ $debug = "1" ]; then
		echo "$*"
	fi
}

SaiErro () {
	echo "<H1><FONT SIZE=+1 COLOR=red>ERRO!</FONT></H1>"
	echo "<H4>$*</H4><BR>"
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	rm $TMP
	exit 1
}

AddLista () {

		if [ ! -f /home/httpd/html/ed/cgis/lista-addlista ]; then
				SaiErro "Não achei o /home/httpd/html/ed/cgis/lista-lista <BR>Entre em contato com o webmaster.<BR>" 
		fi


    /home/httpd/html/ed/cgis/lista-addlista $Lista $Mantenedor $Senha > $TMP
	if [ $? != "0" ]; then
		SaiErro  "erro na criação da lista $Lista"
	else
		echo "<BR> Lista $Lista Criada com sucesso.  "
		if [ $debug = "1" ]; then
			aux=`cat $TMP`
			Debug $aux
		fi
	fi
}

GravaAliases () {

grep ^$Lista: /etc/aliases > /dev/null
if [ $? = "0" ]; then
	SaiErro "Impossível cadastrar lista com o nome $Lista, pois já existe entrada no /etc/aliases<BR> com este nome. Tente cadastrar lista com outro nome ! <BR>" 
fi


if [ ! -f /home/httpd/html/ed/cgis/lista-addaliases ]; then
		SaiErro "Não achei o /home/httpd/html/ed/cgis/lista-addaliases <BR>Entre em contato com o webmaster  informando o erro <BR>" 
fi

/home/httpd/html/ed/cgis/lista-addaliases $Lista
                                     
if [ ! -f /usr/bin/newaliases ]; then
		SaiErro "Não consegui executar o  programa /usr/bin/newaliases <BR>Entre em contato com o webmaster  informando o erro <BR>" 
fi

/usr/bin/newaliases > /dev/null
if [ $? != "0" ]; then
	SaiErro "Entre na execução do newaliases entre em contato com o webmaster! <BR>" 
fi

}

	if [ ! -f /home/mailman/bin/newlist ]; then
		SaiErro "Não achei o /home/mailman/bin/newlist <BR>Talvez a rpm do mailman  não foi instalada. entre em contato com o webmaster<BR>" 
	fi

	if [ -d /home/mailman/lists/$Lista ]; then
		SaiErro "<BR>Lista já existe <BR>"
	fi

	AddLista $Lista $Mantenedor $Senha

	GravaAliases

	rm $TMP
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"

