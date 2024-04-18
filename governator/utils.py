import base64
import uuid


def generate_short_id(length=8):
    uuid_obj = uuid.uuid4()
    return (
        base64.urlsafe_b64encode(uuid_obj.bytes).rstrip(b"=").decode("utf-8")[:length]
    )
