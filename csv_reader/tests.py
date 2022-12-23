from django.test import TestCase

# Create your tests here.


class TestReadCSV(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_read_csv(self):
        response = self.client.get('/read_csv/')
        
        file = 'spacex_launch_data.csv'
        
        # test case to check whether file exists or not
        self.assertTrue(open(file, 'r' , encoding='UTF-8'))

        # test case to check the file is csv
        file_ext = file.split('.')[-1]
        self.assertEqual(file_ext , 'csv')
        
        # test case to check the response code
        self.assertEqual(response.status_code, 200)
        
        # test case to check the desired template rendered or not
        self.assertTemplateUsed(response , 'datatable.html')

        # test case to check the desired context provided to the template : 'headers' and 'data
        self.assertTrue('headers' in response.context)
        self.assertTrue('data' in response.context)
