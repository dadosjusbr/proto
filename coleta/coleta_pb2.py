# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coleta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
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
  serialized_options=_b('Z\"github.com/dadosjusbr/proto/coleta'),
  serialized_pb=_b('\n\x0c\x63oleta.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x01\n\x0fResultadoColeta\x12\x17\n\x06\x63oleta\x18\x01 \x01(\x0b\x32\x07.Coleta\x12 \n\x05\x66olha\x18\x02 \x01(\x0b\x32\x11.FolhaDePagamento\x12\x1b\n\x08procinfo\x18\x03 \x01(\x0b\x32\t.ProcInfo\x12\x1d\n\tmetadados\x18\x04 \x01(\x0b\x32\n.Metadados\"s\n\x08ProcInfo\x12\r\n\x05stdin\x18\x01 \x01(\t\x12\x0e\n\x06stdout\x18\x02 \x01(\t\x12\x0e\n\x06stderr\x18\x03 \x01(\t\x12\x0b\n\x03\x63md\x18\x04 \x01(\t\x12\x0e\n\x06\x63mdDir\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\x05\x12\x0b\n\x03\x65nv\x18\x07 \x03(\t\"\xd9\x01\n\x06\x43oleta\x12\x14\n\x0c\x63have_coleta\x18\x01 \x01(\t\x12\r\n\x05orgao\x18\x02 \x01(\t\x12\x0b\n\x03mes\x18\x03 \x01(\x05\x12\x0b\n\x03\x61no\x18\x04 \x01(\x05\x12\x34\n\x10timestamp_coleta\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x13repositorio_coletor\x18\x06 \x01(\t\x12\x16\n\x0eversao_coletor\x18\x07 \x01(\t\x12\x13\n\x0b\x64ir_coletor\x18\x08 \x01(\t\x12\x10\n\x08\x61rquivos\x18\t \x03(\t\"8\n\x10\x46olhaDePagamento\x12$\n\rcontra_cheque\x18\x01 \x03(\x0b\x32\r.ContraCheque\"\xff\x01\n\x0c\x43ontraCheque\x12\x18\n\x10id_contra_cheque\x18\x01 \x01(\t\x12\x14\n\x0c\x63have_coleta\x18\x02 \x01(\t\x12\x0c\n\x04nome\x18\x03 \x01(\t\x12\x11\n\tmatricula\x18\x04 \x01(\t\x12\x0e\n\x06\x66uncao\x18\x05 \x01(\t\x12\x16\n\x0elocal_trabalho\x18\x06 \x01(\t\x12 \n\x04tipo\x18\x07 \x01(\x0e\x32\x12.ContraCheque.Tipo\x12\r\n\x05\x61tivo\x18\x08 \x01(\x08\x12#\n\x0cremuneracoes\x18\t \x01(\x0b\x32\r.Remuneracoes\" \n\x04Tipo\x12\n\n\x06MEMBRO\x10\x00\x12\x0c\n\x08SERVIDOR\x10\x01\"1\n\x0cRemuneracoes\x12!\n\x0bremuneracao\x18\x01 \x03(\x0b\x32\x0c.Remuneracao\"\xcd\x01\n\x0bRemuneracao\x12\'\n\x08natureza\x18\x01 \x01(\x0e\x32\x15.Remuneracao.Natureza\x12\x11\n\tcategoria\x18\x02 \x01(\t\x12\x0c\n\x04item\x18\x03 \x01(\t\x12\r\n\x05valor\x18\x04 \x01(\x01\x12.\n\x0ctipo_receita\x18\x05 \x01(\x0e\x32\x18.Remuneracao.TipoReceita\"\x18\n\x08Natureza\x12\x05\n\x01R\x10\x00\x12\x05\n\x01\x44\x10\x01\"\x1b\n\x0bTipoReceita\x12\x05\n\x01\x42\x10\x00\x12\x05\n\x01O\x10\x01\"\xa1\x06\n\tMetadados\x12\x18\n\x10nao_requer_login\x18\x01 \x01(\x08\x12\x1a\n\x12nao_requer_captcha\x18\x02 \x01(\x08\x12(\n\x06\x61\x63\x65sso\x18\x03 \x01(\x0e\x32\x18.Metadados.FormaDeAcesso\x12%\n\x08\x65xtensao\x18\x04 \x01(\x0e\x32\x13.Metadados.Extensao\x12\x1c\n\x14\x65stritamente_tabular\x18\x05 \x01(\x08\x12\x1b\n\x13\x66ormato_consistente\x18\x06 \x01(\x08\x12\x15\n\rtem_matricula\x18\x07 \x01(\x08\x12\x13\n\x0btem_lotacao\x18\x08 \x01(\x08\x12\x11\n\ttem_cargo\x18\t \x01(\x08\x12\x16\n\x0e\x66ormato_aberto\x18\x10 \x01(\x08\x12\x33\n\x0creceita_base\x18\n \x01(\x0e\x32\x1d.Metadados.OpcoesDetalhamento\x12\x36\n\x0foutras_receitas\x18\x0b \x01(\x0e\x32\x1d.Metadados.OpcoesDetalhamento\x12/\n\x08\x64\x65spesas\x18\x0c \x01(\x0e\x32\x1d.Metadados.OpcoesDetalhamento\x12\x19\n\x11indice_completude\x18\r \x01(\x02\x12\x19\n\x11indice_facilidade\x18\x0e \x01(\x02\x12\x1c\n\x14indice_transparencia\x18\x0f \x01(\x02\"y\n\rFormaDeAcesso\x12\x11\n\rACESSO_DIRETO\x10\x00\x12\x1a\n\x16\x41MIGAVEL_PARA_RASPAGEM\x10\x01\x12\x18\n\x14RASPAGEM_DIFICULTADA\x10\x02\x12\x1f\n\x1bNECESSITA_SIMULACAO_USUARIO\x10\x03\"K\n\x08\x45xtensao\x12\x07\n\x03PDF\x10\x00\x12\x07\n\x03ODS\x10\x01\x12\x07\n\x03XLS\x10\x02\x12\x08\n\x04JSON\x10\x03\x12\x07\n\x03\x43SV\x10\x04\x12\x08\n\x04HTML\x10\x05\x12\x07\n\x03ODT\x10\x06\"A\n\x12OpcoesDetalhamento\x12\x0c\n\x08\x41USENCIA\x10\x00\x12\x0e\n\nSUMARIZADO\x10\x01\x12\r\n\tDETALHADO\x10\x02\x42$Z\"github.com/dadosjusbr/proto/coletab\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_CONTRACHEQUE_TIPO = _descriptor.EnumDescriptor(
  name='Tipo',
  full_name='ContraCheque.Tipo',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MEMBRO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVIDOR', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=807,
  serialized_end=839,
)
_sym_db.RegisterEnumDescriptor(_CONTRACHEQUE_TIPO)

