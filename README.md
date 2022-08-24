# EnsinoADistancia
 Distance Learning with PHP PostgreSQL , shells, etc

Solução de ensino a distância via Internet para instituições de ensino superior com problemas de assiduidade professor/aluno.

Fábio Dorival Victorelli  e Eduardo Nissenbaum




   Abstract    Detectamos o problema de assiduidade professor/aluno no CEFET-PR ( instituição de ensino superior da área tecnológica) devido a fatores intrinsecos ao perfil da mesma como : Necessidade de ausências por período 
prolongados a trabalho de professores e alunos.
	Implementamos uma aplicação WEB que usa uma metodologia de ensino a distância e recursos multimídia para solucionar esse tipo de problema. 
Aspectos técnicos de comunicações e metodológicos de administração do ensino a distância são analisados nesse artigo.

   Index Terms ¾ Distance Learning. Internet, Web Server.


I. INTRODUCTION

    O Cefet-PR é uma instituição de ensino superior cujo perfil do curso de engenharia industrial é fortemente voltado para a prática tecnológica. Alem disso a maioria de seus alunos já são técnicos na área em que cursam a engenharia e portanto trabalham durante o curso.
    Por outro lado a maioria dos professores trabalham em empresas da área de suas matérias. Esse perfil, aliado às demandas modernas de viagens constantes no mercado de trabalho tecnológico, leva-nos ao problema de períodos
de faltas inevitáveis do aluno/professor dentro do calendário programado de  aulas.  
   A qualidade de ensino nas matérias onde o problema ocorre cai e propomos o uso de uma _FERRAMENTA_ metodologia de ensino a distância via Internet implementada em um servidor web da instituição, para professores e alunos que tenham previsão de baixa assiduidade durante o semestre da matéria em questão e que tenham acesso à microcomputadores de baixo custo ligados a Internet nos locais remotos onde se encontrem durante os períodos de ausência.
   O crescimento exponencial da Internet chegou a dezenas de milhões de servidores em todo o mundo e vem crescendo cada vez mais. O numero de Web sites dobra a cada 06 meses. Aplicações do tipo video-on-demand e distance learning incrementa o tráfego na Internet cada vez a taxa maiores.  Alguns sites recebem milhões de visitas por dia, e é comum estes sites terem uma taxa muito alta de repostas.





A. O servidor  e seus recursos administrativos

 Diante do que se tem hoje em tecnologia voltada para educação a distância, deveremos utilizar no sistema as seguintes aplicações:
* hipertexto (www),
*  transferência de arquivos (ftp),
* listas de discussão sobre diversos assuntos, via email,
* chats (software para conversação on-line entre um grupo de pessoas),
* vídeo conferência (refletor de vídeo conferência e cu-seeme),
* ferramenta de buscas (search engines) para busca de informação em outras universidades,
* correspondencia eletrônica (email).
* correio de vídeos. ( arquivos de imagem com  som gravados, com possíveis perguntas e respostas)   

    O projeto encontra-se em fase final de desenvolvimenteo e testes,  pretendemos que este software tenha acesso prático e de fácil uso por parte dos professores e alunos, como também um software de fácil manutenção pelo administrador identificado aqui como webmaster, que possa configurar permissões dar manutenção nas bases de professores, alunos e matérias cadastradas.
    O projeto proposto teria 04 areas: webmaster, matérias, professores e alunos. As interfaces de cada uma das áreas seriam:

    Professor
* Listas e grupos de discussão, de responsabilidade do professor
* Chats entre professores e aluno.
* Interface para um professor novo se cadastrar de maneira fácil.
* Interfaces para o professor enviar arquivo de aula(s).
* Interfaces para o professor enviar arquivo de vídeo(s).
* Interface para um professor criar uma matéria.
* Interface para um professor criar e dar manutenção numa lista de discussão.
* Refletor de vídeo conferência.



    Aluno
* Interface para cadastramento como aluno.
* Interface para a matrícula num curso de educação a distância.
* Interface de acesso às materias cadastradas pelo professor.
* Área pública de alunos para transferência de arquivos.
* Interface para assinar uma lista de discussão, cadastrada pelo professor.

    Matéria ( acesso do webmaster)
