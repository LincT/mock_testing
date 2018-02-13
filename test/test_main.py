from unittest import main as test_main, TestCase
from unittest.mock import patch
from main import main


class TestMain(TestCase):
    @patch('main.main.random_num', return_value=10)
    @patch('builtins.print')
    def test_main(self, mock_print, mock_random):
        main.main()
        print_calls = mock_print.call_args_list
        self.assertIn('win', str(print_calls))

    @patch('main.main.random_num', return_value=10)
    @patch('builtins.print')
    def test_mock_print_count(self, mock_print, mock_random):
        main.main()
        self.assertEqual(2,mock_print.call_count)

    @patch('main.main.random_num', return_value=10)
    @patch('builtins.print')
    def test_mock_print_contains(self, mock_print, mock_random):
        main.main()
        mock_print.assert_called_with('win')

    # tried adding this from what was described, may need to return to this
    @patch('builtins.input',return_value="some text")
    def test_print(self, mock_input):
        self.assertEqual(mock_input, "some_text")


if __name__ == '__main__':
    test_main()
