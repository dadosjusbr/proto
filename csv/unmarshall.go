package csv

import (
	"fmt"
)

func (c *ContraCheque_CSV) MarshalCSV() (string, error) {
	headers := fmt.Sprintln("id_contra_cheque,chave_coleta,nome,matricula,funcao,local_trabalho,tipo,ativo")
	row := fmt.Sprintf("%s,%s,%s,%s,%s,%s,%s,%t",
		c.IdContraCheque,
		c.ChaveColeta,
		c.Nome,
		c.Matricula,
		c.Funcao,
		c.LocalTrabalho,
		c.Tipo,
		c.Ativo)
	return fmt.Sprintf("%s%s", headers, row), nil
}

func (c *Coleta_CSV) MarshalCSV() (string, error) {
	headers := fmt.Sprintln("chave_coleta,orgao,mes,ano,timestamp_coleta,repositorio_coletor,versao_coletor,dir_coletor")
	row := fmt.Sprintf("%s,%s,%d,%d,%v,%s,%s,%s", c.ChaveColeta, c.Orgao, c.Mes, c.Ano, c.TimestampColeta.Seconds, c.RepositorioColetor, c.VersaoColetor, c.DirColetor)
	return fmt.Sprintf("%s%s", headers, row), nil
}

func (c *Metadados_CSV) MarshalCSV() (string, error) {
	headers := fmt.Sprintln("chave_coleta,nao_requer_login,nao_requer_captcha,acesso,extensao,estritamente_tabular,formato_consistente,tem_matricula,tem_lotacao,tem_cargo,detalhamento_receita_base,detalhamento_outras_receitas,detalhamento_descontos")
	row := fmt.Sprintf("%s,%t,%t,%s,%s,%t,%t,%t,%t,%t,%s,%s,%s",
		c.ChaveColeta,
		c.NaoRequerLogin,
		c.NaoRequerCaptcha,
		c.Acesso.String(),
		c.Extensao.String(),
		c.EstritamenteTabular,
		c.FormatoConsistente,
		c.TemMatricula,
		c.TemLotacao,
		c.TemCargo,
		c.DetalhamentoReceitaBase.String(),
		c.DetalhamentoOutrasReceitas.String(),
		c.DetalhamentoDescontos.String())
	return fmt.Sprintf("%s%s", headers, row), nil
}

func (r *Remuneracao_CSV) MarshalCSV() (string, error) {
	headers := fmt.Sprintln("id_contra_cheque,chave_coleta,natureza,categoria,item,valor")
	row := fmt.Sprintf("%s,%s,%s,%s,%s,%f",
		r.IdContraCheque,
		r.ChaveColeta,
		r.Natureza.String(),
		r.Categoria,
		r.Item,
		r.Valor)
	return fmt.Sprintf("%s%s", headers, row), nil
}
