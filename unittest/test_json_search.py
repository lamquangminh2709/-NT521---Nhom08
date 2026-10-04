import unittest
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    '''test module to test search function in recursive_json_search.py'''

    # --- 3 Unit test chức năng ban đầu ---
    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

    # --- Tối thiểu 3 Security test cases theo Yêu cầu 5 ---
    def test_wrong_role_cannot_read_secret(self):
        '''role khong co quyen khong duoc phep doc apiKey'''
        result = json_search("apiKey", data, role="viewer")
        self.assertEqual([], result)

    def test_admin_can_read_secret(self):
        '''admin duoc phep doc apiKey'''
        result = json_search("apiKey", data, role="admin")
        self.assertTrue([] != result)

    def test_viewer_cannot_read_management_ip(self):
        '''viewer khong duoc phep doc managementIpAddress'''
        result = json_search("managementIpAddress", data, role="viewer")
        self.assertEqual([], result)

if __name__ == '__main__':
    unittest.main()