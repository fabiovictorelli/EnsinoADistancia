# EnsinoADistancia
 Distance Learning with HTML, PHP, PostgreSQL, shells, etc

Educacao a Distancia é um software de ensino via Web, onde o professor passa/troca informacoes com alunos remotamente. A principio desenhado para ser utilizado a rede internet, embora muitas servicos como vídeo-conferência exigam uma  banda de dados maiores do que a existente hoje, o software traz um refletor para vídeo conferência, que podera ser configurado para rodar na rede local do servidor. Este projeto está sendo elaborado sob softwares free, sob licensa de uso GNU, sob Sistema Operacional Linux.

Fábio Dorival Victorelli  e Eduardo Nissenbaum, 1997


A. O servidor  e seus recursos administrativos

 Diante do que se tem hoje em tecnologia voltada para educação a distância, deveremos utilizar no sistema as seguintes aplicações:
* hipertexto (www),
* transferência de arquivos (ftp),
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

B. SOFTWARES NECESSARIOS: 
* Servidor Linux
* HTTPD (Apache)
* PHP3 
* PostgreSQL  

C. INSTALACAO
  Veja diretorio ed/install os scripts install.sh e cria_base
    
