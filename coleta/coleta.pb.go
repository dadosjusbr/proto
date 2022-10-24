// Code generated by protoc-gen-go. DO NOT EDIT.
// source: coleta.proto

package coleta

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	timestamp "github.com/golang/protobuf/ptypes/timestamp"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type ContraCheque_Tipo int32

const (
	ContraCheque_MEMBRO   ContraCheque_Tipo = 0
	ContraCheque_SERVIDOR ContraCheque_Tipo = 1
)

var ContraCheque_Tipo_name = map[int32]string{
	0: "MEMBRO",
	1: "SERVIDOR",
}

var ContraCheque_Tipo_value = map[string]int32{
	"MEMBRO":   0,
	"SERVIDOR": 1,
}

func (x ContraCheque_Tipo) String() string {
	return proto.EnumName(ContraCheque_Tipo_name, int32(x))
}

func (ContraCheque_Tipo) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{4, 0}
}

type Remuneracao_Natureza int32

const (
	Remuneracao_R Remuneracao_Natureza = 0
	Remuneracao_D Remuneracao_Natureza = 1
)

var Remuneracao_Natureza_name = map[int32]string{
	0: "R",
	1: "D",
}

var Remuneracao_Natureza_value = map[string]int32{
	"R": 0,
	"D": 1,
}

func (x Remuneracao_Natureza) String() string {
	return proto.EnumName(Remuneracao_Natureza_name, int32(x))
}

func (Remuneracao_Natureza) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{6, 0}
}

type Remuneracao_TipoReceita int32

const (
	Remuneracao_B Remuneracao_TipoReceita = 0
	Remuneracao_O Remuneracao_TipoReceita = 1
)

var Remuneracao_TipoReceita_name = map[int32]string{
	0: "B",
	1: "O",
}

var Remuneracao_TipoReceita_value = map[string]int32{
	"B": 0,
	"O": 1,
}

func (x Remuneracao_TipoReceita) String() string {
	return proto.EnumName(Remuneracao_TipoReceita_name, int32(x))
}

func (Remuneracao_TipoReceita) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{6, 1}
}

type Metadados_FormaDeAcesso int32

const (
	Metadados_ACESSO_DIRETO               Metadados_FormaDeAcesso = 0
	Metadados_NECESSITA_RASPAGEM          Metadados_FormaDeAcesso = 1
	Metadados_NECESSITA_SIMULACAO_USUARIO Metadados_FormaDeAcesso = 2
)

var Metadados_FormaDeAcesso_name = map[int32]string{
	0: "ACESSO_DIRETO",
	1: "NECESSITA_RASPAGEM",
	2: "NECESSITA_SIMULACAO_USUARIO",
}

var Metadados_FormaDeAcesso_value = map[string]int32{
	"ACESSO_DIRETO":               0,
	"NECESSITA_RASPAGEM":          1,
	"NECESSITA_SIMULACAO_USUARIO": 2,
}

func (x Metadados_FormaDeAcesso) String() string {
	return proto.EnumName(Metadados_FormaDeAcesso_name, int32(x))
}

func (Metadados_FormaDeAcesso) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{7, 0}
}

type Metadados_Extensao int32

const (
	Metadados_PDF  Metadados_Extensao = 0
	Metadados_ODS  Metadados_Extensao = 1
	Metadados_XLS  Metadados_Extensao = 2
	Metadados_JSON Metadados_Extensao = 3
	Metadados_CSV  Metadados_Extensao = 4
	Metadados_HTML Metadados_Extensao = 5
	Metadados_ODT  Metadados_Extensao = 6
)

var Metadados_Extensao_name = map[int32]string{
	0: "PDF",
	1: "ODS",
	2: "XLS",
	3: "JSON",
	4: "CSV",
	5: "HTML",
	6: "ODT",
}

var Metadados_Extensao_value = map[string]int32{
	"PDF":  0,
	"ODS":  1,
	"XLS":  2,
	"JSON": 3,
	"CSV":  4,
	"HTML": 5,
	"ODT":  6,
}

func (x Metadados_Extensao) String() string {
	return proto.EnumName(Metadados_Extensao_name, int32(x))
}

func (Metadados_Extensao) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{7, 1}
}

type Metadados_OpcoesDetalhamento int32

const (
	Metadados_AUSENCIA   Metadados_OpcoesDetalhamento = 0
	Metadados_SUMARIZADO Metadados_OpcoesDetalhamento = 1
	Metadados_DETALHADO  Metadados_OpcoesDetalhamento = 2
)

var Metadados_OpcoesDetalhamento_name = map[int32]string{
	0: "AUSENCIA",
	1: "SUMARIZADO",
	2: "DETALHADO",
}

var Metadados_OpcoesDetalhamento_value = map[string]int32{
	"AUSENCIA":   0,
	"SUMARIZADO": 1,
	"DETALHADO":  2,
}

func (x Metadados_OpcoesDetalhamento) String() string {
	return proto.EnumName(Metadados_OpcoesDetalhamento_name, int32(x))
}

func (Metadados_OpcoesDetalhamento) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{7, 2}
}

