import userdata
import unittest
from unittest.mock import patch, Mock

class TestUserData(unittest.TestCase):

    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dict = {"name": "John", "email": "john@example.com"}
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        user_data = userdata.get_user_data(1)
        mock_get.assert_called_with("https://api.example.com/users/1")
        self.assertEqual(user_data, response_dict)

if __name__ == "__main__":
    unittest.main()