* . Interface para manutencao na base de materias, com( inclusao,alteracao,listagem e exclusao de uma materia)

    Webmaster ( administrador do sistema )
* Interface para ativar/desativar e verificar status do sistema.
* Interface para configurar o sistema, nos aspectos:
* linguagem
* diretório
* nivel de proteção da área do professor
* permissão de upload de arquivos textos para os alunos
* permissão de upload de arquivos de vídeos para os alunos
* configuração de tamanho máximo de arquivos para upload.
* configuração da disponibilidade de arquivos de vídeos no servidor.
* Interface p/ manutenção em vídeo conferência.
* Interface p/ manutenção das listas de discussão, com
* Criar lista
* Remover lista
* Editar arquivos de mensagem
* Incluir/Remover Usuários
* Listar Usuários                      
* Interface para manutenção na base de professores, com
* Incluir, Alterar, Excluir e Listar os professores cadastrados
* Interace para cadastramento de professores novos.
* Interface para manutenção na base de matérias, com
* Incluir, Alterar, Excluir e Listar as matérias cadastradas
* Interface para manutenção na base de alunos, com
* Incluir, Alterar, Excluir e Listar os alunos cadastrados


2.0 Análise de Performance Client/Server 
	Vamos considerar aqui uma Universidade com 1.000 computadores em 100 locais diferentes sendo salas de treinamento, laboratorios , etc.  e uma media de 6.000 alunos, sendo manha, tarde e noite, que totalize uma media de 02 alunos por computador. Embora nossa analise seja sobre o acesso remoto aos dados (educacao a distancia) eh interessante termos estes numeros para sabermos da proporcao.
	Consideraremos o acesso remoto utlizando o backbone internet para  acesso aos dados de educacao a distancia no servidor, onde 1.000 alunos fazem cursos a distancia utilizando um computador pessoal em casa, acessando os dados no  servidor. 
	O acesso aos dados no servidor sao 24 horas por dia nos 07 dias da semana. Uma media de 500 acessos ao dia . Ointenta porcento destes acessos sao feitos ao dia, num pico de 12 horas, ou seja ( 400 = 0.8 x 500). Entao o numero medio de acesso aos dados por hora neste periodo eh de 33.3 , ou seja um acesso a cada 1,8 minutos ( 01 minuto e 48 segundos ). O servidor eh uma maquina Unix ( Linux com kernel 2.36 ) com 02 discos IDE de 4,3 e 3,4 de 03
gigabytes, com 64 Mega de RAM, e um processador Pentium 200 MHZ. A comunicacao entre o servidor e o Roteador eh atraves de uma placa de rede de 10 megatibis, O roteador tem links com outras redes internas da universidade e tem acesso ao backbone internet sobre um link de 2 megabitis.
	Esta universidade tem outros 07 servidores www, ftp e email.
	Bom, eh logico que nao podemos considerar todo o link para o nosso servidor, pois existem varias outras aplicacoes em uso na universidade neste link, como email, ftp, listas de discussão, outras aplicacoes WWW, e
outros servicos oferecidos pela universidade. Entao, aqui teremos que decidir sob qual otica utilizaremos para dimensionar a banda do nosso servidor, ou seja a questao eh quanto da banda utilizaremos ou qual o tipo de servico que ofereceremos, visto que determinados servicos utilizam boa
parte da banda, por exemplo video conferencia precisariamos de 64 kbytes(???) fixos para cada aluno.
	Assumiremos entao que utilizaremos parcialmente a banda de 02 megabitis para a aplicação de educacao a distancia, a questao agora eh quanto teremos disponiveis para este servidor. Vimos anteriormente que temos em media
500 acessos www ao dia ou seja um a cada 1,8 minutos por cada um dos 400  alunos durante o dia. Com  certeza teremos varios acessos simultaneos, mas esturaremos aqui como se houesse somente 01 acesso por vez para simplificar o 
estudo. Mas quanto da banda permitiremos que este acesso possa chegar? 
	Decidimos utilizar em nosso servidor varios servicos como acesso www, transferencia de arquivos via ftp, listas de discussão via email  e principalmente troca de arquivos de video com tamanhos variados,  todos acima de 1 megabytes.
	Observando o comportamento medio de cada aluno chegamos a tabela I
	
                                                      TABLE I
