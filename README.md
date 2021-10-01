# Proto
- Esquema de dados em Protobuf.

# Gerar código go e python

## Gerando novos protos

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

## Atulizando a lib no pipy

```sh
    $ python setup.py sdist
    $ python -m twine upload --skip-existing dist/*
```