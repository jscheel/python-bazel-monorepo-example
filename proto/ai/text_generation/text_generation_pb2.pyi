from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClarificationRequest(_message.Message):
    __slots__ = ["requester_gid", "text"]
    REQUESTER_GID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    requester_gid: str
    text: str
    def __init__(self, text: _Optional[str] = ..., requester_gid: _Optional[str] = ...) -> None: ...

class MeteredTextResponse(_message.Message):
    __slots__ = ["text", "token_count"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    text: str
    token_count: int
    def __init__(self, text: _Optional[str] = ..., token_count: _Optional[int] = ...) -> None: ...

class ToneModificationRequest(_message.Message):
    __slots__ = ["requester_gid", "text", "tone"]
    class Tone(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CASUAL: ToneModificationRequest.Tone
    FORMAL: ToneModificationRequest.Tone
    REQUESTER_GID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: ToneModificationRequest.Tone
    requester_gid: str
    text: str
    tone: ToneModificationRequest.Tone
    def __init__(self, text: _Optional[str] = ..., tone: _Optional[_Union[ToneModificationRequest.Tone, str]] = ..., requester_gid: _Optional[str] = ...) -> None: ...
