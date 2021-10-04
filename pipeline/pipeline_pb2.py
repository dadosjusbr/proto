# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipeline.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import coleta_pb2 as coleta__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pipeline.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('Z$github.com/dadosjusbr/proto/pipeline'),
  serialized_pb=_b('\n\x0epipeline.proto\x1a\x0c\x63oleta.proto\"V\n\x11ResultadoExecucao\x12#\n\x02pr\x18\x01 \x01(\x0b\x32\x17.ResultadoEmpacotamento\x12\x1c\n\x02rc\x18\x02 \x01(\x0b\x32\x10.ResultadoColeta\"E\n\x16ResultadoEmpacotamento\x12\x0e\n\x06pacote\x18\x01 \x01(\t\x12\x1b\n\x08procinfo\x18\x02 \x01(\x0b\x32\t.ProcInfoB&Z$github.com/dadosjusbr/proto/pipelineb\x06proto3')
  ,
  dependencies=[coleta__pb2.DESCRIPTOR,])




_RESULTADOEXECUCAO = _descriptor.Descriptor(
  name='ResultadoExecucao',
  full_name='ResultadoExecucao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pr', full_name='ResultadoExecucao.pr', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rc', full_name='ResultadoExecucao.rc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=118,
)


_RESULTADOEMPACOTAMENTO = _descriptor.Descriptor(
  name='ResultadoEmpacotamento',
  full_name='ResultadoEmpacotamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pacote', full_name='ResultadoEmpacotamento.pacote', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procinfo', full_name='ResultadoEmpacotamento.procinfo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=120,
  serialized_end=189,
)

_RESULTADOEXECUCAO.fields_by_name['pr'].message_type = _RESULTADOEMPACOTAMENTO
_RESULTADOEXECUCAO.fields_by_name['rc'].message_type = coleta__pb2._RESULTADOCOLETA
_RESULTADOEMPACOTAMENTO.fields_by_name['procinfo'].message_type = coleta__pb2._PROCINFO
DESCRIPTOR.message_types_by_name['ResultadoExecucao'] = _RESULTADOEXECUCAO
DESCRIPTOR.message_types_by_name['ResultadoEmpacotamento'] = _RESULTADOEMPACOTAMENTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResultadoExecucao = _reflection.GeneratedProtocolMessageType('ResultadoExecucao', (_message.Message,), dict(
  DESCRIPTOR = _RESULTADOEXECUCAO,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoExecucao)
  ))
_sym_db.RegisterMessage(ResultadoExecucao)

ResultadoEmpacotamento = _reflection.GeneratedProtocolMessageType('ResultadoEmpacotamento', (_message.Message,), dict(
  DESCRIPTOR = _RESULTADOEMPACOTAMENTO,
  __module__ = 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoEmpacotamento)
  ))
_sym_db.RegisterMessage(ResultadoEmpacotamento)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)