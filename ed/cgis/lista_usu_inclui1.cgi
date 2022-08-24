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

TMP=/tmp/lista_usu_inclui1.cgi_.$$

Cabec () {
	echo "<BODY BGCOLOR=#FFFFFF>"
	echo "<H2>Inclusão de usuário na lista</H2>"
}

TRACE()
{
	echo "Inicio do TRACE"
	echo "TITULO \nQUERY_STRING=$QUERY_STRING <BR>"
	echo "Lista=$Lista <BR>"
	echo "Email=$Email <BR>"
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

	if [ "$NameVar" = "email" ]; then
		Email=`echo $ConteudoVar | unescape`
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

AddUsuLista () {
	
	if [ -z "$Lista" ]; then
		SaiErro "Deve-se informar o nome da lista "	
	fi
	if [ -z "$Email" ]; then
		SaiErro "Deve-se informar o email para ser cadastrado na lista $Lista "	
	fi

#	verificando se o usuário já está cadastrado
	/home/mailman/bin/list_members $Lista | grep $Email > /dev/null 
	if [ $? = "0" ]; then
		SaiErro "Usuário $Email já está cadastrado na lista $Lista"
	fi
	
#	cadastrando o  o usuário
	echo "$Email" > $TMP
	if [ ! -f $TMP ]; then
		SaiErro  "Impossível criar arquivo temporário $TMP, avise o webmaster"
	fi

#	/home/mailman/bin/add_members -n $TMP $Lista
	/home/httpd/html/ed/cgis/lista-addusu $Lista $TMP
	if [ $? != "0" ]; then
		SaiErro  "erro no cadastramento do usuário $Email na  lista $Lista"
	else
		echo "<BR> Usuário $Email cadastrado na lista $Lista com sucesso."
	fi
	rm $TMP
}

	if [ ! -f /home/mailman/bin/add_members ]; then
		SaiErro "Não achei o /home/mailman/bin/add_members <BR>Talvez a rpm do mailman  não foi instalada. entre em contato com o webmaster<BR>" 
	fi

	AddUsuLista $Lista $Email

	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
