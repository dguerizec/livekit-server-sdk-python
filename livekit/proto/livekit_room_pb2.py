# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: livekit_room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import livekit_egress_pb2 as livekit__egress__pb2
from . import livekit_models_pb2 as livekit__models__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x12livekit_room.proto\x12\x07livekit\x1a\x14livekit_models.proto\x1a\x14livekit_egress.proto"\x9a\x01\n\x11\x43reateRoomRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rempty_timeout\x18\x02 \x01(\r\x12\x18\n\x10max_participants\x18\x03 \x01(\r\x12\x0f\n\x07node_id\x18\x04 \x01(\t\x12\x10\n\x08metadata\x18\x05 \x01(\t\x12#\n\x06\x65gress\x18\x06 \x01(\x0b\x32\x13.livekit.RoomEgress"i\n\nRoomEgress\x12\x31\n\x04room\x18\x01 \x01(\x0b\x32#.livekit.RoomCompositeEgressRequest\x12(\n\x06tracks\x18\x02 \x01(\x0b\x32\x18.livekit.AutoTrackEgress"!\n\x10ListRoomsRequest\x12\r\n\x05names\x18\x01 \x03(\t"1\n\x11ListRoomsResponse\x12\x1c\n\x05rooms\x18\x01 \x03(\x0b\x32\r.livekit.Room"!\n\x11\x44\x65leteRoomRequest\x12\x0c\n\x04room\x18\x01 \x01(\t"\x14\n\x12\x44\x65leteRoomResponse"\'\n\x17ListParticipantsRequest\x12\x0c\n\x04room\x18\x01 \x01(\t"J\n\x18ListParticipantsResponse\x12.\n\x0cparticipants\x18\x01 \x03(\x0b\x32\x18.livekit.ParticipantInfo"9\n\x17RoomParticipantIdentity\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t"\x1b\n\x19RemoveParticipantResponse"X\n\x14MuteRoomTrackRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x11\n\ttrack_sid\x18\x03 \x01(\t\x12\r\n\x05muted\x18\x04 \x01(\x08":\n\x15MuteRoomTrackResponse\x12!\n\x05track\x18\x01 \x01(\x0b\x32\x12.livekit.TrackInfo"\x8e\x01\n\x18UpdateParticipantRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12\x32\n\npermission\x18\x04 \x01(\x0b\x32\x1e.livekit.ParticipantPermission\x12\x0c\n\x04name\x18\x05 \x01(\t"\x9b\x01\n\x1aUpdateSubscriptionsRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08identity\x18\x02 \x01(\t\x12\x12\n\ntrack_sids\x18\x03 \x03(\t\x12\x11\n\tsubscribe\x18\x04 \x01(\x08\x12\x36\n\x12participant_tracks\x18\x05 \x03(\x0b\x32\x1a.livekit.ParticipantTracks"\x1d\n\x1bUpdateSubscriptionsResponse"o\n\x0fSendDataRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12&\n\x04kind\x18\x03 \x01(\x0e\x32\x18.livekit.DataPacket.Kind\x12\x18\n\x10\x64\x65stination_sids\x18\x04 \x03(\t"\x12\n\x10SendDataResponse";\n\x19UpdateRoomMetadataRequest\x12\x0c\n\x04room\x18\x01 \x01(\t\x12\x10\n\x08metadata\x18\x02 \x01(\t2\xe6\x06\n\x0bRoomService\x12\x37\n\nCreateRoom\x12\x1a.livekit.CreateRoomRequest\x1a\r.livekit.Room\x12\x42\n\tListRooms\x12\x19.livekit.ListRoomsRequest\x1a\x1a.livekit.ListRoomsResponse\x12\x45\n\nDeleteRoom\x12\x1a.livekit.DeleteRoomRequest\x1a\x1b.livekit.DeleteRoomResponse\x12W\n\x10ListParticipants\x12 .livekit.ListParticipantsRequest\x1a!.livekit.ListParticipantsResponse\x12L\n\x0eGetParticipant\x12 .livekit.RoomParticipantIdentity\x1a\x18.livekit.ParticipantInfo\x12Y\n\x11RemoveParticipant\x12 .livekit.RoomParticipantIdentity\x1a".livekit.RemoveParticipantResponse\x12S\n\x12MutePublishedTrack\x12\x1d.livekit.MuteRoomTrackRequest\x1a\x1e.livekit.MuteRoomTrackResponse\x12P\n\x11UpdateParticipant\x12!.livekit.UpdateParticipantRequest\x1a\x18.livekit.ParticipantInfo\x12`\n\x13UpdateSubscriptions\x12#.livekit.UpdateSubscriptionsRequest\x1a$.livekit.UpdateSubscriptionsResponse\x12?\n\x08SendData\x12\x18.livekit.SendDataRequest\x1a\x19.livekit.SendDataResponse\x12G\n\x12UpdateRoomMetadata\x12".livekit.UpdateRoomMetadataRequest\x1a\r.livekit.RoomBFZ#github.com/livekit/protocol/livekit\xaa\x02\rLiveKit.Proto\xea\x02\x0eLiveKit::Protob\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "livekit_room_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z#github.com/livekit/protocol/livekit\252\002\rLiveKit.Proto\352\002\016LiveKit::Proto"
    _CREATEROOMREQUEST._serialized_start = 76
    _CREATEROOMREQUEST._serialized_end = 230
    _ROOMEGRESS._serialized_start = 232
    _ROOMEGRESS._serialized_end = 337
    _LISTROOMSREQUEST._serialized_start = 339
    _LISTROOMSREQUEST._serialized_end = 372
    _LISTROOMSRESPONSE._serialized_start = 374
    _LISTROOMSRESPONSE._serialized_end = 423
    _DELETEROOMREQUEST._serialized_start = 425
    _DELETEROOMREQUEST._serialized_end = 458
    _DELETEROOMRESPONSE._serialized_start = 460
    _DELETEROOMRESPONSE._serialized_end = 480
    _LISTPARTICIPANTSREQUEST._serialized_start = 482
    _LISTPARTICIPANTSREQUEST._serialized_end = 521
    _LISTPARTICIPANTSRESPONSE._serialized_start = 523
    _LISTPARTICIPANTSRESPONSE._serialized_end = 597
    _ROOMPARTICIPANTIDENTITY._serialized_start = 599
    _ROOMPARTICIPANTIDENTITY._serialized_end = 656
    _REMOVEPARTICIPANTRESPONSE._serialized_start = 658
    _REMOVEPARTICIPANTRESPONSE._serialized_end = 685
    _MUTEROOMTRACKREQUEST._serialized_start = 687
    _MUTEROOMTRACKREQUEST._serialized_end = 775
    _MUTEROOMTRACKRESPONSE._serialized_start = 777
    _MUTEROOMTRACKRESPONSE._serialized_end = 835
    _UPDATEPARTICIPANTREQUEST._serialized_start = 838
    _UPDATEPARTICIPANTREQUEST._serialized_end = 980
    _UPDATESUBSCRIPTIONSREQUEST._serialized_start = 983
    _UPDATESUBSCRIPTIONSREQUEST._serialized_end = 1138
    _UPDATESUBSCRIPTIONSRESPONSE._serialized_start = 1140
    _UPDATESUBSCRIPTIONSRESPONSE._serialized_end = 1169
    _SENDDATAREQUEST._serialized_start = 1171
    _SENDDATAREQUEST._serialized_end = 1282
    _SENDDATARESPONSE._serialized_start = 1284
    _SENDDATARESPONSE._serialized_end = 1302
    _UPDATEROOMMETADATAREQUEST._serialized_start = 1304
    _UPDATEROOMMETADATAREQUEST._serialized_end = 1363
    _ROOMSERVICE._serialized_start = 1366
    _ROOMSERVICE._serialized_end = 2236
# @@protoc_insertion_point(module_scope)