// Estrutura com informações pertencentes a execução da coleta dos dados.
type ResultadoColeta struct {
	Coleta               *Coleta           `protobuf:"bytes,1,opt,name=coleta,proto3" json:"coleta,omitempty"`
	Folha                *FolhaDePagamento `protobuf:"bytes,2,opt,name=folha,proto3" json:"folha,omitempty"`
	Procinfo             *ProcInfo         `protobuf:"bytes,3,opt,name=procinfo,proto3" json:"procinfo,omitempty"`
	Metadados            *Metadados        `protobuf:"bytes,4,opt,name=metadados,proto3" json:"metadados,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *ResultadoColeta) Reset()         { *m = ResultadoColeta{} }
func (m *ResultadoColeta) String() string { return proto.CompactTextString(m) }
func (*ResultadoColeta) ProtoMessage()    {}
func (*ResultadoColeta) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{0}
}

func (m *ResultadoColeta) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ResultadoColeta.Unmarshal(m, b)
}
func (m *ResultadoColeta) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ResultadoColeta.Marshal(b, m, deterministic)
}
func (m *ResultadoColeta) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ResultadoColeta.Merge(m, src)
}
func (m *ResultadoColeta) XXX_Size() int {
	return xxx_messageInfo_ResultadoColeta.Size(m)
}
func (m *ResultadoColeta) XXX_DiscardUnknown() {
	xxx_messageInfo_ResultadoColeta.DiscardUnknown(m)
}

var xxx_messageInfo_ResultadoColeta proto.InternalMessageInfo

func (m *ResultadoColeta) GetColeta() *Coleta {
	if m != nil {
		return m.Coleta
	}
	return nil
}

func (m *ResultadoColeta) GetFolha() *FolhaDePagamento {
	if m != nil {
		return m.Folha
	}
	return nil
}

func (m *ResultadoColeta) GetProcinfo() *ProcInfo {
	if m != nil {
		return m.Procinfo
	}
	return nil
}

func (m *ResultadoColeta) GetMetadados() *Metadados {
	if m != nil {
		return m.Metadados
	}
	return nil
}

type ProcInfo struct {
	Stdin                string   `protobuf:"bytes,1,opt,name=stdin,proto3" json:"stdin,omitempty"`
	Stdout               string   `protobuf:"bytes,2,opt,name=stdout,proto3" json:"stdout,omitempty"`
	Stderr               string   `protobuf:"bytes,3,opt,name=stderr,proto3" json:"stderr,omitempty"`
	Cmd                  string   `protobuf:"bytes,4,opt,name=cmd,proto3" json:"cmd,omitempty"`
	CmdDir               string   `protobuf:"bytes,5,opt,name=cmdDir,proto3" json:"cmdDir,omitempty"`
	Status               int32    `protobuf:"varint,6,opt,name=status,proto3" json:"status,omitempty"`
	Env                  []string `protobuf:"bytes,7,rep,name=env,proto3" json:"env,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *ProcInfo) Reset()         { *m = ProcInfo{} }
func (m *ProcInfo) String() string { return proto.CompactTextString(m) }
func (*ProcInfo) ProtoMessage()    {}
func (*ProcInfo) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{1}
}

func (m *ProcInfo) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ProcInfo.Unmarshal(m, b)
}
func (m *ProcInfo) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ProcInfo.Marshal(b, m, deterministic)
}
func (m *ProcInfo) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ProcInfo.Merge(m, src)
}
func (m *ProcInfo) XXX_Size() int {
	return xxx_messageInfo_ProcInfo.Size(m)
}
func (m *ProcInfo) XXX_DiscardUnknown() {
	xxx_messageInfo_ProcInfo.DiscardUnknown(m)
}

var xxx_messageInfo_ProcInfo proto.InternalMessageInfo

func (m *ProcInfo) GetStdin() string {
	if m != nil {
		return m.Stdin
	}
	return ""
}

func (m *ProcInfo) GetStdout() string {
	if m != nil {
		return m.Stdout
	}
	return ""
}

func (m *ProcInfo) GetStderr() string {
	if m != nil {
		return m.Stderr
	}
	return ""
}

func (m *ProcInfo) GetCmd() string {
	if m != nil {
		return m.Cmd
	}
	return ""
}

func (m *ProcInfo) GetCmdDir() string {
	if m != nil {
		return m.CmdDir
	}
	return ""
}

func (m *ProcInfo) GetStatus() int32 {
	if m != nil {
		return m.Status
	}
	return 0
}

func (m *ProcInfo) GetEnv() []string {
	if m != nil {
		return m.Env
	}
	return nil
}

// Estrutura com informações pertencentes a coleta dos dados referentes a um órgão-mes-ano
type Coleta struct {
	ChaveColeta          string               `protobuf:"bytes,1,opt,name=chave_coleta,json=chaveColeta,proto3" json:"chave_coleta,omitempty"`
	Orgao                string               `protobuf:"bytes,2,opt,name=orgao,proto3" json:"orgao,omitempty"`
	Mes                  int32                `protobuf:"varint,3,opt,name=mes,proto3" json:"mes,omitempty"`
	Ano                  int32                `protobuf:"varint,4,opt,name=ano,proto3" json:"ano,omitempty"`
	TimestampColeta      *timestamp.Timestamp `protobuf:"bytes,5,opt,name=timestamp_coleta,json=timestampColeta,proto3" json:"timestamp_coleta,omitempty"`
	RepositorioColetor   string               `protobuf:"bytes,6,opt,name=repositorio_coletor,json=repositorioColetor,proto3" json:"repositorio_coletor,omitempty"`
	VersaoColetor        string               `protobuf:"bytes,7,opt,name=versao_coletor,json=versaoColetor,proto3" json:"versao_coletor,omitempty"`
	DirColetor           string               `protobuf:"bytes,8,opt,name=dir_coletor,json=dirColetor,proto3" json:"dir_coletor,omitempty"`
	Arquivos             []string             `protobuf:"bytes,9,rep,name=arquivos,proto3" json:"arquivos,omitempty"`
	XXX_NoUnkeyedLiteral struct{}             `json:"-"`
	XXX_unrecognized     []byte               `json:"-"`
	XXX_sizecache        int32                `json:"-"`
}

func (m *Coleta) Reset()         { *m = Coleta{} }
func (m *Coleta) String() string { return proto.CompactTextString(m) }
func (*Coleta) ProtoMessage()    {}
func (*Coleta) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{2}
}

func (m *Coleta) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Coleta.Unmarshal(m, b)
}
func (m *Coleta) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Coleta.Marshal(b, m, deterministic)
}
func (m *Coleta) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Coleta.Merge(m, src)
}
func (m *Coleta) XXX_Size() int {
	return xxx_messageInfo_Coleta.Size(m)
}
func (m *Coleta) XXX_DiscardUnknown() {
	xxx_messageInfo_Coleta.DiscardUnknown(m)
}

