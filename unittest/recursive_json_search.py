from test_data import *
from policy import POLICY

def json_search(key, input_object, role=None):
    # Kiểm tra phân quyền:
    # 1. Nếu key có trong POLICY:
    if key in POLICY:
        # Nếu role được chỉ định nhưng không nằm trong danh sách cho phép -> Chặn
        if role is not None and role not in POLICY[key]:
            return []
        # Nếu role không được chỉ định (role=None), chỉ cho phép nếu key đó cho phép tất cả các role (như issueSummary)
        # Các key nhạy cảm (như apiKey, managementIpAddress) bắt buộc phải có role hợp lệ
        if role is None and len(POLICY[key]) < 3:
            return []

    ret_val = []
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                temp = {k: v}
                ret_val.append(temp)
            if isinstance(v, dict):
                ret_val.extend(json_search(key, v, role=role))
            elif isinstance(v, list):
                for item in v:
                    if not isinstance(item, (str, int)):
                        ret_val.extend(json_search(key, item, role=role))
    else:
        for val in input_object:
            if not isinstance(val, (str, int)):
                ret_val.extend(json_search(key, val, role=role))
    return ret_val

if __name__ == '__main__':
    print(json_search("issueSummary", data))