# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pipeline.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import coleta_pb2 as coleta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epipeline.proto\x1a\x0c\x63oleta.proto\"V\n\x11ResultadoExecucao\x12#\n\x02pr\x18\x01 \x01(\x0b\x32\x17.ResultadoEmpacotamento\x12\x1c\n\x02rc\x18\x02 \x01(\x0b\x32\x10.ResultadoColeta\"E\n\x16ResultadoEmpacotamento\x12\x0e\n\x06pacote\x18\x01 \x01(\t\x12\x1b\n\x08procinfo\x18\x02 \x01(\x0b\x32\t.ProcInfoB&Z$github.com/dadosjusbr/proto/pipelineb\x06proto3')



_RESULTADOEXECUCAO = DESCRIPTOR.message_types_by_name['ResultadoExecucao']
_RESULTADOEMPACOTAMENTO = DESCRIPTOR.message_types_by_name['ResultadoEmpacotamento']
ResultadoExecucao = _reflection.GeneratedProtocolMessageType('ResultadoExecucao', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADOEXECUCAO,
  '__module__' : 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoExecucao)
  })
_sym_db.RegisterMessage(ResultadoExecucao)

ResultadoEmpacotamento = _reflection.GeneratedProtocolMessageType('ResultadoEmpacotamento', (_message.Message,), {
  'DESCRIPTOR' : _RESULTADOEMPACOTAMENTO,
  '__module__' : 'pipeline_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoEmpacotamento)
  })
_sym_db.RegisterMessage(ResultadoEmpacotamento)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z$github.com/dadosjusbr/proto/pipeline'
  _RESULTADOEXECUCAO._serialized_start=32
  _RESULTADOEXECUCAO._serialized_end=118
  _RESULTADOEMPACOTAMENTO._serialized_start=120
  _RESULTADOEMPACOTAMENTO._serialized_end=189
# @@protoc_insertion_point(module_scope)
