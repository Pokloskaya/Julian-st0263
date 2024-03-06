from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ("peerName", "puertoPservidor", "fileName")
    PEERNAME_FIELD_NUMBER: _ClassVar[int]
    PUERTOPSERVIDOR_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    peerName: str
    puertoPservidor: str
    fileName: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, peerName: _Optional[str] = ..., puertoPservidor: _Optional[str] = ..., fileName: _Optional[_Iterable[str]] = ...) -> None: ...

class OperationResponse(_message.Message):
    __slots__ = ("serverResponse",)
    SERVERRESPONSE_FIELD_NUMBER: _ClassVar[int]
    serverResponse: str
    def __init__(self, serverResponse: _Optional[str] = ...) -> None: ...
