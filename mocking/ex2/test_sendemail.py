import unittest
from unittest.mock import patch, Mock, ANY

import sendemail

class TestSendEmail(unittest.TestCase):

    @patch("smtplib.SMTP")
    def test_send_email(self, mock_smtp):
        instance = mock_smtp.return_value

        sendemail.send_email("smtp.example.com", 587, "mymail@example.com", "hismail@example.com", "Subject", "Mail Content")

        mock_smtp.assert_called_with("smtp.example.com", 587)

        instance.starttls.assert_called_with()
        instance.login.assert_called_with("mymail@example.com", "MyPassword")
        instance.sendmail.assert_called_with("mymail@example.com", "hismail@example.com", ANY)
        instance.quit.assert_called_with()

if __name__ == "__main__":
    unittest.main()