AVERAGE OF BYTES TX PER EACH STUDENTE IN A DAY
Serviço 
Descrição da unidade
Quantidade  kbytes
www
ftp
email
vídeo

07 páginas de ikb
tx of text file
20 messages of 2 k
01 file of video per  week

          7
    250
      40
 2.500

		Total   2.797 kbytes 


   Desconsidermos aqui o tempo livre da banda, entre por exemplo a leitura de um email e outro, ou a leitura de uma pagina nova de aula.
   Tambem desconsideraremos o tempo de processamento, acesso ao disco pois o sistema utiliza 5 msec de CPU do cliente, 10 msec de CPU do servidor e leitura 10 blockos de 2048 bytes do disco do servidor, temos em tempo  medio de 9 msec de seek e 4,17 msec como media de tempo de latencia do disco.
 O tempo de processamento e acesso ao disco eh muito pequeno para ser considerado neste trabalho, ou seja:

Sd = AvgSeek + Avg Latency + TransfTime  ( pg 38 livro Web Performace)
     = avgSeek + AvgLatency + BlockSize/Transfer Rate
     = 0.009 + 0.00417 +2048/20,000,000 
     = 0.0133 segundos.

   Analisaremos entao o tempo real de uso da banda para podermos chegar no tamanho ideal da banda passante para a aplicação.
   Agora nos temos uma somatora em media de 2.797 kbytes por aluno,  que resulta em 2.843.648 bytes por aluno.

   Qmuso= Qmwww + Qmftp + Qmemail + Qmvideo
   Qmuso = 2797 kbytes.
	
   Como vimos que em media cada aluno tem direito a 1,8 minutos por dia, teriamos 108 segundos de uso e calculariamos a largura da banda para o sistema, sendo
Qmuso ( Quantidade de uso média por aluno) / Tmaluno ( tempo medio diario do aluno) 
   Larg Banda = Qmuso / Tmaluno
   Larg Banda = 2797 / 108 segundos
   Larg Banda = 25.7 kbytes por segundo    
   Larg Banda = 205,7 kbits por seg.

   Esta largura ( 205,7 kbits por seg. ) desconsiderando erros de transmissao e pedidos de retransmissao estaria razoavel para uma universidade que tem um link de 2 megabits , ou seja a aplicação do ensino a distancia usaria 10 por cento da largura total da banda da universidade.
   O problema que usualmente o aluno nao tem um modem de 205,7 kbits por segundo em casa, entao adminindo que em media o aluno tem um modem de 33,600 bits por segundo,  e contando com o melhor caso em que a comuni
cacao TCP/IP do aluno chegaria a universidade com esta media de transmissao  ( do roteador de seu ISP ate o roteador da universidade ) nosso tempo  medio de transmissao diario do aluno ficaria em ( 205,7 / 33,6 ) = a 6,12  vezes do tempo original que era de 1,8 minutos, ou seja , cada aluno teria direito a 11,02 minutos de uso diariamente do sistema.

***	 Aqui colocaremos o direito do aluno baixar somente 01 arq de video pela limitacao acima.

    Anatomia de uma transacao Web ( pg 77 do Web Performance)
   Outro tempo que devemos levar em consideracao eh o tempo que em sistemas distribuidos como o World Wide Web, quando algo acontece errado a responsabilidade da performance eh difundida sendo que eh dificel achar o 
verdadeiro responsavel. Entao o primeiro passo eh saber o que realmente acontece numa transacao.  
	Vamos analisar uma transacao completa em 03 principais componentes: browser, a rede e o servidor.
	
	FIGURA II ( ver pg 78 Web Performance )

Usuário      Browser Cliente          Rede            Servidor
	
