#!/bin/sh

echo Content-type: text/html
echo

# web-sistema.cgi
# fabio@conectiva.com.br 
# qua set  2 17:21:56 EST 1998
# Manutenção no sistema de Educação a Distancia
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


Cabec () {
	echo "<BODY BGCOLOR=#FFFFFF>"
	echo "<H2>Criação de Listas </H2>"
}

TRACE()
{
	echo "Inicio do TRACE"
	echo "TITULO \nQUERY_STRING=$QUERY_STRING <BR>"
	echo "Sistema=$Sistema <BR>"
	echo "Fim do TRACE"
}
#
#-------------------2. LENDO AS VARIAVEIS -----------------------------------#
#
# atencao: nao mude a ordem destas variaveis abaixo pois depende da ordem
#          de QUERY_STRING

Cabec

if [ $debug = "1" ]; then
	echo "QUERY_STRING=$QUERY_STRING"
fi

aux=`echo $QUERY_STRING | sed -e 's/&/ /g' `

if [ $debug = "1" ]; then
	echo "aux=$aux"
fi


for var in $aux 
do
	NameVar=`echo $var | cut -d"=" -f1`
	ConteudoVar=`echo $var | cut -d"=" -f2`
	
	if [ "$NameVar" = "sistema" ]; then
		Sistema=`echo $ConteudoVar | unescape`
	fi
done

if [ $debug = "1" ]; then
	TRACE
fi
Debug () {
	if [ $debug = "1" ]; then
		echo "$1"
	fi
}

Ativa () {
	Debug "<BR> Entrei em  Ativa <BR>"
	rm -rf /tmp/.s.PGSQL.*
#	/etc/rc.d/init.d/postgresql start  2> /tmp/lixo.$$
	/home/httpd/html/ed/cgis/iniciaservidor 2> /tmp/lixo.$$
	if [ $? = "0" ]; then
		echo " postgresql iniciado com sucesso. "
	else
		Debug "`cat /tmp/lixo.$$` "
	fi
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	rm /tmp/lixo.$$
}
Desativa () {
	Debug "<BR> Entrei em  Desativa <BR>"
#	/etc/rc.d/init.d/postgresql stop  2> /tmp/lixo.$$
	/home/httpd/html/ed/cgis/paraservidor
	if [ $? = "0" ]; then
		echo " postgresql parado com sucesso. "
	else
		Debug "`cat /tmp/lixo.$$` "
	fi
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	rm /tmp/lixo.$$
}
Status () {
	Debug "<BR> Entrei em  Status <BR>"
	ps ax | grep postmaster | grep -v grep > /tmp/lixo.$$
	if [ $? = "0" ]; then
    	   echo "<BR>===================================================="
	   echo "<BR>Status do Sistema = postmaster está rodando no Conectiva Linux"
	   echo "<BR>pid do postmaster: `pidof postmaster` <BR>"
	   echo "`cat /tmp/lixo.$$ `"
	   echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	   echo "<BR>===================================================="
	else
    	   echo "<BR>===================================================="
	   echo "<BR>Status do Sistema = postmaster não está rodando <BR>"
	   echo "<BR>Retorne e entre na opção de Ativar Sistema<BR>"
	   echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	   echo "<BR>===================================================="

	fi
	rm /tmp/lixo.$$

}

case $Sistema in
	ativa ) Ativa ;;
	desativa ) Desativa ;;
	status ) Status ;;
esac

