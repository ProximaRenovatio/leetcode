from solutions.arrays_hashing.medium._0271_encode_and_decode_strings import Codec

def test_encode_and_decode_strings():
    codec = Codec()

    values = ["lint", "code", "love", "you"]
    assert codec.decode(codec.encode(values)) == values

    values = ["we", "say", ":", "yes"]
    assert codec.decode(codec.encode(values)) == values

    values = [""]
    assert codec.decode(codec.encode(values)) == values
