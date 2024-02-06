#!/usr/bin/python3
""" To JSON string """


def to_json_string(my_obj):
    """
    Returns the JSON representation of an obj(str)

    Args:
        my_obj: object to be converted to JSON

    Returns:
        Json representation of obj(str)
    """
    import json
    if isinstance(my_obj, dict):
        return (json.dumps(
               {key: my_obj[key] for key in sorted(my_obj)},
               sort_keys=True)
        )
    else:
        return (json.dumps(my_obj))
