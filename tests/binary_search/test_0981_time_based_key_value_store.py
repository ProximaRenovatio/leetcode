from solutions.binary_search.medium._0981_time_based_key_value_store import TimeMap

def test_time_based_key_value_store():
    time_map = TimeMap()

    time_map.set("foo", "bar", 1)
    assert time_map.get("foo", 1) == "bar"
    assert time_map.get("foo", 3) == "bar"

    time_map.set("foo", "bar2", 4)
    assert time_map.get("foo", 4) == "bar2"
    assert time_map.get("foo", 5) == "bar2"
