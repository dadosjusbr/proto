package proto

import "fmt"

// IDColeta gera um nova chave para coleta.
func IDColeta(orgao string, mes, ano int) string {
	return fmt.Sprintf("%s/%v/%v", orgao, mes, ano)
}
