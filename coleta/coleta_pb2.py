# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coleta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63oleta.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x01\n\x0fResultadoColeta\x12\x17\n\x06\x63oleta\x18\x01 \x01(\x0b\x32\x07.Coleta\x12 \n\x05\x66olha\x18\x02 \x01(\x0b\x32\x11.FolhaDePagamento\x12\x1b\n\x08procinfo\x18\x03 \x01(\x0b\x32\t.ProcInfo\x12\x1d\n\tmetadados\x18\x04 \x01(\x0b\x32\n.Metadados\"s\n\x08ProcInfo\x12\r\n\x05stdin\x18\x01 \x01(\t\x12\x0e\n\x06stdout\x18\x02 \x01(\t\x12\x0e\n\x06stderr\x18\x03 \x01(\t\x12\x0b\n\x03\x63md\x18\x04 \x01(\t\x12\x0e\n\x06\x63mdDir\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\x05\x12\x0b\n\x03\x65nv\x18\x07 \x03(\t\"\xd9\x01\n\x06\x43oleta\x12\x14\n\x0c\x63have_coleta\x18\x01 \x01(\t\x12\r\n\x05orgao\x18\x02 \x01(\t\x12\x0b\n\x03mes\x18\x03 \x01(\x05\x12\x0b\n\x03\x61no\x18\x04 \x01(\x05\x12\x34\n\x10timestamp_coleta\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13repositorio_coletor\x18\x06 \x01(\t\x12\x16\n\x0eversao_coletor\x18\x07 \x01(\t\x12\x13\n\x0b\x64ir_coletor\x18\x08 \x01(\t\x12\x10\n\x08\x61rquivos\x18\t \x03(\t\"8\n\x10\x46olhaDePagamento\x12$\n\rcontra_cheque\x18\x01 \x03(\x0b\x32\r.ContraCheque\"\xff\x01\n\x0c\x43ontraCheque\x12\x18\n\x10id_contra_cheque\x18\x01 \x01(\t\x12\x14\n\x0c\x63have_coleta\x18\x02 \x01(\t\x12\x0c\n\x04nome\x18\x03 \x01(\t\x12\x11\n\tmatricula\x18\x04 \x01(\t\x12\x0e\n\x06\x66uncao\x18\x05 \x01(\t\x12\x16\n\x0elocal_trabalho\x18\x06 \x01(\t\x12 \n\x04tipo\x18\x07 \x01(\x0e\x32\x12.ContraCheque.Tipo\x12\r\n\x05\x61tivo\x18\x08 \x01(\x08\x12#\n\x0cremuneracoes\x18\t \x01(\x0b\x32\r.Remuneracoes\" \n\x04Tipo\x12\n\n\x06MEMBRO\x10\x00\x12\x0c\n\x08SERVIDOR\x10\x01\"1\n\x0cRemuneracoes\x12!\n\x0bremuneracao\x18\x01 \x03(\x0b\x32\x0c.Remuneracao\"\xcd\x01\n\x0bRemuneracao\x12\'\n\x08natureza\x18\x01 \x01(\x0e\x32\x15.Remuneracao.Natureza\x12\x11\n\tcategoria\x18\x02 \x01(\t\x12\x0c\n\x04item\x18\x03 \x01(\t\x12\r\n\x05valor\x18\x04 \x01(\x01\x12.\n\x0ctipo_receita\x18\x05 \x01(\x0e\x32\x18.Remuneracao.TipoReceita\"\x18\n\x08Natureza\x12\x05\n\x01R\x10\x00\x12\x05\n\x01\x44\x10\x01\"\x1b\n\x0bTipoReceita\x12\x05\n\x01\x42\x10\x00\x12\x05\n\x01O\x10\x01\"\x8f\x06\n\tMetadados\x12\x18\n\x10nao_requer_login\x18\x01 \x01(\x08\x12\x1a\n\x12nao_requer_captcha\x18\x02 \x01(\x08\x12(\n\x06\x61\x63\x65sso\x18\x03 \x01(\x0e\x32\x18.Metadados.FormaDeAcesso\x12%\n\x08\x65xtensao\x18\x04 \x01(\x0e\x32\x13.Metadados.Extensao\x12\x1c\n\x14\x65stritamente_tabular\x18\x05 \x01(\x08\x12\x1b\n\x13\x66ormato_consistente\x18\x06 \x01(\x08\x12\x15\n\rtem_matricula\x18\x07 \x01(\x08\x12\x13\n\x0btem_lotacao\x18\x08 \x01(\x08\x12\x11\n\ttem_cargo\x18\t \x01(\x08\x12\x33\n\x0creceita_base\x18\n \x01(\x0e\x32\x1d.Metadados.OpcoesDetalhamento\x12\x36\n\x0foutras_receitas\x18\x0b \x01(\x0e\x32\x1d.Metadados.OpcoesDetalhamento\x12/\n\x08\x64\x65spesas\x18\x0c \x01(\x0e\x32\x1d.Metadados.OpcoesDetalhamento\x12\x1e\n\x16indice_disponibilidade\x18\r \x01(\x02\x12\x1a\n\x12indice_dificuldade\x18\x0e \x01(\x02\x12\x1c\n\x14indice_transparencia\x18\x0f \x01(\x02\"y\n\rFormaDeAcesso\x12\x11\n\rACESSO_DIRETO\x10\x00\x12\x1a\n\x16\x41MIGAVEL_PARA_RASPAGEM\x10\x01\x12\x18\n\x14RASPAGEM_DIFICULTADA\x10\x02\x12\x1f\n\x1bNECESSITA_SIMULACAO_USUARIO\x10\x03\"K\n\x08\x45xtensao\x12\x07\n\x03PDF\x10\x00\x12\x07\n\x03ODS\x10\x01\x12\x07\n\x03XLS\x10\x02\x12\x08\n\x04JSON\x10\x03\x12\x07\n\x03\x43SV\x10\x04\x12\x08\n\x04HTML\x10\x05\x12\x07\n\x03ODT\x10\x06\"A\n\x12OpcoesDetalhamento\x12\x0c\n\x08\x41USENCIA\x10\x00\x12\x0e\n\nSUMARIZADO\x10\x01\x12\r\n\tDETALHADO\x10\x02\x42$Z\"github.com/dadosjusbr/proto/coletab\x06proto3')



