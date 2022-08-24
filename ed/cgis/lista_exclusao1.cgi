#!/bin/sh

echo Content-type: text/html
echo

# crialista.cgi
# fabio@conectiva.com.br 
# qui mai  6 20:14:05 EST 1999
# Exclusão listas sistema de Educação a Distancia
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
	echo "<H2>Exclusão de Listas </H2>"
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

ExcluiLista () {
	/home/httpd/html/ed/cgis/lista-exclui $Lista > /dev/null
	if [ $? != "0" ]; then
		SaiErro "Erro na execução do /home/mailman/bin/rmlist -a $Lista.<BR> Entre em contato com o webmaster! <BR>" 
	fi
	echo "<BR>Lista $Lista excluída com sucesso!<BR>"
}

		if [ -z $Lista ]; then
			SaiErro "Voce deve informar o nome da lista"	
		fi
	
	if [ ! -f /home/mailman/bin/rmlist ]; then
		SaiErro "Não achei o /home/mailman/bin/rmlist <BR>Talvez a rpm do mailman  não foi instalada. entre em contato com o webmaster<BR>" 
	fi

	if [ ! -d /home/mailman/lists/$Lista ]; then
		SaiErro "<BR>Lista não  existe <BR>"
	else
		echo "excluindo lista $Lista ..."
		ExcluiLista
	fi


	rm $TMP
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"