_REMUNERACAO_NATUREZA = _descriptor.EnumDescriptor(
  name='Natureza',
  full_name='Remuneracao.Natureza',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='R', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='D', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1045,
  serialized_end=1069,
)
_sym_db.RegisterEnumDescriptor(_REMUNERACAO_NATUREZA)

_REMUNERACAO_TIPORECEITA = _descriptor.EnumDescriptor(
  name='TipoReceita',
  full_name='Remuneracao.TipoReceita',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='B', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='O', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1071,
  serialized_end=1098,
)
_sym_db.RegisterEnumDescriptor(_REMUNERACAO_TIPORECEITA)

_METADADOS_FORMADEACESSO = _descriptor.EnumDescriptor(
  name='FormaDeAcesso',
  full_name='Metadados.FormaDeAcesso',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACESSO_DIRETO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMIGAVEL_PARA_RASPAGEM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RASPAGEM_DIFICULTADA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NECESSITA_SIMULACAO_USUARIO', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1637,
  serialized_end=1758,
)
_sym_db.RegisterEnumDescriptor(_METADADOS_FORMADEACESSO)

_METADADOS_EXTENSAO = _descriptor.EnumDescriptor(
  name='Extensao',
  full_name='Metadados.Extensao',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PDF', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ODS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XLS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CSV', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ODT', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1760,
  serialized_end=1835,
)
_sym_db.RegisterEnumDescriptor(_METADADOS_EXTENSAO)

_METADADOS_OPCOESDETALHAMENTO = _descriptor.EnumDescriptor(
  name='OpcoesDetalhamento',
  full_name='Metadados.OpcoesDetalhamento',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUSENCIA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUMARIZADO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DETALHADO', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1837,
  serialized_end=1902,
)
_sym_db.RegisterEnumDescriptor(_METADADOS_OPCOESDETALHAMENTO)


_RESULTADOCOLETA = _descriptor.Descriptor(
  name='ResultadoColeta',
  full_name='ResultadoColeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coleta', full_name='ResultadoColeta.coleta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='folha', full_name='ResultadoColeta.folha', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procinfo', full_name='ResultadoColeta.procinfo', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadados', full_name='ResultadoColeta.metadados', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=50,
  serialized_end=186,
)


