// Code generated by protoc-gen-go. DO NOT EDIT.
// source: pipeline.proto

package pipeline

import (
	fmt "fmt"
	coleta "github.com/dadosjusbr/proto/coleta"
	proto "github.com/golang/protobuf/proto"
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

type ResultadoExecucao struct {
	Pr                   *ResultadoEmpacotamento `protobuf:"bytes,1,opt,name=pr,proto3" json:"pr,omitempty"`
	Rc                   *coleta.ResultadoColeta `protobuf:"bytes,2,opt,name=rc,proto3" json:"rc,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                `json:"-"`
	XXX_unrecognized     []byte                  `json:"-"`
	XXX_sizecache        int32                   `json:"-"`
}

func (m *ResultadoExecucao) Reset()         { *m = ResultadoExecucao{} }
func (m *ResultadoExecucao) String() string { return proto.CompactTextString(m) }
func (*ResultadoExecucao) ProtoMessage()    {}
func (*ResultadoExecucao) Descriptor() ([]byte, []int) {
	return fileDescriptor_7ac67a7adf3df9c7, []int{0}
}

func (m *ResultadoExecucao) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ResultadoExecucao.Unmarshal(m, b)
}
func (m *ResultadoExecucao) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ResultadoExecucao.Marshal(b, m, deterministic)
}
func (m *ResultadoExecucao) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ResultadoExecucao.Merge(m, src)
}
func (m *ResultadoExecucao) XXX_Size() int {
	return xxx_messageInfo_ResultadoExecucao.Size(m)
}
func (m *ResultadoExecucao) XXX_DiscardUnknown() {
	xxx_messageInfo_ResultadoExecucao.DiscardUnknown(m)
}

var xxx_messageInfo_ResultadoExecucao proto.InternalMessageInfo

func (m *ResultadoExecucao) GetPr() *ResultadoEmpacotamento {
	if m != nil {
		return m.Pr
	}
	return nil
}

func (m *ResultadoExecucao) GetRc() *coleta.ResultadoColeta {
	if m != nil {
		return m.Rc
	}
	return nil
}

// PackagingResult holds the result of the package step, which creates the datapackage.
type ResultadoEmpacotamento struct {
	Pacote               string           `protobuf:"bytes,1,opt,name=pacote,proto3" json:"pacote,omitempty"`
	Procinfo             *coleta.ProcInfo `protobuf:"bytes,2,opt,name=procinfo,proto3" json:"procinfo,omitempty"`
	XXX_NoUnkeyedLiteral struct{}         `json:"-"`
	XXX_unrecognized     []byte           `json:"-"`
	XXX_sizecache        int32            `json:"-"`
}

func (m *ResultadoEmpacotamento) Reset()         { *m = ResultadoEmpacotamento{} }
func (m *ResultadoEmpacotamento) String() string { return proto.CompactTextString(m) }
func (*ResultadoEmpacotamento) ProtoMessage()    {}
func (*ResultadoEmpacotamento) Descriptor() ([]byte, []int) {
	return fileDescriptor_7ac67a7adf3df9c7, []int{1}
}

func (m *ResultadoEmpacotamento) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_ResultadoEmpacotamento.Unmarshal(m, b)
}
func (m *ResultadoEmpacotamento) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_ResultadoEmpacotamento.Marshal(b, m, deterministic)
}
func (m *ResultadoEmpacotamento) XXX_Merge(src proto.Message) {
	xxx_messageInfo_ResultadoEmpacotamento.Merge(m, src)
}
func (m *ResultadoEmpacotamento) XXX_Size() int {
	return xxx_messageInfo_ResultadoEmpacotamento.Size(m)
}
func (m *ResultadoEmpacotamento) XXX_DiscardUnknown() {
	xxx_messageInfo_ResultadoEmpacotamento.DiscardUnknown(m)
}

var xxx_messageInfo_ResultadoEmpacotamento proto.InternalMessageInfo

func (m *ResultadoEmpacotamento) GetPacote() string {
	if m != nil {
		return m.Pacote
	}
	return ""
}

func (m *ResultadoEmpacotamento) GetProcinfo() *coleta.ProcInfo {
	if m != nil {
		return m.Procinfo
	}
	return nil
}

func init() {
	proto.RegisterType((*ResultadoExecucao)(nil), "ResultadoExecucao")
	proto.RegisterType((*ResultadoEmpacotamento)(nil), "ResultadoEmpacotamento")
}

func init() { proto.RegisterFile("pipeline.proto", fileDescriptor_7ac67a7adf3df9c7) }

var fileDescriptor_7ac67a7adf3df9c7 = []byte{
	// 205 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x6c, 0x8f, 0x4f, 0x4b, 0xc4, 0x30,
	0x10, 0xc5, 0x69, 0x0e, 0xc5, 0x46, 0x11, 0xcd, 0xa1, 0x16, 0x4f, 0xa5, 0xf8, 0xef, 0x94, 0x82,
	0x7e, 0x03, 0xc5, 0x83, 0x37, 0xc9, 0x45, 0xf0, 0x20, 0xa4, 0xd3, 0xd4, 0xcd, 0xd2, 0x66, 0xc2,
	0x34, 0x81, 0xfd, 0xf8, 0x0b, 0xd9, 0xee, 0xf6, 0xb2, 0xc7, 0x1f, 0xef, 0xcd, 0x3c, 0x7e, 0xfc,
	0xda, 0x5b, 0x6f, 0x46, 0xeb, 0x8c, 0xf4, 0x84, 0x01, 0xef, 0xaf, 0x00, 0x47, 0x13, 0xf4, 0x81,
	0x9a, 0x3f, 0x7e, 0xab, 0xcc, 0x1c, 0xc7, 0xa0, 0x7b, 0xfc, 0xdc, 0x19, 0x88, 0xa0, 0x51, 0x3c,
	0x73, 0xe6, 0xa9, 0xca, 0xea, 0xec, 0xe5, 0xf2, 0xf5, 0x4e, 0xae, 0xf9, 0xe4, 0x35, 0x60, 0xd0,
	0x93, 0x71, 0x01, 0x15, 0xf3, 0x24, 0x6a, 0xce, 0x08, 0x2a, 0x96, 0x8a, 0x37, 0x6b, 0xf1, 0x23,
	0x2d, 0x28, 0x46, 0xd0, 0xfc, 0xf0, 0xf2, 0xfc, 0xbd, 0x28, 0x79, 0x9e, 0xd0, 0xa4, 0xa1, 0x42,
	0x2d, 0x24, 0x1e, 0xf9, 0x85, 0x27, 0x04, 0xeb, 0x06, 0x5c, 0x3e, 0x17, 0xf2, 0x9b, 0x10, 0xbe,
	0xdc, 0x80, 0xea, 0x14, 0xbd, 0x3f, 0xfd, 0x3e, 0xfc, 0xdb, 0xb0, 0x89, 0x9d, 0x04, 0x9c, 0xda,
	0x5e, 0xf7, 0x38, 0x6f, 0xe3, 0xdc, 0x51, 0x9b, 0xbc, 0xda, 0xa3, 0x74, 0x97, 0x27, 0x7e, 0xdb,
	0x07, 0x00, 0x00, 0xff, 0xff, 0x44, 0x80, 0xfe, 0x2a, 0x07, 0x01, 0x00, 0x00,
}
