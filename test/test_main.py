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


if __name__ == '__main__':
    test_main()
