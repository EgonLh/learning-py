import unittest
from  collectionData import CollectData

class TestCollectData(unittest.TestCase):
    """Test for the class which collect data"""
    def setUp(self):
        """SEt up method for setting up class for the test cases"""
        question = "What is your hobby?";
        self.data_collection = CollectData(question);
        self.responses = ['Reading','Writing','Running']

    def test_store_single_response(self):
        """Test that a single response is stored property"""
        self.data_collection.store_response(self.responses[0]);
        self.assertIn(self.responses[0],self.data_collection.responses)
    def test_store_many_responses(self):
        """Test that a single response is stored property"""
        self.data_collection.store_response(self.responses);
        self.assertIn(self.responses,self.data_collection.responses)  
unittest.main()