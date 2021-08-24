package csv

import (
	"fmt"
)

func (c *Coleta_CSV) MarshalCSV() (string, error) {
	return fmt.Sprintf("%s,%s,%d,%d,%v,%s,%s,%s", c.ChaveColeta, c.Orgao, c.Mes, c.Ano, c.TimestampColeta.Seconds, c.RepositorioColetor, c.VersaoColetor, c.DirColetor), nil
}
