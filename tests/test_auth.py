from app.core.jwt import create_access_token, decode_access_token


def test_create_access_token():
    token = create_access_token(
        {
            "sub": "user@example.com",
            "role": "student",
        }
    )

    assert token is not None


def test_decode_access_token():
    token = create_access_token(
        {
            "sub": "user@example.com",
            "role": "student",
        }
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "user@example.com"
    assert payload["role"] == "student"
