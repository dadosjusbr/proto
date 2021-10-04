# Proto
- Esquema de dados em Protobuf.

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
    $ cd ../csv
    $ protoc --go_out=./ pacote.proto
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
    $ cd ../csv
    $ protoc --python_out=./ pacote.proto
```

```sh
    $ cd ..
    $ protoc --python_out=pipeline/ --proto_path=coleta --proto_path=pipeline pipeline/pipeline.proto
```
## Atulizando a lib no pipy

```sh
    $ python setup.py sdist
    $ python -m twine upload --skip-existing dist/*
```