var xxx_messageInfo_Coleta proto.InternalMessageInfo

func (m *Coleta) GetChaveColeta() string {
	if m != nil {
		return m.ChaveColeta
	}
	return ""
}

func (m *Coleta) GetOrgao() string {
	if m != nil {
		return m.Orgao
	}
	return ""
}

func (m *Coleta) GetMes() int32 {
	if m != nil {
		return m.Mes
	}
	return 0
}

func (m *Coleta) GetAno() int32 {
	if m != nil {
		return m.Ano
	}
	return 0
}

func (m *Coleta) GetTimestampColeta() *timestamp.Timestamp {
	if m != nil {
		return m.TimestampColeta
	}
	return nil
}

func (m *Coleta) GetRepositorioColetor() string {
	if m != nil {
		return m.RepositorioColetor
	}
	return ""
}

func (m *Coleta) GetVersaoColetor() string {
	if m != nil {
		return m.VersaoColetor
	}
	return ""
}

func (m *Coleta) GetDirColetor() string {
	if m != nil {
		return m.DirColetor
	}
	return ""
}

func (m *Coleta) GetArquivos() []string {
	if m != nil {
		return m.Arquivos
	}
	return nil
}

// Estrutura que faz referência a uma lista de contra-cheques
type FolhaDePagamento struct {
	ContraCheque         []*ContraCheque `protobuf:"bytes,1,rep,name=contra_cheque,json=contraCheque,proto3" json:"contra_cheque,omitempty"`
	XXX_NoUnkeyedLiteral struct{}        `json:"-"`
	XXX_unrecognized     []byte          `json:"-"`
	XXX_sizecache        int32           `json:"-"`
}

func (m *FolhaDePagamento) Reset()         { *m = FolhaDePagamento{} }
func (m *FolhaDePagamento) String() string { return proto.CompactTextString(m) }
func (*FolhaDePagamento) ProtoMessage()    {}
func (*FolhaDePagamento) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{3}
}

func (m *FolhaDePagamento) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_FolhaDePagamento.Unmarshal(m, b)
}
func (m *FolhaDePagamento) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_FolhaDePagamento.Marshal(b, m, deterministic)
}
func (m *FolhaDePagamento) XXX_Merge(src proto.Message) {
	xxx_messageInfo_FolhaDePagamento.Merge(m, src)
}
func (m *FolhaDePagamento) XXX_Size() int {
	return xxx_messageInfo_FolhaDePagamento.Size(m)
}
func (m *FolhaDePagamento) XXX_DiscardUnknown() {
	xxx_messageInfo_FolhaDePagamento.DiscardUnknown(m)
}

var xxx_messageInfo_FolhaDePagamento proto.InternalMessageInfo

func (m *FolhaDePagamento) GetContraCheque() []*ContraCheque {
	if m != nil {
		return m.ContraCheque
	}
	return nil
}

// Estrutura que faz referência a uma linha de contra-cheque em um órgão-mes-ano
type ContraCheque struct {
	IdContraCheque       string            `protobuf:"bytes,1,opt,name=id_contra_cheque,json=idContraCheque,proto3" json:"id_contra_cheque,omitempty"`
	ChaveColeta          string            `protobuf:"bytes,2,opt,name=chave_coleta,json=chaveColeta,proto3" json:"chave_coleta,omitempty"`
	Nome                 string            `protobuf:"bytes,3,opt,name=nome,proto3" json:"nome,omitempty"`
	Matricula            string            `protobuf:"bytes,4,opt,name=matricula,proto3" json:"matricula,omitempty"`
	Funcao               string            `protobuf:"bytes,5,opt,name=funcao,proto3" json:"funcao,omitempty"`
	LocalTrabalho        string            `protobuf:"bytes,6,opt,name=local_trabalho,json=localTrabalho,proto3" json:"local_trabalho,omitempty"`
	Tipo                 ContraCheque_Tipo `protobuf:"varint,7,opt,name=tipo,proto3,enum=ContraCheque_Tipo" json:"tipo,omitempty"`
	Ativo                bool              `protobuf:"varint,8,opt,name=ativo,proto3" json:"ativo,omitempty"`
	Remuneracoes         *Remuneracoes     `protobuf:"bytes,9,opt,name=remuneracoes,proto3" json:"remuneracoes,omitempty"`
	XXX_NoUnkeyedLiteral struct{}          `json:"-"`
	XXX_unrecognized     []byte            `json:"-"`
	XXX_sizecache        int32             `json:"-"`
}

func (m *ContraCheque) Reset()         { *m = ContraCheque{} }
func (m *ContraCheque) String() string { return proto.CompactTextString(m) }
func (*ContraCheque) ProtoMessage()    {}
func (*ContraCheque) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{4}
}

func (m *ContraCheque) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ContraCheque.Unmarshal(m, b)
}
func (m *ContraCheque) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ContraCheque.Marshal(b, m, deterministic)
}
func (m *ContraCheque) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ContraCheque.Merge(m, src)
}
func (m *ContraCheque) XXX_Size() int {
	return xxx_messageInfo_ContraCheque.Size(m)
}
func (m *ContraCheque) XXX_DiscardUnknown() {
	xxx_messageInfo_ContraCheque.DiscardUnknown(m)
}

var xxx_messageInfo_ContraCheque proto.InternalMessageInfo

func (m *ContraCheque) GetIdContraCheque() string {
	if m != nil {
		return m.IdContraCheque
	}
	return ""
}

func (m *ContraCheque) GetChaveColeta() string {
	if m != nil {
		return m.ChaveColeta
	}
	return ""
}

func (m *ContraCheque) GetNome() string {
	if m != nil {
		return m.Nome
	}
	return ""
}

