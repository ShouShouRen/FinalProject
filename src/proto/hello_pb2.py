# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hello.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'hello.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bhello.proto\")\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61ge\x18\x02 \x01(\x05\"!\n\x0eStringResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\"\n\x0c\x46ileResponse\x12\x12\n\nchunk_data\x18\x01 \x01(\x0c\"/\n\x08MetaData\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x11\n\textension\x18\x02 \x01(\t\"S\n\x11UploadFileRequest\x12\x1d\n\x08metadata\x18\x01 \x01(\x0b\x32\t.MetaDataH\x00\x12\x14\n\nchunk_data\x18\x02 \x01(\x0cH\x00\x42\t\n\x07request2\x9c\x01\n\x07Greeter\x12,\n\x08SayHello\x12\r.HelloRequest\x1a\x0f.StringResponse\"\x00\x12\x35\n\nUploadFile\x12\x12.UploadFileRequest\x1a\x0f.StringResponse\"\x00(\x01\x12,\n\x0c\x44ownloadFile\x12\t.MetaData\x1a\r.FileResponse\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HELLOREQUEST']._serialized_start=15
  _globals['_HELLOREQUEST']._serialized_end=56
  _globals['_STRINGRESPONSE']._serialized_start=58
  _globals['_STRINGRESPONSE']._serialized_end=91
  _globals['_FILERESPONSE']._serialized_start=93
  _globals['_FILERESPONSE']._serialized_end=127
  _globals['_METADATA']._serialized_start=129
  _globals['_METADATA']._serialized_end=176
  _globals['_UPLOADFILEREQUEST']._serialized_start=178
  _globals['_UPLOADFILEREQUEST']._serialized_end=261
  _globals['_GREETER']._serialized_start=264
  _globals['_GREETER']._serialized_end=420
# @@protoc_insertion_point(module_scope)
