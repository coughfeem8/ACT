import unittest

from view.shell import commands
class TestCommands(unittest.TestCase):
    '''testing shell.commands'''

    def test_command_list(self):
        self.assertIsNone(commands.list_command([]))

if __name__ == '__main__':
    unittest.main()