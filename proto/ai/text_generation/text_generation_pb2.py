# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ai/text_generation/text_generation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.proto/ai/text_generation/text_generation.proto\x12\x1cproto.rpc.ai.text_generation\"\xb5\x01\n\x17ToneModificationRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12H\n\x04tone\x18\x02 \x01(\x0e\x32:.proto.rpc.ai.text_generation.ToneModificationRequest.Tone\x12\x15\n\rrequester_gid\x18\x03 \x01(\t\"+\n\x04Tone\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x46ORMAL\x10\x01\x12\n\n\x06\x43\x41SUAL\x10\x02\";\n\x14\x43larificationRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x15\n\rrequester_gid\x18\x03 \x01(\t\"8\n\x13MeteredTextResponse\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x13\n\x0btoken_count\x18\x02 \x01(\x05\x32\xfc\x01\n\x0bTextRefiner\x12y\n\x0bmodify_tone\x12\x35.proto.rpc.ai.text_generation.ToneModificationRequest\x1a\x31.proto.rpc.ai.text_generation.MeteredTextResponse\"\x00\x12r\n\x07\x63larify\x12\x32.proto.rpc.ai.text_generation.ClarificationRequest\x1a\x31.proto.rpc.ai.text_generation.MeteredTextResponse\"\x00\x42\x1c\xea\x02\x19Proto::AI::TextGenerationb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.ai.text_generation.text_generation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\352\002\031Proto::AI::TextGeneration'
  _TONEMODIFICATIONREQUEST._serialized_start=81
  _TONEMODIFICATIONREQUEST._serialized_end=262
  _TONEMODIFICATIONREQUEST_TONE._serialized_start=219
  _TONEMODIFICATIONREQUEST_TONE._serialized_end=262
  _CLARIFICATIONREQUEST._serialized_start=264
  _CLARIFICATIONREQUEST._serialized_end=323
  _METEREDTEXTRESPONSE._serialized_start=325
  _METEREDTEXTRESPONSE._serialized_end=381
  _TEXTREFINER._serialized_start=384
  _TEXTREFINER._serialized_end=636
# @@protoc_insertion_point(module_scope)