Browser
* Qdo um usuário clica num hyperlink e pede um documento.
* O browser verifica no cache se existe o documento 
* requisitado
* O browser pede ao DNS [ara mapear o hostname para um 
* Endereco Ip	
* O cliente abre uma conexao TCP com o servidor
* O cliente envia uma requisicao HTTP para o servidor.

Rede
*  Normalmente eh o tempo dentre a rota do cliente ate o
servidor entre varios equipamentos como modems, rotea
dores, pontes, etc. 
		  
Rnetwork= Rn1 + Rn2

Servidor
* Uma requisicao chega do cliente
* O servidor analisa a requisicao de acordo com o protocolo HTTP.
* O servidor executa o metodo requisitado ( ex, GET )
* No caso de GET, o servidor le o arquivo do disco ou de sua memoria principal, caso esteje o documento no cache.
* Quando o arquivo foi completamente enviado o servidor fecha a conexao.
* The Server residence time Rserv, eh o tempo gasto para a execucao, aqui entra os varios componentes do servidor como , o tipo do processardor, disco e interface de placa de rede.
		
   Quando um documento esta no cache do cliente , eh facil dimensionar o tempo sendo somente a verificacao se esta no cache e leitura do arquivo em memoria ou cache do cliente.
   Quando o arquivo nao esta no cache do cliente, o tempo de Resposta ficaria ( Rr) da requisicao r sendo a soma do tempo de residencia de todos os recursos:
   Rr = Rbrowser + Rnetwork + Rserver
	




   FTP - tranferencia de arquivos de video usando FTP

   Segue abaixo uma analise de transferencia de arquivos de varios clientes 
  Hoje temos varios padroes de arquivos de video, utilizando mpeg3 teriamos arquivos em media de tamanho 1024 kbytes para cada 10 segundos.
tendo em vista que para o sistema em uso cada aluno poderia transferir  2500 kbytes de arquivos de video, terimos somente videos de 24 segundos de video ou seja , somente arquivos de videos pequenos.

   Segue estudo a parte.
	 
   Utilizando o software MediaStudio Video Capture, em uma maquina Intel Pentium com 32.248 KB de memoria, disco de 1.533 MB, e Monitor SVGA color configurado com resoluzao 800X600, Resolucao de 96,96 pixels/inch, 
16 bits per pixel,  quanto ao software de caputra de video tem
as seguintes configuracoes: 

	Video
	Frame Rate: 8,00   Frames/Sec 	
	Tamanho : 176 x 144 (QCIF)
	Cor  : Milhões ( 24 bits )
	Tempo : 10 segundos
	Compactação : Intel Indeo(R) Video Interactive

	Som
	Formato PCM
	attributes: 8.000 Hz; 8bit; Mono  8 KB/s

xxx
	arquivo ficou com  ???

	
=x=x=x=x=x=x
	mesmos atributos acima 
	TEMPO = 01 minuto
	tamanho teste.avi 1.048.576
=x=x=x=x=x=x
	mesmos atributos acima
	TEMPO = 02 minutos
	tamanho teste.avi 1.236.072
	
=x=x=x=x=x=x=x=x
	goodtime.avi   39.311.306 bytes com 03 minutos e 13 segundos
	2912 frames com tamanho de 176x144 (QCIF) 


CONCLUSÃO ( do trabalho individual)

    Esta pesquisa tem como propósito central o estudo da viabilidade de difusão da informação utilizando recursos tecnológicos via internet junto com a utilização de softwares de livre distribuição, que na maioria dos casos são gratuítos. Fazendo com que se torne viável para as aplicações das entidades de ensino público, reduzindo o investimento pelos orgãos competentes e auxiliando o educador ou o próprio aprendiz na estruturação de seus conhecimentos.

    Educacao a Distancia é um software de ensino, onde o professor passa/troca informacoes com alunos remotamente. A principio desenhado para ser utilizado a rede internet, embora muitas servicos como vídeo-conferência exigam uma
banda de dados maiores do que a existente hoje, o software traz um refletor para vídeo conferência, que podera ser configurado para rodar na rede local do servidor. Este projeto está sendo elaborado sob softwares free, sob licensa de uso GNU, sob Sistema Operacional Linux.

REFERENCES
 [1] Menascé Daniel A. and Almeida Virgílio A.F., "Capacity Planning For
	Web Performance Metrics, Models, & Methods" , 1998
[2] Transaction Processing Performance Council, http://www.tpc.org 



  
    
