package proto

import "fmt"

// IDColeta gera um nova chave para coleta.
func IDColeta(orgao, mes, ano string) string {
	return fmt.Sprintf("%s/%s/%s", orgao, mes, ano)
}
