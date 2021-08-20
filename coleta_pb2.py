# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coleta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='coleta.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\007./proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63oleta.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"q\n\x0fResultadoColeta\x12\x17\n\x06\x63oleta\x18\x01 \x01(\x0b\x32\x07.Coleta\x12#\n\x0cremuneracoes\x18\x02 \x01(\x0b\x32\r.Remuneracoes\x12 \n\x05\x66olha\x18\x03 \x01(\x0b\x32\x11.FolhaDePagamento\"\xc7\x01\n\x06\x43oleta\x12\x14\n\x0c\x63have_coleta\x18\x01 \x01(\t\x12\r\n\x05orgao\x18\x02 \x01(\t\x12\x0b\n\x03mes\x18\x03 \x01(\x05\x12\x0b\n\x03\x61no\x18\x04 \x01(\x05\x12\x34\n\x10timestamp_coleta\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13repositorio_coletor\x18\x06 \x01(\t\x12\x16\n\x0eversao_coletor\x18\x07 \x01(\t\x12\x13\n\x0b\x64ir_coletor\x18\x08 \x01(\t\"8\n\x10\x46olhaDePagamento\x12$\n\rcontra_cheque\x18\x01 \x03(\x0b\x32\r.ContraCheque\"\xda\x01\n\x0c\x43ontraCheque\x12\x18\n\x10id_contra_cheque\x18\x01 \x01(\t\x12\x14\n\x0c\x63have_coleta\x18\x02 \x01(\t\x12\x0c\n\x04nome\x18\x03 \x01(\t\x12\x11\n\tmatricula\x18\x04 \x01(\t\x12\x0e\n\x06\x66uncao\x18\x05 \x01(\t\x12\x16\n\x0elocal_trabalho\x18\x06 \x01(\t\x12 \n\x04tipo\x18\x07 \x01(\x0e\x32\x12.ContraCheque.Tipo\x12\r\n\x05\x61tivo\x18\x08 \x01(\x08\" \n\x04Tipo\x12\n\n\x06MEMBRO\x10\x00\x12\x0c\n\x08SERVIDOR\x10\x01\"1\n\x0cRemuneracoes\x12!\n\x0bremuneracao\x18\x01 \x03(\x0b\x32\x0c.Remuneracao\"\xb0\x01\n\x0bRemuneracao\x12\x18\n\x10id_contra_cheque\x18\x01 \x01(\t\x12\x14\n\x0c\x63have_coleta\x18\x02 \x01(\t\x12\'\n\x08natureza\x18\x03 \x01(\x0e\x32\x15.Remuneracao.Natureza\x12\x11\n\tcategoria\x18\x04 \x01(\t\x12\x0c\n\x04item\x18\x05 \x01(\t\x12\r\n\x05valor\x18\x06 \x01(\x01\"\x18\n\x08Natureza\x12\x05\n\x01R\x10\x00\x12\x05\n\x01\x44\x10\x01\x42\tZ\x07./protob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_CONTRACHEQUE_TIPO = _descriptor.EnumDescriptor(
  name='Tipo',
  full_name='ContraCheque.Tipo',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MEMBRO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVIDOR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=611,
  serialized_end=643,
)
_sym_db.RegisterEnumDescriptor(_CONTRACHEQUE_TIPO)

_REMUNERACAO_NATUREZA = _descriptor.EnumDescriptor(
  name='Natureza',
  full_name='Remuneracao.Natureza',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='R', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='D', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=849,
  serialized_end=873,
)
_sym_db.RegisterEnumDescriptor(_REMUNERACAO_NATUREZA)


_RESULTADOCOLETA = _descriptor.Descriptor(
  name='ResultadoColeta',
  full_name='ResultadoColeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='coleta', full_name='ResultadoColeta.coleta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remuneracoes', full_name='ResultadoColeta.remuneracoes', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='folha', full_name='ResultadoColeta.folha', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=162,
)


