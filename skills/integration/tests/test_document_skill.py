import unittest
from unittest.mock import MagicMock, patch
from skills.integration.document_skill import DocumentSkill
from langchain_core.documents import Document

class TestDocumentSkill(unittest.TestCase):
    def setUp(self):
        self.skill = DocumentSkill()

    def test_split_text(self):
        text = "Hello world. " * 100 # Long text
        chunks = self.skill.get_text_chunks(text)
        self.assertTrue(len(chunks) > 1)
        self.assertIn("Hello world.", chunks[0])

    @patch('skills.integration.document_skill.PyPDFLoader')
    def test_load_pdf_mock(self, mock_loader):
        # Mocking PDF loader because we might not have a real PDF in the environment
        mock_instance = mock_loader.return_value
        mock_instance.load.return_value = [Document(page_content="PDF Content", metadata={"source": "test.pdf"})]
        
        with patch('os.path.exists', return_value=True):
            docs = self.skill.load_pdf("fake.pdf")
            self.assertEqual(len(docs), 1)
            self.assertEqual(docs[0].page_content, "PDF Content")

    @patch('skills.integration.document_skill.WebBaseLoader')
    def test_load_url_mock(self, mock_loader):
        mock_instance = mock_loader.return_value
        mock_instance.load.return_value = [Document(page_content="Web Content", metadata={"source": "http://test.com"})]
        
        docs = self.skill.load_url("http://test.com")
        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0].page_content, "Web Content")

if __name__ == '__main__':
    unittest.main()
