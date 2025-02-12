import unittest

from name_function import get_formatted_name;

class NamesTestCase(unittest.TestCase):
    """Test for the `name_function.py`"""
    
    def test_first_last_name(self):
        """Do Names like Janis Joplin work"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    
    def test_first_middle_last_name(self):
        """Do Names with middle work?"""
        formatted_name = get_formatted_name('jeason','jophin','john')
        self.assertEqual(formatted_name,"Jeason John Jophin")
unittest.main()