func (m *ContraCheque) GetMatricula() string {
	if m != nil {
		return m.Matricula
	}
	return ""
}

func (m *ContraCheque) GetFuncao() string {
	if m != nil {
		return m.Funcao
	}
	return ""
}

func (m *ContraCheque) GetLocalTrabalho() string {
	if m != nil {
		return m.LocalTrabalho
	}
	return ""
}

func (m *ContraCheque) GetTipo() ContraCheque_Tipo {
	if m != nil {
		return m.Tipo
	}
	return ContraCheque_MEMBRO
}

func (m *ContraCheque) GetAtivo() bool {
	if m != nil {
		return m.Ativo
	}
	return false
}

func (m *ContraCheque) GetRemuneracoes() *Remuneracoes {
	if m != nil {
		return m.Remuneracoes
	}
	return nil
}

// Estrutura que faz referência a uma lista de Remunerações
type Remuneracoes struct {
	Remuneracao          []*Remuneracao `protobuf:"bytes,1,rep,name=remuneracao,proto3" json:"remuneracao,omitempty"`
	XXX_NoUnkeyedLiteral struct{}       `json:"-"`
	XXX_unrecognized     []byte         `json:"-"`
	XXX_sizecache        int32          `json:"-"`
}

func (m *Remuneracoes) Reset()         { *m = Remuneracoes{} }
func (m *Remuneracoes) String() string { return proto.CompactTextString(m) }
func (*Remuneracoes) ProtoMessage()    {}
func (*Remuneracoes) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{5}
}

func (m *Remuneracoes) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Remuneracoes.Unmarshal(m, b)
}
func (m *Remuneracoes) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Remuneracoes.Marshal(b, m, deterministic)
}
func (m *Remuneracoes) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Remuneracoes.Merge(m, src)
}
func (m *Remuneracoes) XXX_Size() int {
	return xxx_messageInfo_Remuneracoes.Size(m)
}
func (m *Remuneracoes) XXX_DiscardUnknown() {
	xxx_messageInfo_Remuneracoes.DiscardUnknown(m)
}

var xxx_messageInfo_Remuneracoes proto.InternalMessageInfo

func (m *Remuneracoes) GetRemuneracao() []*Remuneracao {
	if m != nil {
		return m.Remuneracao
	}
	return nil
}

// Estrutura que faz referência a uma linha de remuneração em um órgão-mes-ano
type Remuneracao struct {
	Natureza             Remuneracao_Natureza    `protobuf:"varint,1,opt,name=natureza,proto3,enum=Remuneracao_Natureza" json:"natureza,omitempty"`
	Categoria            string                  `protobuf:"bytes,2,opt,name=categoria,proto3" json:"categoria,omitempty"`
	Item                 string                  `protobuf:"bytes,3,opt,name=item,proto3" json:"item,omitempty"`
	Valor                float64                 `protobuf:"fixed64,4,opt,name=valor,proto3" json:"valor,omitempty"`
	TipoReceita          Remuneracao_TipoReceita `protobuf:"varint,5,opt,name=tipo_receita,json=tipoReceita,proto3,enum=Remuneracao_TipoReceita" json:"tipo_receita,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                `json:"-"`
	XXX_unrecognized     []byte                  `json:"-"`
	XXX_sizecache        int32                   `json:"-"`
}

func (m *Remuneracao) Reset()         { *m = Remuneracao{} }
func (m *Remuneracao) String() string { return proto.CompactTextString(m) }
func (*Remuneracao) ProtoMessage()    {}
func (*Remuneracao) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{6}
}

func (m *Remuneracao) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Remuneracao.Unmarshal(m, b)
}
func (m *Remuneracao) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Remuneracao.Marshal(b, m, deterministic)
}
func (m *Remuneracao) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Remuneracao.Merge(m, src)
}
func (m *Remuneracao) XXX_Size() int {
	return xxx_messageInfo_Remuneracao.Size(m)
}
func (m *Remuneracao) XXX_DiscardUnknown() {
	xxx_messageInfo_Remuneracao.DiscardUnknown(m)
}

var xxx_messageInfo_Remuneracao proto.InternalMessageInfo

func (m *Remuneracao) GetNatureza() Remuneracao_Natureza {
	if m != nil {
		return m.Natureza
	}
	return Remuneracao_R
}

func (m *Remuneracao) GetCategoria() string {
	if m != nil {
		return m.Categoria
	}
	return ""
}

func (m *Remuneracao) GetItem() string {
	if m != nil {
		return m.Item
	}
	return ""
}

func (m *Remuneracao) GetValor() float64 {
	if m != nil {
		return m.Valor
	}
	return 0
}

func (m *Remuneracao) GetTipoReceita() Remuneracao_TipoReceita {
	if m != nil {
		return m.TipoReceita
	}
	return Remuneracao_B
}

// Estrutura que faz referência aos metadadoss utilizados para construção do índice de transparência
type Metadados struct {
	Acesso               Metadados_FormaDeAcesso      `protobuf:"varint,3,opt,name=acesso,proto3,enum=Metadados_FormaDeAcesso" json:"acesso,omitempty"`
	Extensao             Metadados_Extensao           `protobuf:"varint,4,opt,name=extensao,proto3,enum=Metadados_Extensao" json:"extensao,omitempty"`
	EstritamenteTabular  bool                         `protobuf:"varint,5,opt,name=estritamente_tabular,json=estritamenteTabular,proto3" json:"estritamente_tabular,omitempty"`
	FormatoConsistente   bool                         `protobuf:"varint,6,opt,name=formato_consistente,json=formatoConsistente,proto3" json:"formato_consistente,omitempty"`
	TemMatricula         bool                         `protobuf:"varint,7,opt,name=tem_matricula,json=temMatricula,proto3" json:"tem_matricula,omitempty"`
	TemLotacao           bool                         `protobuf:"varint,8,opt,name=tem_lotacao,json=temLotacao,proto3" json:"tem_lotacao,omitempty"`
	TemCargo             bool                         `protobuf:"varint,9,opt,name=tem_cargo,json=temCargo,proto3" json:"tem_cargo,omitempty"`
	FormatoAberto        bool                         `protobuf:"varint,10,opt,name=formato_aberto,json=formatoAberto,proto3" json:"formato_aberto,omitempty"`
	ReceitaBase          Metadados_OpcoesDetalhamento `protobuf:"varint,11,opt,name=receita_base,json=receitaBase,proto3,enum=Metadados_OpcoesDetalhamento" json:"receita_base,omitempty"`
	OutrasReceitas       Metadados_OpcoesDetalhamento `protobuf:"varint,12,opt,name=outras_receitas,json=outrasReceitas,proto3,enum=Metadados_OpcoesDetalhamento" json:"outras_receitas,omitempty"`
	Despesas             Metadados_OpcoesDetalhamento `protobuf:"varint,13,opt,name=despesas,proto3,enum=Metadados_OpcoesDetalhamento" json:"despesas,omitempty"`
	IndiceCompletude     float32                      `protobuf:"fixed32,14,opt,name=indice_completude,json=indiceCompletude,proto3" json:"indice_completude,omitempty"`
	IndiceFacilidade     float32                      `protobuf:"fixed32,15,opt,name=indice_facilidade,json=indiceFacilidade,proto3" json:"indice_facilidade,omitempty"`
	IndiceTransparencia  float32                      `protobuf:"fixed32,16,opt,name=indice_transparencia,json=indiceTransparencia,proto3" json:"indice_transparencia,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                     `json:"-"`
	XXX_unrecognized     []byte                       `json:"-"`
	XXX_sizecache        int32                        `json:"-"`
}

