import unittest
from unittest.mock import patch, MagicMock
from hello_operator import HelloOperator


class TestHelloOperator(unittest.TestCase):
    @patch("hello_operator.BaseHook")
    def test_execute_with_conn_id(self, mock_hook):
        mock_conn = MagicMock()
        mock_conn.conn_id = "test_conn"
        mock_hook.get_connection.return_value = mock_conn

        operator = HelloOperator(
            task_id="test_task", name="Test", conn_id="test_conn"
        )
        result = operator.execute(context={})

        self.assertEqual(result, "Hello Test")
        mock_hook.get_connection.assert_called_once_with("test_conn")

    def test_execute_without_conn_id(self):
        operator = HelloOperator(task_id="test_task", name="Test")
        result = operator.execute(context={})
        self.assertEqual(result, "Hello Test")


if __name__ == "__main__":
    unittest.main()
