# proto
Esquema de dados em Protobuf.

# Gerar código go e python

go install google.golang.org/protobuf/cmd/protoc-gen-go

// Gerar stub na raiz.
protoc --go_out=./ --go_opt=paths=source_relative coleta.proto