func (m *Metadados) Reset()         { *m = Metadados{} }
func (m *Metadados) String() string { return proto.CompactTextString(m) }
func (*Metadados) ProtoMessage()    {}
func (*Metadados) Descriptor() ([]byte, []int) {
	return fileDescriptor_6d118783d7815953, []int{7}
}

func (m *Metadados) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Metadados.Unmarshal(m, b)
}
func (m *Metadados) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Metadados.Marshal(b, m, deterministic)
}
func (m *Metadados) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Metadados.Merge(m, src)
}
func (m *Metadados) XXX_Size() int {
	return xxx_messageInfo_Metadados.Size(m)
}
func (m *Metadados) XXX_DiscardUnknown() {
	xxx_messageInfo_Metadados.DiscardUnknown(m)
}

var xxx_messageInfo_Metadados proto.InternalMessageInfo

func (m *Metadados) GetAcesso() Metadados_FormaDeAcesso {
	if m != nil {
		return m.Acesso
	}
	return Metadados_ACESSO_DIRETO
}

func (m *Metadados) GetExtensao() Metadados_Extensao {
	if m != nil {
		return m.Extensao
	}
	return Metadados_PDF
}

func (m *Metadados) GetEstritamenteTabular() bool {
	if m != nil {
		return m.EstritamenteTabular
	}
	return false
}

func (m *Metadados) GetFormatoConsistente() bool {
	if m != nil {
		return m.FormatoConsistente
	}
	return false
}

func (m *Metadados) GetTemMatricula() bool {
	if m != nil {
		return m.TemMatricula
	}
	return false
}

func (m *Metadados) GetTemLotacao() bool {
	if m != nil {
		return m.TemLotacao
	}
	return false
}

func (m *Metadados) GetTemCargo() bool {
	if m != nil {
		return m.TemCargo
	}
	return false
}

func (m *Metadados) GetFormatoAberto() bool {
	if m != nil {
		return m.FormatoAberto
	}
	return false
}

func (m *Metadados) GetReceitaBase() Metadados_OpcoesDetalhamento {
	if m != nil {
		return m.ReceitaBase
	}
	return Metadados_AUSENCIA
}

func (m *Metadados) GetOutrasReceitas() Metadados_OpcoesDetalhamento {
	if m != nil {
		return m.OutrasReceitas
	}
	return Metadados_AUSENCIA
}

func (m *Metadados) GetDespesas() Metadados_OpcoesDetalhamento {
	if m != nil {
		return m.Despesas
	}
	return Metadados_AUSENCIA
}

func (m *Metadados) GetIndiceCompletude() float32 {
	if m != nil {
		return m.IndiceCompletude
	}
	return 0
}

func (m *Metadados) GetIndiceFacilidade() float32 {
	if m != nil {
		return m.IndiceFacilidade
	}
	return 0
}

func (m *Metadados) GetIndiceTransparencia() float32 {
	if m != nil {
		return m.IndiceTransparencia
	}
	return 0
}

func init() {
	proto.RegisterEnum("ContraCheque_Tipo", ContraCheque_Tipo_name, ContraCheque_Tipo_value)
	proto.RegisterEnum("Remuneracao_Natureza", Remuneracao_Natureza_name, Remuneracao_Natureza_value)
	proto.RegisterEnum("Remuneracao_TipoReceita", Remuneracao_TipoReceita_name, Remuneracao_TipoReceita_value)
	proto.RegisterEnum("Metadados_FormaDeAcesso", Metadados_FormaDeAcesso_name, Metadados_FormaDeAcesso_value)
	proto.RegisterEnum("Metadados_Extensao", Metadados_Extensao_name, Metadados_Extensao_value)
	proto.RegisterEnum("Metadados_OpcoesDetalhamento", Metadados_OpcoesDetalhamento_name, Metadados_OpcoesDetalhamento_value)
	proto.RegisterType((*ResultadoColeta)(nil), "ResultadoColeta")
	proto.RegisterType((*ProcInfo)(nil), "ProcInfo")
	proto.RegisterType((*Coleta)(nil), "Coleta")
	proto.RegisterType((*FolhaDePagamento)(nil), "FolhaDePagamento")
	proto.RegisterType((*ContraCheque)(nil), "ContraCheque")
	proto.RegisterType((*Remuneracoes)(nil), "Remuneracoes")
	proto.RegisterType((*Remuneracao)(nil), "Remuneracao")
	proto.RegisterType((*Metadados)(nil), "Metadados")
}

