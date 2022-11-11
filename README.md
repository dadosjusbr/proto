# Proto

- Esquema de dados em Protobuf.

# Instalando o proto

```sh
    $ apt install -y protobuf-compiler
```

# Gerar código go e python

## Gerando novos protos

### GO

```sh
    $ go install google.golang.org/protobuf/cmd/protoc-gen-go
```

// Gerar stub na raiz.

```sh
    $ cd coleta
    $ protoc --go_out=./ --go_opt=paths=source_relative coleta.proto
```

```sh
    $ cd ..
    $ protoc --go_out=pipeline/ --go_opt=paths=source_relative --proto_path=coleta --proto_path=pipeline pipeline/pipeline.proto
```

### Python

// Gerar stub na raiz.

```sh
    $ cd coleta
    $ protoc --python_out=./ coleta.proto
```

```sh
    $ cd ..
    $ protoc --python_out=pipeline/ --proto_path=coleta --proto_path=pipeline pipeline/pipeline.proto
```

## Casos de erro ao tentar gerar proto

Caso o seguinte erro tenha ocorrido, significa que a instalação da lib do protobuf não funcionou:

```
"protoc-gen-go: program not found or is not executable--go_out: protoc-gen-go: Plugin failed with status code 1."
```

Para consertar, você deve executar os seguintes comandos:

```
    $ export GOPATH=$HOME/go
    $ export PATH=$PATH:$GOPATH/bin
    $ go install google.golang.org/protobuf/cmd/protoc-gen-go
```

Após isso, você conseguirá gerar o proto.

## Atulizando a lib no pipy

```sh
    $ python3 setup.py sdist
    $ python3 -m twine upload --skip-existing dist/*
```
