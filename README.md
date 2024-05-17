# Inteli Prova 1 - Módulo 10

## Funcionamento

### Swagger

https://github.com/Lemos1347/inteli-modulo-10-prova-1/assets/99190347/f051171f-daf7-464d-9140-f6a2873e8efc

### Insomnia

## Como rodar

Para rodar essa aplicação basta rodas os seguinte comandos:

1. Clone o repositório:

```bash
git clone https://github.com/Lemos1347/inteli-modulo-10-prova-1.git prova-1-m10
```

2. Entre na pasta do projeto:

```bash
cd prova-1-m10
```

3. Suba os conteineres:

```bash
docker-compose up --build
```

Pronto! Agora você tera a aplicação rodando em sua máquina:

- Backend: http://localhost:3001
  - Backend docs: [http://localhost:3001/docs](http://localhost:3001/docs)
- Banco de dados: http://localhost:5432

Você pode encontrar uma coleção do inmsominia em [static/insomnia.json](./static/Insomnia_2024-05-17.json)

## Estrutura do repositório

Nesse repositório você encontrará duas pastas:

- /backend: contento todo o código do backend
  - Dentro de backend além do código fonte em python, é possível encontrar o seu Dockerfile
- /database: contento todas as tabelas que devem ser criadas no repositorio
- /statis: arquivos estáticos (e.g.: [collections do insomnia](./static/Insomnia_2024-05-17.json))
