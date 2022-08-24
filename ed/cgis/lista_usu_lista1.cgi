#!/bin/sh

echo Content-type: text/html
echo
# lista_usu_listar1.cgi
# fabio@conectiva.com.br 
# ter mai 18 19:09:10 EST 1999
# lisstar usuários listas sistema de Educação a Distancia

read QUERY_STRING
debug=0 


aux=`echo $QUERY_STRING | sed -e 's/&/ /g' `



for var in $aux
do
    NameVar=`echo $var | cut -d"=" -f1`
    ConteudoVar=`echo $var | cut -d"=" -f2`

    if [ "$NameVar" = "lista" ]; then
        Lista=`echo $ConteudoVar | unescape`
    fi                                      
    if [ "$NameVar" = "tipolista" ]; then
        TipoLista=`echo $ConteudoVar | unescape`
    fi                                      
done


if [ $debug = "1" ]; then
    echo "aux=$aux, lista=$Lista, TipoLista=$TipoLista"
fi


	echo "<BODY BGCOLOR=#FFFFFF>"
	echo "<H2>Listagem dos usuários cadastradas nas Listas</H2>"

SaiErro () {
	echo "<H1><FONT SIZE=+1 COLOR=red>ERRO!</FONT></H1>"
	echo "<H4>$*</H4><BR>"
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	rm $TMP
	exit 1
}
ListaUsuarios () {

	lista=$1
	echo "<BR>"
	echo "<table border=1>"
	aux=`/home/mailman/bin/list_members $lista`
	for var in $aux 
	do
		echo "<TR><TD>$var</TD></TR> "
	done
	echo "</table>"
}

	if [ ! -d /home/mailman/lists ]; then
		SaiErro "Não achei o /home/mailman/lists<BR>Talvez a rpm do mailman  não foi instalada. entre em contato com o webmaster<BR>" 
	fi
	if [ ! -f /home/mailman/bin/list_members ]; then
		SaiErro "Não achei o /home/mailman/bin/list_members<BR>Talvez a rpm do mailman  não foi instalada. entre em contato com o webmaster<BR>" 
	fi


	if [ $TipoLista = "dalista" ]; then
		if [ -z $Lista ]; then
			SaiErro "Você nao informou o nome da lista"
		fi
		ListaUsuarios $Lista
	fi
	if [ $TipoLista = "todos" ]; then
		aux=`ls /home/mailman/lists`
		for var in $aux
		do    
			echo "<BR>$var"
			ListaUsuarios $var
		done
	fi

	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"

