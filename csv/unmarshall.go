package csv

import (
	"fmt"
)

func (c *Coleta_CSV) MarshalCSV() (string, error) {
	headers := fmt.Sprintln("chave_coleta,orgao,mes,ano,timestamp_coleta,repositorio_coletor,versao_coletor,dir_coletor")
	row := fmt.Sprintf("%s,%s,%d,%d,%v,%s,%s,%s", c.ChaveColeta, c.Orgao, c.Mes, c.Ano, c.TimestampColeta.Seconds, c.RepositorioColetor, c.VersaoColetor, c.DirColetor)
	return fmt.Sprintf("%s\n%s", headers, row), nil
}
