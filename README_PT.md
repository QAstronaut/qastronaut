# QAstronaut

Bem-vindo ao **QAstronaut, Sua Solução para Testes de API com Agilidade!**

![GitHub Logo](/images/logo_qastronaut.png)

O QAstronaut é um projeto em desenvolvimento que visa automatizar a execução e criação de suítes de testes. Este repositório serve como um espaço central para o desenvolvimento, documentação e colaboração.

## Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Instalação](#instalação)
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

Siga estas instruções para baixar e configurar o QAstronaut em seu ambiente.

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
    > **Alerta:** em alguns casos, pode ser necessário usar `python3` ou `py` em vez de `python` para chamar o interpretador Python 3.

    Este comando irá solicitar a sua Postman [API Key](https://learning.postman.com/docs/developer/postman-api/authentication/) e criará as pastas de configuração do QAstronaut.

    Após esse processo, o QAstronaut está pronto para uso.

    Para mais informações sobre o QAstronaut, incluindo suas funcionalidades, configurações e `primeiros passos`, recomendamos consultar nossa [Wiki](https://github.com/QAstronaut/qastronaut/wiki).

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
