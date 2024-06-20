### Treeinamento MQ

Sequência de passos para seguir no laboratório

- Processo de instalação do MQ
- Estrutura de diretórios Windows
- Estrutura de diretórios Linux
- Comando para mostrar versão do MQ
- Comando para mostrar qmgr em execução 
- Criação básica de um qmgr
- Deleção de um qmgr
- Criação de um qmgr e listar algumas configurações
- Criar uma fila 
- Limpar uma fila
- Deletar uma fila
- Verificar profundidade da fila  
- Verificar  profundidade atual
- Alterar a profundidade da fila
- Alterar atributo da fila  de put/get
- Criar um alias apontando para fila
- Criar um aliás apontando para tópico 
- Alterar o alias para outra fila
- Configuração TLS
- Executar backup do IBM MQ

### Lab 1: Instalação e Configuração Inicial do IBM MQ

Objetivo: Instalar o IBM MQ e configurar um ambiente básico.

Passo 01

	-	Baixe a versão apropriada do IBM MQ do site da IBM.
	-	Siga as instruções para instalar o IBM MQ no seu sistema operacional (Windows/Linux).
	-	Abra um terminal ou prompt de comando.
	-	Execute o comando para criar um Queue Manager:
    crtmqm QM.01

		
	- Inicie o Queue Manager:
   strmqm QM.01

  - Desativar a autenticação
    - Conecte no IBM MQ
    runmqsc

  


	3.	Criação de uma Fila (Queue):
	•	Abra o IBM MQ Explorer ou use a linha de comando.
	•	Crie uma fila chamada QL.TESTE:

runmqsc QM.01
DEFINE QLOCAL('QL.TESTE')


	4.	Verificação da Configuração:
	•	Verifique se o Queue Manager e a fila foram criados corretamente usando:

DISPLAY QMGR
DISPLAY QUEUE(QL.TESTE)


### Lab 2: Colocar e Obter Mensagens em uma Fila

Objetivo: Aprender a colocar mensagens em uma fila e obter mensagens de uma fila.

Passos:

	1.	Colocar Mensagens em uma Fila:
	•	Use o utilitário amqsput para colocar mensagens na fila QL.TESTE:

amqsput QL.TESTE QM.01

	1.	
	•	Digite algumas mensagens e pressione Enter após cada mensagem. Pressione Ctrl+D (Linux) ou Ctrl+Z (Windows) para terminar.
	2.	Obter Mensagens de uma Fila:
	•	Use o utilitário amqsget para obter mensagens da fila QL.TESTE:

amqsget QL.TESTE QM.01


	3.	Verificação das Mensagens:
	•	Verifique se as mensagens foram corretamente colocadas e obtidas da fila.

### Lab 3: Configuração de um Canal e Comunicação entre Queue Managers

Objetivo: Configurar canais de comunicação entre dois Queue Managers.

Passos:

	1.	Criação de um Segundo Queue Manager:
	•	Crie um segundo Queue Manager chamado QM2:

crtmqm QM2
strmqm QM2


	2.	Configuração dos Canais:
	•	Configure um canal de envio no QM.01:

runmqsc QM.01
DEFINE CHANNEL('QM.01.TO.QM2') CHLTYPE(SDR) CONNAME('localhost(1415)') XMITQ('QM2')

	2.	
	•	Configure um canal de recepção no QM2:

runmqsc QM2
DEFINE CHANNEL('QM.01.TO.QM2') CHLTYPE(RCVR)


	3.	Configuração de Filas de Transmissão e Fila Remota:
	•	Configure uma fila de transmissão no QM.01:

runmqsc QM.01
DEFINE QLOCAL('QM2') USAGE(XMITQ)

	3.	
	•	Configure uma fila remota no QM.01 que aponta para uma fila local no QM2:

runmqsc QM.01
DEFINE QREMOTE('REMOTE.Q1') RNAME('Q1') RQMNAME('QM2') XMITQ('QM2')

	3.	
	•	No QM2, configure a fila local Q1:

runmqsc QM2
DEFINE QLOCAL('Q1')


	4.	Teste de Comunicação:
	•	Coloque uma mensagem na fila remota REMOTE.Q1 no QM.01:

amqsput REMOTE.Q1 QM.01

	4.	
	•	Verifique se a mensagem chegou na fila Q1 no QM2:

amqsget Q1 QM2



### Lab 4: Configuração de Triggering para Processamento Automático de Mensagens

Objetivo: Configurar triggering para iniciar automaticamente um aplicativo quando uma mensagem chega em uma fila.

Passos:

	1.	Criação da Fila de Aplicação e Trigger:
	•	Crie uma fila chamada APP.QUEUE no QM.01:

runmqsc QM.01
DEFINE QLOCAL('APP.QUEUE') TRIGGER TRIGTYPE(FIRST) INITQ('INIT.QUEUE')

	1.	
	•	Crie uma fila de inicialização chamada INIT.QUEUE:

runmqsc QM.01
DEFINE QLOCAL('INIT.QUEUE')


	2.	Configuração do Process Definition:
	•	Defina um processo que será chamado quando o trigger for acionado:

runmqsc QM.01
DEFINE PROCESS('MY.PROCESS') APPLICID('/path/to/application')


	3.	Configuração do Trigger Monitor:
	•	Inicie um monitor de trigger para a fila INIT.QUEUE:

runmqtrm -m QM.01 -q INIT.QUEUE


### Lab 5: Perssionamento básico no IBM MQ





	4.	Teste do Trigger:
	•	Coloque uma mensagem na fila APP.QUEUE e verifique se o aplicativo definido no processo é executado automaticamente:

amqsput APP.QUEUE QM.01
