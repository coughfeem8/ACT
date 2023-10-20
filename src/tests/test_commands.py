import unittest

from view.shell import commands
class TestCommands(unittest.TestCase):
    '''testing shell.commands'''

    @classmethod
    def setUpClass(self) -> None:
        print('preparing Shell command test')

    @classmethod
    def tearDownClass(self) -> None:
        print('cleaning Shell command test')
        


#list command
    def test_list_all_series(self):
        self.assertIsNone(commands.list_command([]))

    def test_list_single_amiibo(self):
        self.assertIsNone(commands.list_command(['amiibo','0x1996']))

    def test_list_amiibos_single_series(self):
         self.assertIsNone(commands.list_command(['series','0x010']))
    
    def test_amiibo_not_found(self):
        self.assertIsNone(commands.list_command(['amiibo','0x1sdd']))
    
#download 
    def test_download_command(self):
        """this test check that if you select the command download and store metadata"""
        self.assertIsNone(commands.download_command([]))

#create
    def test_create_command(self):
        """create a an amiibo card from a previously stored metadata"""
        self.assertIsNone(commands.create_command([]))


if __name__ == '__main__':
    unittest.main()