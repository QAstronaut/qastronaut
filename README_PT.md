# QAstronaut

Bem-vindo ao **QAstronaut, Sua Solução para Testes de API com Agilidade!**

![GitHub Logo](/images/logo_qastronaut.png)

O QAstronaut é um projeto em desenvolvimento que visa automatizar a execução e criação de suítes de testes. Este repositório serve como um espaço central para o desenvolvimento, documentação e colaboração.

## Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuindo](#contribuindo)
- [Agradecimentos](#agradecimentos)
- [Licença](#licença)

## Visão Geral

O **QAstronaut** é um projeto revolucionário que simplifica e acelera o processo de criação de suítes de teste para APIs, em parceria com a conhecida ferramenta **Postman**. Nossa abordagem inovadora é baseada na integração perfeita com o Postman via **API Key**, permitindo que você crie suítes de teste de forma mais ágil e eficiente, seguindo heurísticas confiáveis. Mas, afinal, o que torna o QAstronaut tão especial?

### O Que é o QAstronaut?

O **QAstronaut** é uma plataforma que visa simplificar a complexidade dos testes de APIs. Ele é projetado para equipes de desenvolvimento e testes que desejam automatizar o processo de testes e garantir a qualidade de suas APIs de maneira mais rápida e confiável. Com a ajuda do QAstronaut, você poderá criar, organizar e executar suítes de teste de API com facilidade, economizando tempo e esforço.

### Qual é o Propósito do QAstronaut?

O propósito do **QAstronaut** é oferecer uma solução abrangente para as necessidades de testes de API. O projeto visa:

1. **Aceleração do Desenvolvimento:** Reduza o tempo necessário para criar e manter suítes de teste de API, permitindo que sua equipe se concentre em outras tarefas críticas.

2. **Testes Confiáveis:** Utilize heurísticas confiáveis para estruturar seus testes, garantindo que suas APIs funcionem como esperado.

3. **Integração Perfeita com o Postman:** A integração com o Postman via API Key simplifica o processo de criação de testes, aproveitando a popularidade e a funcionalidade avançada dessa ferramenta.

4. **Colaboração Eficiente:** Facilite a colaboração entre desenvolvedores e testadores, garantindo que todos estejam na mesma página e que os testes estejam sempre atualizados.

### Por Que se Interessar Pelo QAstronaut?

O **QAstronaut** oferece benefícios significativos para qualquer equipe envolvida no desenvolvimento de APIs. Aqui estão algumas razões pelas quais você deve considerar utilizar nossa plataforma:

- **Economia de Tempo:** Reduza o tempo gasto na criação de testes de API, acelerando o ciclo de desenvolvimento.

- **Melhoria da Qualidade:** Utilize heurísticas e boas práticas para garantir testes eficazes e confiáveis.

- **Simplicidade e Facilidade de Uso:** Não é necessário ser um especialista em testes de API para aproveitar os recursos do QAstronaut.

- **Integração com o Postman:** Aproveite o poder e a versatilidade do Postman com uma integração direta e simplificada.

- **Aumento da Colaboração:** Promova a colaboração entre equipes de desenvolvimento e teste, garantindo uma compreensão compartilhada dos requisitos e testes.

Em resumo, o **QAstronaut** é a solução perfeita para quem busca simplificar e aprimorar o processo de testes de API, permitindo que você alcance seus objetivos de desenvolvimento com mais rapidez e confiança. Junte-se a nós e embarque nesta jornada em direção a testes de API mais ágeis e eficazes com o QAstronaut!

> Se você não está familiarizado com a ferramenta Postman, recomendamos a leitura da sua [documentação](https://learning.postman.com/docs/getting-started/overview/). Isso pode ser útil para se familiarizar com a ferramenta que integramos.


## Instalação

Siga estas instruções para baixar, configurar e executar o QAstronaut em seu ambiente.

### Pré-requisitos

Certifique-se de ter os seguintes requisitos atendidos antes de começar:

- [Postman](https://www.postman.com/downloads/)
- [Python3+](https://www.python.org/)
- [Bibliotecas Python](requirements.txt)

### Passos de Instalação

1. Clone o repositório QAstronaut do GitHub para o seu sistema:

   ```bash
   git clone https://github.com/QAstronaut/qastronaut.git
   ```

2. Com o **Python instalado**, execute no diretório *qastronaut/* o seguinte comando:

    ```bash
    pip install -r requirements.txt
    ```

3. Em seguida, execute o comando:

    ```bash
    python qastronaut.py --init
    ```
    > **Alerta:** em alguns casos, pode ser necessário usar `python3` em vez de `python` para chamar o interpretador Python 3 no Linux.

    Este comando irá solicitar a sua [API Key](https://learning.postman.com/docs/developer/postman-api/authentication/) e criará as pastas de configuração do QAstronaut.

    Após esse processo, o QAstronaut está pronto para uso.



## Uso

Depois da instalação você terá uma estrutura de pastas parecida com essa:

```bash
qastronaut/
│
├── config/
│   ├── requests/
│   │   └── curl.txt
│   ├── requests_names/
│   │   └── user_requests.txt
│   ├── tests/
│   │   └── body/
│   │       ├── empty.txt
│   │       ├── invalid.txt
│   │       ├── nonexistent.txt
│   │       ├── null.txt
│   │       └── size.txt
│   └── api_key.json
│
├── functions/
│   ├── create_postman.py
│   ├── fetch_data_postman.py
│   └── welcome.py
│
├── images/
│   └── logo_qastronaut.png
│
├── unit_tests/
│   ├── test_create_postman.py
│   ├── test_fetch_data_postman.py
│   └── test_welcome.py
│
├── qastronaut.py
├── README.md
├── requirements.txt
└── LICENSE 
```

**Lembre-se**: A API Key é um componente essencial para o pleno funcionamento do QAstronaut. Se você a alterou ou não a forneceu durante a instalação, é importante que atualize o arquivo `api_key.json` incluindo uma chave válida.

## Configuração de Testes e Cenários

Toda a interação com o QAstronaut será realizada via linha de comando para execução. No ponto de configuração, focaremos no diretório `config/`.

### Adicionando uma Solicitação HTTP

Para incluir uma solicitação HTTP, siga o procedimento abaixo:

1. Salve o cURL da solicitação desejada e cole o mesmo no arquivo com o nome `curl.txt`.
2. `curl.txt` está no diretório `config/requests/`.

Dessa forma, garantimos uma configuração adequada para as solicitações HTTP em seu ambiente de testes.


> Atualmente, o QAstronaut é capaz de testar somente um endpoint por vez. Se você precisar testar múltiplos endpoints, será necessário substituir o arquivo curl.txt a cada vez.

#### Configuração dos testes

 No diretório `config/tests/`, você encontrará todos os scripts JavaScript de teste disponíveis para o QAstronaut, referente a cada cenário de teste que o QAstronaut é capaz de criar. É essencial observar que esta lista de testes está em constante evolução e requer alterações para se adequar aos requisitos do endpoint planejado. Certifique-se de manter esses scripts atualizados para garantir uma cobertura adequada de testes.

Caso prefira, você tem a opção de criar seu próprio script de teste para os cenários listados na pasta de testes, sobrescrevendo os existentes. Essa abordagem possibilita uma personalização completa de acordo com as suas necessidades específicas.

> A configuração de testes do QAstronaut se refere ao elemento [Tests](https://learning.postman.com/docs/getting-started/first-steps/write-your-first-test/) do postman

> **Obs:** No que diz respeito à quantidade de cenários de teste disponíveis, o QAstronaut está comprometido com a melhoria contínua, expandindo seu repertório de heurísticas de teste e ampliando o escopo dos testes de API. Estamos sempre trabalhando para oferecer uma variedade maior de cenários de teste e aprimorar a cobertura geral de testes, garantindo que o QAstronaut continue sendo uma ferramenta valiosa para testes abrangentes de API.

> **Lembre-se**: Os demais diretórios do projeto como o `functions/` são pastas que estão ligadas com o funcionamento do QAstronaut, qualquer alteração ou exclusão irá afetar diretamente o funcionamento do mesmo. 

#### Personalização dos Títulos dos Cenários de Teste

No QAstronaut, os nomes das [Requisições (Requests)](https://learning.postman.com/docs/sending-requests/requests/) são definidos da seguinte forma:

```text
CT000 - user_requests - Campo JSON - Cenário
```
1. "CT000" representa um contador exclusivo para cada cenário de teste.
2. "user_requests" é o nome do arquivo que deve ser personalizado para identificar a suíte de teste. 
> **Atenção**: Certifique-se de preencher o arquivo `user_requests` pois o QAstronaut depende dele para funcionar corretamente, ele está localizado no diretório `config/requests_names/`
3. O "Campo JSON" refere-se ao campo que está sendo testado no cenário de teste.
4. O "Cenário" descreve o cenário de teste em si, como "Inexistente," "Vazio," "Nulo," e assim por diante.

Para um exemplo prático, um nome de pedido real pode ser definido da seguinte forma:

```text
CT023 - CadastrarUsuário - Nome - Vazio
```

Esta estrutura de nomeação permite uma fácil identificação e rastreamento dos cenários de teste, ajudando a manter seu projeto de testes organizado e eficiente.

## Criação de suítes de teste

Uma vez que o arquivo `curl.txt` foi criado e colocado no diretório `config/requests/`, você estará pronto para executar o QAstronaut. Siga os passos abaixo:

1. Navegue até o diretório `qastronaut/`, que contém o arquivo `qastronaut.py`.
2. Execute o seguinte comando:

    ```bash
    python qastronaut.py
    ```
   
   > **Nota:** Em alguns casos, especialmente no Linux, pode ser necessário usar `python3` em vez de `python` para chamar o interpretador Python 3.

3. Você receberá as seguintes orientações:

    ```bash
    Por favor, coloque o comando cURL em um arquivo de texto chamado 'curl.txt' e pressione 'Enter'.

    Você colocou o comando cURL em 'curl.txt'? (S/n): 
    ```

4. Se você já adicionou o arquivo `curl.txt`, pressione Enter para prosseguir. Caso contrário, adicione o arquivo `curl.txt` e continue.

5. Após esta etapa, você será solicitado a fornecer o nome da coleção que será criada para a suíte de testes e o nome da pasta:

    ```bash
    What will be the name of the collection? Teste
    What will be the name of the folder? Teste

    Collection 'Teste' created successfully with the collection ID: 23485401-2e399297-2c19-41b1-b1ee-a3f209bfee97

    Folder 'Teste' created successfully with the folder ID: 156a5f3f-a018-1943-1373-ba635b2fad44
    ```

6. Após a confirmação do QAstronaut sobre a criação bem-sucedida da coleção e pasta, o próximo passo é informar o método HTTP desejado:

```bash
Which HTTP method do you want to use (GET/POST/PUT/DELETE, etc.)? post
```
7. Feito isso, o QAstronaut irá mostrar a solicitação HTTP correspondente e começará a criar os testes no workspace do Postman, fornecendo um retorno a cada solicitação HTTP criada

```bash
Request Method: POST
Request URL: https://serverest.dev/produtos
Request Body: {'nome': 'Cheese IV', 'preco': 524, 'descricao': 'Produto', 'detalhes': {'peso': '100g', 'fabricante': 'Empresa XYZ'}, 'imagens': ['imagem1.jpg', 'imagem2.jpg']}
Request Headers: Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IkFteTg0QGhvdG1haWwuY29tIiwicGFzc3dvcmQiOiJJTUlVQmpOU1hKSnN2RXMiLCJpYXQiOjE2OTMzNDkwNjcsImV4cCI6MTY5MzM0OTY2N30.B2Rc1H8iR0saTeY9FsX7bo2lDHla_frX0FR6Uz8AjLY
Content-Type: application/json

----------------------------------------------------------------------

<Response [200]>
name has been tested empty
<Response [200]>
price has been tested empty
...
```


## Contribuindo

Agradecemos o seu interesse em contribuir para o projeto **QAstronaut**. Sua contribuição pode ajudar a melhorar o software e beneficiar a comunidade de usuários. Abaixo, explicamos como você pode contribuir:

### Enviando Pull Requests (PRs)

Se você deseja adicionar uma nova funcionalidade, corrigir um erro ou melhorar o código existente, siga estas etapas:

1. Faça um fork do repositório **QAstronaut** para a sua conta do GitHub.

2. Clone o seu fork para o seu ambiente de desenvolvimento local.

```bash
git clone https://github.com/seu-usuario/QAstronaut.git
```

3. Crie um branch para a sua contribuição. Certifique-se de nomear o branch de forma descritiva.

```bash
git checkout -b minha-contribuicao
```

4. Faça as alterações desejadas no código.

5. Certifique-se de que as alterações sejam acompanhadas por testes apropriados.

6. Realize um commit das suas alterações.

```bash
git commit -m "Adiciona funcionalidade X"
```

7. Envie o branch com as alterações para o seu fork no GitHub.

```bash
git push origin minha-contribuicao
```

8. Acesse o seu fork no GitHub e clique em "New Pull Request" para enviar a sua contribuição. Certifique-se de fornecer uma descrição clara das alterações.

### Relatando Problemas

Se você encontrar problemas ou bugs no software, agradecemos por relatar esses problemas. Para relatar um problema, siga estas etapas:

1. Acesse a seção "Issues" deste repositório.

2. Clique em "New Issue" e descreva o problema de forma detalhada. Inclua informações relevantes, como o ambiente em que você encontrou o problema e etapas para reproduzi-lo.

3. Aguarde a equipe do projeto analisar e responder ao seu relatório.

### Sugerindo Melhorias

Se você tiver sugestões para melhorar o software, adoraríamos ouvir suas ideias. Siga estas etapas para sugerir melhorias:

1. Acesse a seção "Issues" deste repositório.

2. Clique em "New Issue" e selecione a opção "Feature Request" ou "Enhancement". Descreva a melhoria que você gostaria de ver no software.

3. Aguarde a equipe do projeto considerar a sua sugestão.

Agradecemos a todos os contribuidores pelo seu tempo e esforço dedicados a tornar o projeto **QAstronaut** melhor. Juntos, podemos criar um software mais robusto e eficaz.

## Agradecimentos

Gostaríamos de expressar nossa profunda gratidão às seguintes pessoas que desempenharam papéis fundamentais no sucesso deste projeto:

- Professor Dr. Fabio Vieira: Queremos estender nosso agradecimento ao Professor Dr. Fabio por orientar e supervisionar nosso projeto. Sua orientação acadêmica e apoio foram essenciais para o seu sucesso.

- [Paula Santiago](https://www.linkedin.com/in/paulasanty): Agradecemos a Paula Santiago por compartilhar seu conhecimento prático em garantia de qualidade (QA) e sua experiência com a ferramenta Postman. Suas contribuições foram cruciais para a qualidade do nosso projeto.

- [Samara Suelen Garofalo](https://github.com/samaragarofalo): Agradecemos a Samara por sua orientação valiosa e mentoria durante todo o processo de desenvolvimento. Sua experiência e insights foram inestimáveis.

- Enzo Marinho: Agradecemos a Enzo por sua criatividade e por ajudar no desenvolvimento da logo do projeto. Sua contribuição adicionou um toque especial ao nosso trabalho.

Estamos profundamente gratos a essas pessoas por suas contribuições valiosas. Seu apoio e dedicação foram essenciais para o nosso projeto. Obrigado por fazer parte desta jornada conosco.


## Licença

Este software é licenciado sob a [Licença MIT](https://github.com/QAstronaut/qastronaut/blob/main/LICENSE)