func init() { proto.RegisterFile("coleta.proto", fileDescriptor_6d118783d7815953) }

var fileDescriptor_6d118783d7815953 = []byte{
	// 1224 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x56, 0xcd, 0x6e, 0xe3, 0xb6,
	0x16, 0x8e, 0x9c, 0xd8, 0x91, 0x8f, 0x7f, 0xa2, 0x61, 0xe6, 0x0e, 0x84, 0x99, 0x7b, 0x91, 0x5c,
	0xb5, 0xd3, 0x06, 0x28, 0xa0, 0x74, 0xdc, 0x55, 0x51, 0xa0, 0xa8, 0x62, 0x3b, 0x1d, 0xb7, 0x71,
	0x1c, 0xd0, 0xce, 0xa0, 0x98, 0x2e, 0x0c, 0x5a, 0xa2, 0x1d, 0x15, 0x92, 0xe8, 0x21, 0x29, 0xa3,
	0xe8, 0xab, 0x74, 0xdb, 0x65, 0x5f, 0xa2, 0x4f, 0xd2, 0x17, 0xe9, 0xa2, 0x20, 0x29, 0xc9, 0xca,
	0xcc, 0x66, 0x56, 0xe1, 0xf9, 0xbe, 0x8f, 0x87, 0xc7, 0xdf, 0x39, 0xa4, 0x02, 0xdd, 0x90, 0x25,
	0x54, 0x12, 0x7f, 0xcb, 0x99, 0x64, 0xcf, 0xcf, 0x36, 0x8c, 0x6d, 0x12, 0x7a, 0xa9, 0xa3, 0x55,
	0xbe, 0xbe, 0x94, 0x71, 0x4a, 0x85, 0x24, 0xe9, 0xd6, 0x08, 0xbc, 0x3f, 0x2d, 0x38, 0xc1, 0x54,
	0xe4, 0x89, 0x24, 0x11, 0x1b, 0xea, 0xad, 0xe8, 0x0c, 0x5a, 0x26, 0x89, 0x6b, 0x9d, 0x5b, 0x17,
	0x9d, 0xc1, 0xb1, 0x6f, 0x08, 0x5c, 0xc0, 0xe8, 0x73, 0x68, 0xae, 0x59, 0xf2, 0x40, 0xdc, 0x86,
	0xe6, 0x9f, 0xf8, 0xd7, 0x2a, 0x1a, 0xd1, 0x3b, 0xb2, 0x21, 0x29, 0xcd, 0x24, 0xc3, 0x86, 0x47,
	0x2f, 0xc1, 0xde, 0x72, 0x16, 0xc6, 0xd9, 0x9a, 0xb9, 0x87, 0x5a, 0xdb, 0xf6, 0xef, 0x38, 0x0b,
	0x27, 0xd9, 0x9a, 0xe1, 0x8a, 0x42, 0x17, 0xd0, 0x4e, 0xa9, 0x24, 0x11, 0x89, 0x98, 0x70, 0x8f,
	0xb4, 0x0e, 0xfc, 0x69, 0x89, 0xe0, 0x3d, 0xe9, 0xfd, 0x61, 0x81, 0x5d, 0x26, 0x40, 0x4f, 0xa1,
	0x29, 0x64, 0x14, 0x67, 0xba, 0xcc, 0x36, 0x36, 0x01, 0x7a, 0x06, 0x2d, 0x21, 0x23, 0x96, 0x4b,
	0x5d, 0x5d, 0x1b, 0x17, 0x51, 0x81, 0x53, 0xce, 0x75, 0x25, 0x06, 0xa7, 0x9c, 0x23, 0x07, 0x0e,
	0xc3, 0x34, 0xd2, 0xc7, 0xb6, 0xb1, 0x5a, 0x2a, 0x65, 0x98, 0x46, 0xa3, 0x98, 0xbb, 0x4d, 0xa3,
	0x34, 0x91, 0xc9, 0x40, 0x64, 0x2e, 0xdc, 0xd6, 0xb9, 0x75, 0xd1, 0xc4, 0x45, 0xa4, 0x32, 0xd0,
	0x6c, 0xe7, 0x1e, 0x9f, 0x1f, 0xaa, 0x0c, 0x34, 0xdb, 0x79, 0x7f, 0x35, 0xa0, 0x55, 0x98, 0xf9,
	0x7f, 0xe8, 0x86, 0x0f, 0x64, 0x47, 0x97, 0x35, 0x4b, 0xdb, 0xb8, 0xa3, 0xb1, 0x42, 0xf2, 0x14,
	0x9a, 0x8c, 0x6f, 0x08, 0x2b, 0x0a, 0x36, 0x81, 0xca, 0x9a, 0x52, 0xa1, 0x8b, 0x6d, 0x62, 0xb5,
	0x54, 0x08, 0xc9, 0x98, 0xae, 0xb4, 0x89, 0xd5, 0x12, 0x8d, 0xc1, 0xa9, 0x1a, 0x5a, 0x1e, 0xd0,
	0xd4, 0xfe, 0x3d, 0xf7, 0x4d, 0xe7, 0xfd, 0xb2, 0xf3, 0xfe, 0xa2, 0x14, 0xe2, 0x93, 0x6a, 0x4f,
	0x51, 0xc0, 0x25, 0x9c, 0x72, 0xba, 0x65, 0x22, 0x96, 0x8c, 0xc7, 0xcc, 0x24, 0x62, 0x5c, 0xff,
	0xca, 0x36, 0x46, 0x35, 0x6a, 0x68, 0x18, 0xf4, 0x12, 0xfa, 0x3b, 0xca, 0x05, 0xd9, 0x6b, 0x8f,
	0xb5, 0xb6, 0x67, 0xd0, 0x52, 0x76, 0x06, 0x9d, 0x28, 0xe6, 0x95, 0xc6, 0xd6, 0x1a, 0x88, 0x62,
	0x5e, 0x0a, 0x9e, 0x83, 0x4d, 0xf8, 0xbb, 0x3c, 0xde, 0x31, 0xe1, 0xb6, 0xb5, 0x7d, 0x55, 0xec,
	0x5d, 0x83, 0xf3, 0xfe, 0x58, 0xa1, 0x01, 0xf4, 0x42, 0x96, 0x49, 0x4e, 0x96, 0xe1, 0x03, 0x7d,
	0x97, 0x53, 0xd7, 0x3a, 0x3f, 0xbc, 0xe8, 0x0c, 0x7a, 0xfe, 0x50, 0xa3, 0x43, 0x0d, 0xe2, 0x6e,
	0x58, 0x8b, 0xbc, 0xbf, 0x1b, 0xd0, 0xad, 0xd3, 0xe8, 0x02, 0x9c, 0x38, 0x5a, 0xbe, 0x9f, 0x47,
	0x95, 0xd6, 0x8f, 0xa3, 0x47, 0xca, 0xf7, 0x7b, 0xd7, 0xf8, 0xb0, 0x77, 0x08, 0x8e, 0x32, 0x96,
	0xd2, 0x62, 0xa6, 0xf4, 0x1a, 0xfd, 0x17, 0xda, 0x29, 0x91, 0x3c, 0x0e, 0xf3, 0x84, 0x14, 0x73,
	0xb5, 0x07, 0xd4, 0x14, 0xad, 0xf3, 0x2c, 0x24, 0xac, 0x9c, 0x2e, 0x13, 0x29, 0x4f, 0x13, 0x16,
	0x92, 0x64, 0x29, 0x39, 0x59, 0x91, 0xe4, 0x81, 0x15, 0xfe, 0xf7, 0x34, 0xba, 0x28, 0x40, 0xf4,
	0x19, 0x1c, 0xc9, 0x78, 0xcb, 0xb4, 0xe1, 0xfd, 0x01, 0x7a, 0xf4, 0xcb, 0xfd, 0x45, 0xbc, 0x65,
	0x58, 0xf3, 0x6a, 0xa8, 0x88, 0x8c, 0x77, 0x4c, 0xbb, 0x6e, 0x63, 0x13, 0xa0, 0x57, 0xd0, 0xe5,
	0x34, 0xcd, 0x33, 0xca, 0x49, 0xc8, 0xa8, 0x32, 0xdd, 0xd2, 0xfe, 0xe1, 0x1a, 0x88, 0x1f, 0x49,
	0xbc, 0x73, 0x38, 0x52, 0x69, 0x11, 0x40, 0x6b, 0x3a, 0x9e, 0x5e, 0xe1, 0x99, 0x73, 0x80, 0xba,
	0x60, 0xcf, 0xc7, 0xf8, 0xcd, 0x64, 0x34, 0xc3, 0x8e, 0xe5, 0x7d, 0x0b, 0xdd, 0xfa, 0x7e, 0xe4,
	0x43, 0xa7, 0xca, 0x40, 0x58, 0xd1, 0xa3, 0xee, 0xfe, 0x0c, 0xc2, 0x70, 0x5d, 0xe0, 0xfd, 0x63,
	0x41, 0xa7, 0x46, 0xa2, 0x57, 0x60, 0x67, 0x44, 0xe6, 0x9c, 0xfe, 0x66, 0xae, 0x4b, 0x7f, 0xf0,
	0x9f, 0xfa, 0x66, 0xff, 0xb6, 0x20, 0x71, 0x25, 0x53, 0x96, 0x87, 0x44, 0xd2, 0x0d, 0xe3, 0x71,
	0xd9, 0xa6, 0x3d, 0xa0, 0x9a, 0x14, 0x4b, 0x9a, 0x96, 0x4d, 0x52, 0x6b, 0xe5, 0xcf, 0x8e, 0x24,
	0x8c, 0xeb, 0x06, 0x59, 0xd8, 0x04, 0xe8, 0x1b, 0xe8, 0x2a, 0xf7, 0x96, 0x9c, 0x86, 0x34, 0x2e,
	0x2e, 0x53, 0x7f, 0xe0, 0x3e, 0x3a, 0x5e, 0x9b, 0x6c, 0x78, 0xdc, 0x91, 0xfb, 0xc0, 0x73, 0xc1,
	0x2e, 0x4b, 0x43, 0x4d, 0xb0, 0xb0, 0x73, 0xa0, 0xfe, 0x8c, 0x1c, 0xcb, 0x7b, 0x01, 0x9d, 0xda,
	0x2e, 0x85, 0x5e, 0x19, 0x72, 0xe6, 0x58, 0xde, 0xef, 0xc7, 0xd0, 0xae, 0x1e, 0x3b, 0xf4, 0x25,
	0xb4, 0x48, 0x48, 0x85, 0x30, 0x0f, 0xa6, 0x3a, 0xbb, 0xe2, 0xfc, 0x6b, 0xc6, 0x53, 0x32, 0xa2,
	0x81, 0xe6, 0x71, 0xa1, 0x43, 0x97, 0x60, 0xd3, 0x5f, 0x25, 0xcd, 0x04, 0x31, 0x6f, 0x43, 0x7f,
	0x70, 0x5a, 0xdb, 0x33, 0x2e, 0x28, 0x5c, 0x89, 0xd0, 0x2b, 0x78, 0x4a, 0x85, 0xe4, 0xb1, 0xd4,
	0xb7, 0x8a, 0x2e, 0x25, 0x59, 0xe5, 0x09, 0x31, 0xaf, 0x9d, 0x8d, 0x4f, 0xeb, 0xdc, 0xc2, 0x50,
	0xea, 0x85, 0x58, 0xab, 0xc3, 0xa5, 0xba, 0xf1, 0x99, 0x88, 0x85, 0x54, 0xac, 0x9e, 0x50, 0x1b,
	0xa3, 0x82, 0x1a, 0xee, 0x19, 0xf4, 0x09, 0xf4, 0x24, 0x4d, 0x97, 0xfb, 0x7b, 0x70, 0xac, 0xa5,
	0x5d, 0x49, 0xd3, 0x69, 0x75, 0x15, 0xce, 0xa0, 0xa3, 0x44, 0x09, 0x93, 0x7a, 0x50, 0xcc, 0xa4,
	0x82, 0xa4, 0xe9, 0x8d, 0x41, 0xd0, 0x0b, 0x68, 0x2b, 0x41, 0x48, 0xf8, 0x86, 0xe9, 0x59, 0xb5,
	0xb1, 0x2d, 0x69, 0x3a, 0x54, 0xb1, 0xba, 0x30, 0x65, 0x4d, 0x64, 0x45, 0xb9, 0x64, 0x2e, 0x68,
	0x45, 0xaf, 0x40, 0x03, 0x0d, 0xa2, 0xef, 0xd4, 0xc8, 0x6b, 0xdf, 0x97, 0x2b, 0x22, 0xa8, 0xdb,
	0xd1, 0x16, 0xfd, 0xaf, 0x66, 0xd1, 0x6c, 0xab, 0xc6, 0x76, 0x44, 0x25, 0x49, 0x1e, 0x8a, 0xef,
	0x57, 0xa7, 0xd8, 0x72, 0x45, 0x04, 0x45, 0xd7, 0x70, 0xc2, 0x72, 0xc9, 0x89, 0x28, 0xc7, 0x42,
	0xb8, 0xdd, 0x8f, 0x49, 0xd2, 0x37, 0xbb, 0x8a, 0xae, 0x0b, 0xf4, 0x35, 0xd8, 0x11, 0x15, 0x5b,
	0x2a, 0x88, 0x70, 0x7b, 0x1f, 0x93, 0xa0, 0x92, 0xa3, 0x2f, 0xe0, 0x49, 0x9c, 0x45, 0x71, 0xa8,
	0x9e, 0xa2, 0x74, 0x9b, 0x50, 0x99, 0x47, 0xd4, 0xed, 0x9f, 0x5b, 0x17, 0x0d, 0xec, 0x18, 0x62,
	0x58, 0xe1, 0x35, 0xf1, 0x9a, 0x84, 0x71, 0x12, 0x47, 0x24, 0xa2, 0xee, 0x49, 0x5d, 0x7c, 0x5d,
	0xe1, 0x6a, 0x18, 0x0a, 0xb1, 0xe4, 0x24, 0x13, 0x5b, 0xc2, 0x69, 0x16, 0xc6, 0xc4, 0x75, 0xb4,
	0xfe, 0xd4, 0x70, 0x8b, 0x3a, 0xe5, 0xfd, 0x0c, 0xbd, 0x47, 0x93, 0x88, 0x9e, 0x40, 0x2f, 0x18,
	0x8e, 0xe7, 0xf3, 0xd9, 0x72, 0x34, 0xc1, 0xe3, 0x85, 0x7a, 0x21, 0x9e, 0x01, 0xba, 0x1d, 0x2b,
	0x6c, 0xb2, 0x08, 0x96, 0x38, 0x98, 0xdf, 0x05, 0xdf, 0x8f, 0xa7, 0x8e, 0x85, 0xce, 0xe0, 0xc5,
	0x1e, 0x9f, 0x4f, 0xa6, 0xf7, 0x37, 0xc1, 0x30, 0x98, 0x2d, 0xef, 0xe7, 0xf7, 0x01, 0x9e, 0xcc,
	0x9c, 0x86, 0xf7, 0x23, 0xd8, 0xe5, 0xc8, 0xa2, 0x63, 0x38, 0xbc, 0x1b, 0x5d, 0x3b, 0x07, 0x6a,
	0x31, 0x1b, 0xcd, 0x1d, 0x4b, 0x2d, 0x7e, 0xba, 0x99, 0x3b, 0x0d, 0x64, 0xc3, 0xd1, 0x0f, 0xf3,
	0xd9, 0xad, 0x73, 0xa8, 0xa0, 0xe1, 0xfc, 0x8d, 0x73, 0xa4, 0xa0, 0xd7, 0x8b, 0xe9, 0x8d, 0xd3,
	0x34, 0xf2, 0x85, 0xd3, 0xf2, 0x02, 0x40, 0x1f, 0xda, 0xaa, 0x5e, 0xaf, 0xe0, 0x7e, 0x3e, 0xbe,
	0x1d, 0x4e, 0x02, 0xe7, 0x00, 0xf5, 0x01, 0xe6, 0xf7, 0xd3, 0x00, 0x4f, 0xde, 0x06, 0xa3, 0x99,
	0x63, 0xa1, 0x1e, 0xb4, 0x47, 0xe3, 0x45, 0x70, 0xf3, 0x5a, 0x85, 0x8d, 0xab, 0x4f, 0xdf, 0x7a,
	0x9b, 0x58, 0x3e, 0xe4, 0x2b, 0x3f, 0x64, 0xe9, 0xa5, 0x6e, 0xd5, 0x2f, 0xb9, 0x58, 0x71, 0xf3,
	0x2f, 0xd5, 0xa5, 0xf9, 0x32, 0xac, 0x5a, 0x3a, 0xfa, 0xea, 0xdf, 0x00, 0x00, 0x00, 0xff, 0xff,
	0xb0, 0xe5, 0x50, 0x1c, 0x7e, 0x09, 0x00, 0x00,
}
