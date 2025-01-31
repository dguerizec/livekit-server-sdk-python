import datetime

import jwt
import pytest

import livekit_server_sdk


def test_access_token():
    with pytest.raises(ValueError):
        grant = livekit_server_sdk.VideoGrant(room_join=True)
        _ = livekit_server_sdk.AccessToken("key", "secret", grant=grant, identity=None)


def test_access_token_jwt_with_identity():
    api_key = "key"
    api_secret = "secret"
    grant = livekit_server_sdk.VideoGrant()
    identity = "bob"
    name = "Bob"
    access_token = livekit_server_sdk.AccessToken(
        api_key, api_secret, grant=grant, name=name, identity=identity
    )
    token = access_token.to_jwt()
    decoded = jwt.decode(token, key=api_secret, algorithms=["HS256"])
    assert decoded["video"] == {}
    assert decoded["iss"] == api_key
    assert decoded["nbf"] < decoded["exp"]
    assert decoded["sub"] == identity
    assert decoded["name"] == name


def test_access_token_with_metadata():
    api_key = "key"
    api_secret = "secret"
    grant = livekit_server_sdk.VideoGrant()
    identity = "Bob"
    metadata = "bob is cool"
    access_token = livekit_server_sdk.AccessToken(
        api_key,
        api_secret,
        grant=grant,
        identity=identity,
        metadata=metadata,
    )
    token = access_token.to_jwt()
    decoded = jwt.decode(token, key=api_secret, algorithms=["HS256"])
    assert decoded["metadata"] == metadata


def test_access_token_invalid_ttl():
    grant = livekit_server_sdk.VideoGrant()
    with pytest.raises(ValueError):
        _ = livekit_server_sdk.AccessToken(
            "key",
            "secret",
            grant=grant,
            ttl=datetime.timedelta(seconds=0),
        )
