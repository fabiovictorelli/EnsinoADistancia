#!/bin/sh

echo Content-type: text/html
echo
# qua mai 19 18:58:44 EST 1999
# fabio@conectiva.com.br 
# ter mai 18 19:09:10 EST 1999
# esclusao de usuarios sistema de Educação a Distancia

read QUERY_STRING


# ligar debug para teste
#
debug=0  

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

	echo "<BODY BGCOLOR=#FFFFFF>"
	echo "<H2>Exclusao de usuários de Listas </H2>"

SaiErro () {
	echo "<H1><FONT SIZE=+1 COLOR=red>ERRO!</FONT></H1>"
	echo "<H4>$*</H4><BR>"
	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"
	if [ -f $TMP ]; then
		rm $TMP
	fi
	exit 1
}

	if [ ! -f /home/mailman/bin/remove_members ]; then
		SaiErro "Não achei o /home/mailman/bin/remove_members <BR>Talvez a rpm do mailman  não foi instalada. entre em contato com o webmaster<BR>" 
	fi

	if [ -z $Lista ]; then
		SaiErro "Você  não informou a lista"
	fi

	if [ ! -d /home/mailman/lists/$Lista ]; then
		SaiErro "Não achei a lista $Lista cadastrada<BR>" 
	fi

	echo "<BR>"
	echo "<FORM ACTION=\"lista_usu_exclui2.cgi\" METHOD=\"post\">"
	echo "<INPUT TYPE=\"hidden\" NAME=\"lista\" VALUE=\"$Lista\">"
	echo "<SELECT NAME=\"usuario\" size=\"1\" maxlength=\"80\">"
	echo "<OPTION VALUE=\"\">Selecione o usuário "
	aux=`/home/mailman/bin/list_members $Lista`
	for var in $aux 
	do
		echo "<OPTION VALUE=\"$var\">$var "
	done
	echo "</SELECT>  "
	echo "<BR><INPUT TYPE=\"submit\" VALUE=\"exclui\"><BR>"
	echo "</FORM>  "

	echo "<FORM> <input type=\"button\" value=\"Retornar\" onClick=\"history.back()\"></FORM>"