_PROCINFO = _descriptor.Descriptor(
  name='ProcInfo',
  full_name='ProcInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stdin', full_name='ProcInfo.stdin', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stdout', full_name='ProcInfo.stdout', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stderr', full_name='ProcInfo.stderr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmd', full_name='ProcInfo.cmd', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmdDir', full_name='ProcInfo.cmdDir', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ProcInfo.status', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='env', full_name='ProcInfo.env', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=188,
  serialized_end=303,
)


_COLETA = _descriptor.Descriptor(
  name='Coleta',
  full_name='Coleta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chave_coleta', full_name='Coleta.chave_coleta', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orgao', full_name='Coleta.orgao', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mes', full_name='Coleta.mes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ano', full_name='Coleta.ano', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_coleta', full_name='Coleta.timestamp_coleta', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repositorio_coletor', full_name='Coleta.repositorio_coletor', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='versao_coletor', full_name='Coleta.versao_coletor', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dir_coletor', full_name='Coleta.dir_coletor', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arquivos', full_name='Coleta.arquivos', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=306,
  serialized_end=523,
)


_FOLHADEPAGAMENTO = _descriptor.Descriptor(
  name='FolhaDePagamento',
  full_name='FolhaDePagamento',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contra_cheque', full_name='FolhaDePagamento.contra_cheque', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=525,
  serialized_end=581,
)


_CONTRACHEQUE = _descriptor.Descriptor(
  name='ContraCheque',
  full_name='ContraCheque',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_contra_cheque', full_name='ContraCheque.id_contra_cheque', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chave_coleta', full_name='ContraCheque.chave_coleta', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nome', full_name='ContraCheque.nome', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='matricula', full_name='ContraCheque.matricula', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='funcao', full_name='ContraCheque.funcao', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_trabalho', full_name='ContraCheque.local_trabalho', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tipo', full_name='ContraCheque.tipo', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ativo', full_name='ContraCheque.ativo', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remuneracoes', full_name='ContraCheque.remuneracoes', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=584,
  serialized_end=839,
)


_REMUNERACOES = _descriptor.Descriptor(
  name='Remuneracoes',
  full_name='Remuneracoes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remuneracao', full_name='Remuneracoes.remuneracao', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=841,
  serialized_end=890,
)


_REMUNERACAO = _descriptor.Descriptor(
  name='Remuneracao',
  full_name='Remuneracao',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='natureza', full_name='Remuneracao.natureza', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='categoria', full_name='Remuneracao.categoria', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item', full_name='Remuneracao.item', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valor', full_name='Remuneracao.valor', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tipo_receita', full_name='Remuneracao.tipo_receita', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REMUNERACAO_NATUREZA,
    _REMUNERACAO_TIPORECEITA,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=893,
  serialized_end=1098,
)


_METADADOS = _descriptor.Descriptor(
  name='Metadados',
  full_name='Metadados',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nao_requer_login', full_name='Metadados.nao_requer_login', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nao_requer_captcha', full_name='Metadados.nao_requer_captcha', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='acesso', full_name='Metadados.acesso', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extensao', full_name='Metadados.extensao', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='estritamente_tabular', full_name='Metadados.estritamente_tabular', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formato_consistente', full_name='Metadados.formato_consistente', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tem_matricula', full_name='Metadados.tem_matricula', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tem_lotacao', full_name='Metadados.tem_lotacao', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tem_cargo', full_name='Metadados.tem_cargo', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formato_aberto', full_name='Metadados.formato_aberto', index=9,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receita_base', full_name='Metadados.receita_base', index=10,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outras_receitas', full_name='Metadados.outras_receitas', index=11,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='despesas', full_name='Metadados.despesas', index=12,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indice_completude', full_name='Metadados.indice_completude', index=13,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indice_facilidade', full_name='Metadados.indice_facilidade', index=14,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indice_transparencia', full_name='Metadados.indice_transparencia', index=15,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METADADOS_FORMADEACESSO,
    _METADADOS_EXTENSAO,
    _METADADOS_OPCOESDETALHAMENTO,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1101,
  serialized_end=1902,
)

