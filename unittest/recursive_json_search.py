from policy import POLICY

def json_search(key, input_object, role=None):
    """
    Search a key in a JSON object recursively.
    Enforce RBAC based on policy.py before returning matched items.
    """
    if key in POLICY:
        if role not in POLICY[key]:
            return []
            
    ret_val = []

    def inner_search(k, obj):
        if isinstance(obj, dict):
            for k_curr, v_curr in obj.items():
                if k_curr == k:
                    ret_val.append(v_curr)
                inner_search(k, v_curr)
        elif isinstance(obj, list):
            for item in obj:
                inner_search(k, item)

    inner_search(key, input_object)
    return ret_val
