import unittest
from recursive_json_search import json_search
from test_data import data, key1, key2

class json_search_test(unittest.TestCase):
    
    def test_search_found(self):
        """Test searching for a key that exists in the data."""
        res = json_search(key1, data, role="admin")
        self.assertTrue(len(res) > 0)
        self.assertEqual(res[0], "Network Device 10.10.20.82 Is Unreachable From Controller")
        
    def test_search_not_found(self):
        """Test searching for a key that does not exist in the data."""
        res = json_search(key2, data, role="admin")
        self.assertEqual(res, [])
        
    def test_is_a_list(self):
        """Test that the result returned is a list."""
        res = json_search(key1, data, role="admin")
        self.assertIsInstance(res, list)

    def test_rbac_apiKey_admin(self):
        """Test security policy: apiKey can be accessed by admin."""
        res = json_search("apiKey", data, role="admin")
        self.assertEqual(res, ["SNMP-COMMUNITY-STRING-7f3a9c"])

    def test_rbac_apiKey_viewer(self):
        """Test security policy: apiKey cannot be accessed by viewer."""
        res = json_search("apiKey", data, role="viewer")
        self.assertEqual(res, [])

    def test_rbac_managementIpAddress_operator(self):
        """Test security policy: managementIpAddress can be accessed by operator."""
        res = json_search("managementIpAddress", data, role="operator")
        self.assertEqual(res, ["10.10.20.21"])

    def test_rbac_managementIpAddress_viewer(self):
        """Test security policy: managementIpAddress cannot be accessed by viewer."""
        res = json_search("managementIpAddress", data, role="viewer")
        self.assertEqual(res, [])

if __name__ == '__main__':
    unittest.main()