_RESULTADOCOLETA.fields_by_name['coleta'].message_type = _COLETA
_RESULTADOCOLETA.fields_by_name['folha'].message_type = _FOLHADEPAGAMENTO
_RESULTADOCOLETA.fields_by_name['procinfo'].message_type = _PROCINFO
_RESULTADOCOLETA.fields_by_name['metadados'].message_type = _METADADOS
_COLETA.fields_by_name['timestamp_coleta'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_FOLHADEPAGAMENTO.fields_by_name['contra_cheque'].message_type = _CONTRACHEQUE
_CONTRACHEQUE.fields_by_name['tipo'].enum_type = _CONTRACHEQUE_TIPO
_CONTRACHEQUE.fields_by_name['remuneracoes'].message_type = _REMUNERACOES
_CONTRACHEQUE_TIPO.containing_type = _CONTRACHEQUE
_REMUNERACOES.fields_by_name['remuneracao'].message_type = _REMUNERACAO
_REMUNERACAO.fields_by_name['natureza'].enum_type = _REMUNERACAO_NATUREZA
_REMUNERACAO.fields_by_name['tipo_receita'].enum_type = _REMUNERACAO_TIPORECEITA
_REMUNERACAO_NATUREZA.containing_type = _REMUNERACAO
_REMUNERACAO_TIPORECEITA.containing_type = _REMUNERACAO
_METADADOS.fields_by_name['acesso'].enum_type = _METADADOS_FORMADEACESSO
_METADADOS.fields_by_name['extensao'].enum_type = _METADADOS_EXTENSAO
_METADADOS.fields_by_name['receita_base'].enum_type = _METADADOS_OPCOESDETALHAMENTO
_METADADOS.fields_by_name['outras_receitas'].enum_type = _METADADOS_OPCOESDETALHAMENTO
_METADADOS.fields_by_name['despesas'].enum_type = _METADADOS_OPCOESDETALHAMENTO
_METADADOS_FORMADEACESSO.containing_type = _METADADOS
_METADADOS_EXTENSAO.containing_type = _METADADOS
_METADADOS_OPCOESDETALHAMENTO.containing_type = _METADADOS
DESCRIPTOR.message_types_by_name['ResultadoColeta'] = _RESULTADOCOLETA
DESCRIPTOR.message_types_by_name['ProcInfo'] = _PROCINFO
DESCRIPTOR.message_types_by_name['Coleta'] = _COLETA
DESCRIPTOR.message_types_by_name['FolhaDePagamento'] = _FOLHADEPAGAMENTO
DESCRIPTOR.message_types_by_name['ContraCheque'] = _CONTRACHEQUE
DESCRIPTOR.message_types_by_name['Remuneracoes'] = _REMUNERACOES
DESCRIPTOR.message_types_by_name['Remuneracao'] = _REMUNERACAO
DESCRIPTOR.message_types_by_name['Metadados'] = _METADADOS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResultadoColeta = _reflection.GeneratedProtocolMessageType('ResultadoColeta', (_message.Message,), dict(
  DESCRIPTOR = _RESULTADOCOLETA,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ResultadoColeta)
  ))
_sym_db.RegisterMessage(ResultadoColeta)

ProcInfo = _reflection.GeneratedProtocolMessageType('ProcInfo', (_message.Message,), dict(
  DESCRIPTOR = _PROCINFO,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ProcInfo)
  ))
_sym_db.RegisterMessage(ProcInfo)

Coleta = _reflection.GeneratedProtocolMessageType('Coleta', (_message.Message,), dict(
  DESCRIPTOR = _COLETA,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Coleta)
  ))
_sym_db.RegisterMessage(Coleta)

FolhaDePagamento = _reflection.GeneratedProtocolMessageType('FolhaDePagamento', (_message.Message,), dict(
  DESCRIPTOR = _FOLHADEPAGAMENTO,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:FolhaDePagamento)
  ))
_sym_db.RegisterMessage(FolhaDePagamento)

ContraCheque = _reflection.GeneratedProtocolMessageType('ContraCheque', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACHEQUE,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:ContraCheque)
  ))
_sym_db.RegisterMessage(ContraCheque)

Remuneracoes = _reflection.GeneratedProtocolMessageType('Remuneracoes', (_message.Message,), dict(
  DESCRIPTOR = _REMUNERACOES,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Remuneracoes)
  ))
_sym_db.RegisterMessage(Remuneracoes)

Remuneracao = _reflection.GeneratedProtocolMessageType('Remuneracao', (_message.Message,), dict(
  DESCRIPTOR = _REMUNERACAO,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Remuneracao)
  ))
_sym_db.RegisterMessage(Remuneracao)

Metadados = _reflection.GeneratedProtocolMessageType('Metadados', (_message.Message,), dict(
  DESCRIPTOR = _METADADOS,
  __module__ = 'coleta_pb2'
  # @@protoc_insertion_point(class_scope:Metadados)
  ))
_sym_db.RegisterMessage(Metadados)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