_COLETA = _descriptor.Descriptor(
  name='Coleta',
  full_name='Coleta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chave_coleta', full_name='Coleta.chave_coleta', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='orgao', full_name='Coleta.orgao', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mes', full_name='Coleta.mes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ano', full_name='Coleta.ano', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp_coleta', full_name='Coleta.timestamp_coleta', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repositorio_coletor', full_name='Coleta.repositorio_coletor', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versao_coletor', full_name='Coleta.versao_coletor', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dir_coletor', full_name='Coleta.dir_coletor', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=364,
)


_FOLHADEPAGAMENTO = _descriptor.Descriptor(
  name='FolhaDePagamento',
  full_name='FolhaDePagamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='contra_cheque', full_name='FolhaDePagamento.contra_cheque', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=422,
)


_CONTRACHEQUE = _descriptor.Descriptor(
  name='ContraCheque',
  full_name='ContraCheque',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_contra_cheque', full_name='ContraCheque.id_contra_cheque', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chave_coleta', full_name='ContraCheque.chave_coleta', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nome', full_name='ContraCheque.nome', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matricula', full_name='ContraCheque.matricula', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funcao', full_name='ContraCheque.funcao', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local_trabalho', full_name='ContraCheque.local_trabalho', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tipo', full_name='ContraCheque.tipo', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ativo', full_name='ContraCheque.ativo', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONTRACHEQUE_TIPO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=643,
)


_REMUNERACOES = _descriptor.Descriptor(
  name='Remuneracoes',
  full_name='Remuneracoes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='remuneracao', full_name='Remuneracoes.remuneracao', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=645,
  serialized_end=694,
)


_REMUNERACAO = _descriptor.Descriptor(
  name='Remuneracao',
  full_name='Remuneracao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_contra_cheque', full_name='Remuneracao.id_contra_cheque', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='chave_coleta', full_name='Remuneracao.chave_coleta', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='natureza', full_name='Remuneracao.natureza', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='categoria', full_name='Remuneracao.categoria', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='item', full_name='Remuneracao.item', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valor', full_name='Remuneracao.valor', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REMUNERACAO_NATUREZA,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=697,
  serialized_end=873,
)

_RESULTADOCOLETA.fields_by_name['coleta'].message_type = _COLETA
_RESULTADOCOLETA.fields_by_name['remuneracoes'].message_type = _REMUNERACOES
_RESULTADOCOLETA.fields_by_name['folha'].message_type = _FOLHADEPAGAMENTO
_COLETA.fields_by_name['timestamp_coleta'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FOLHADEPAGAMENTO.fields_by_name['contra_cheque'].message_type = _CONTRACHEQUE
_CONTRACHEQUE.fields_by_name['tipo'].enum_type = _CONTRACHEQUE_TIPO
_CONTRACHEQUE_TIPO.containing_type = _CONTRACHEQUE
_REMUNERACOES.fields_by_name['remuneracao'].message_type = _REMUNERACAO
_REMUNERACAO.fields_by_name['natureza'].enum_type = _REMUNERACAO_NATUREZA
_REMUNERACAO_NATUREZA.containing_type = _REMUNERACAO
DESCRIPTOR.message_types_by_name['ResultadoColeta'] = _RESULTADOCOLETA
DESCRIPTOR.message_types_by_name['Coleta'] = _COLETA
DESCRIPTOR.message_types_by_name['FolhaDePagamento'] = _FOLHADEPAGAMENTO
DESCRIPTOR.message_types_by_name['ContraCheque'] = _CONTRACHEQUE
DESCRIPTOR.message_types_by_name['Remuneracoes'] = _REMUNERACOES
DESCRIPTOR.message_types_by_name['Remuneracao'] = _REMUNERACAO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResultadoColeta = _reflection.GeneratedProtocolMessageType('ResultadoColeta', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADOCOLETA,
  '__module__' : 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoColeta)
  })
_sym_db.RegisterMessage(ResultadoColeta)

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


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