_RESULTADOCOLETA = DESCRIPTOR.message_types_by_name['ResultadoColeta']
_PROCINFO = DESCRIPTOR.message_types_by_name['ProcInfo']
_COLETA = DESCRIPTOR.message_types_by_name['Coleta']
_FOLHADEPAGAMENTO = DESCRIPTOR.message_types_by_name['FolhaDePagamento']
_CONTRACHEQUE = DESCRIPTOR.message_types_by_name['ContraCheque']
_REMUNERACOES = DESCRIPTOR.message_types_by_name['Remuneracoes']
_REMUNERACAO = DESCRIPTOR.message_types_by_name['Remuneracao']
_METADADOS = DESCRIPTOR.message_types_by_name['Metadados']
_CONTRACHEQUE_TIPO = _CONTRACHEQUE.enum_types_by_name['Tipo']
_REMUNERACAO_NATUREZA = _REMUNERACAO.enum_types_by_name['Natureza']
_REMUNERACAO_TIPORECEITA = _REMUNERACAO.enum_types_by_name['TipoReceita']
_METADADOS_FORMADEACESSO = _METADADOS.enum_types_by_name['FormaDeAcesso']
_METADADOS_EXTENSAO = _METADADOS.enum_types_by_name['Extensao']
_METADADOS_OPCOESDETALHAMENTO = _METADADOS.enum_types_by_name['OpcoesDetalhamento']
ResultadoColeta = _reflection.GeneratedProtocolMessageType('ResultadoColeta', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADOCOLETA,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoColeta)
  })
_sym_db.RegisterMessage(ResultadoColeta)

ProcInfo = _reflection.GeneratedProtocolMessageType('ProcInfo', (_message.Message,), {
  'DESCRIPTOR' : _PROCINFO,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ProcInfo)
  })
_sym_db.RegisterMessage(ProcInfo)

Coleta = _reflection.GeneratedProtocolMessageType('Coleta', (_message.Message,), {
  'DESCRIPTOR' : _COLETA,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Coleta)
  })
_sym_db.RegisterMessage(Coleta)

FolhaDePagamento = _reflection.GeneratedProtocolMessageType('FolhaDePagamento', (_message.Message,), {
  'DESCRIPTOR' : _FOLHADEPAGAMENTO,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:FolhaDePagamento)
  })
_sym_db.RegisterMessage(FolhaDePagamento)

ContraCheque = _reflection.GeneratedProtocolMessageType('ContraCheque', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACHEQUE,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ContraCheque)
  })
_sym_db.RegisterMessage(ContraCheque)

Remuneracoes = _reflection.GeneratedProtocolMessageType('Remuneracoes', (_message.Message,), {
  'DESCRIPTOR' : _REMUNERACOES,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Remuneracoes)
  })
_sym_db.RegisterMessage(Remuneracoes)

Remuneracao = _reflection.GeneratedProtocolMessageType('Remuneracao', (_message.Message,), {
  'DESCRIPTOR' : _REMUNERACAO,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Remuneracao)
  })
_sym_db.RegisterMessage(Remuneracao)

Metadados = _reflection.GeneratedProtocolMessageType('Metadados', (_message.Message,), {
  'DESCRIPTOR' : _METADADOS,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Metadados)
  })
_sym_db.RegisterMessage(Metadados)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\"github.com/dadosjusbr/proto/coleta'
  _RESULTADOCOLETA._serialized_start=50
  _RESULTADOCOLETA._serialized_end=186
  _PROCINFO._serialized_start=188
  _PROCINFO._serialized_end=303
  _COLETA._serialized_start=306
  _COLETA._serialized_end=523
  _FOLHADEPAGAMENTO._serialized_start=525
  _FOLHADEPAGAMENTO._serialized_end=581
  _CONTRACHEQUE._serialized_start=584
  _CONTRACHEQUE._serialized_end=839
  _CONTRACHEQUE_TIPO._serialized_start=807
  _CONTRACHEQUE_TIPO._serialized_end=839
  _REMUNERACOES._serialized_start=841
  _REMUNERACOES._serialized_end=890
  _REMUNERACAO._serialized_start=893
  _REMUNERACAO._serialized_end=1098
  _REMUNERACAO_NATUREZA._serialized_start=1045
  _REMUNERACAO_NATUREZA._serialized_end=1069
  _REMUNERACAO_TIPORECEITA._serialized_start=1071
  _REMUNERACAO_TIPORECEITA._serialized_end=1098
  _METADADOS._serialized_start=1101
  _METADADOS._serialized_end=1884
  _METADADOS_FORMADEACESSO._serialized_start=1619
  _METADADOS_FORMADEACESSO._serialized_end=1740
  _METADADOS_EXTENSAO._serialized_start=1742
  _METADADOS_EXTENSAO._serialized_end=1817
  _METADADOS_OPCOESDETALHAMENTO._serialized_start=1819
  _METADADOS_OPCOESDETALHAMENTO._serialized_end=1884
# @@protoc_insertion_point(module_scope)
