# MVP DESENVOLVIMENTO FULL-STACK BÁSICO - BACK END

API para o MVP de trabalho final da disciplina Desenvolvimento Full Stack Básico.

# COMO RODAR ESTE PROJETO

Para facilitar rodar este projeto, foi incluído um Dockerfile. Após clonar o projeto, primeiramente, é necessário fazer o build da imagem:

```bash
docker build -t library-mvp .
```

Onde `library-mvp` será o nome da nossa imagem. Logo após, rodar o seguinte comando:

```bash
docker run -d -p 3000:5000 rest-apis-flask-python
```

Onde a porta de número `3000` do nosso sistema será mapeada para a porta `5000` do container, que por sua vez é a porta padrão do Flask, para onde as requisições precisam ser feitas.

Desse modo, pode-se testar o funcionamento da API da seguinte maneira:

```bash
curl http://localhost:3000/ping
```

Se o servidor responder com `pong`, quer dizer que a API está rodando corretamente.
