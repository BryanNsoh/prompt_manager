import unittest
from llm_prompt_manager.core import PromptManager

class TestPromptManager(unittest.TestCase):

    def setUp(self):
        self.pm = PromptManager("tests/prompts")

    def test_load_file(self):
        content = self.pm.load_file("test_template.txt")
        self.assertIn("Hello, {{name}}!", content)

    def test_get_prompt_with_file_template(self):
        prompt = self.pm.get_prompt("test_template.txt", name="John")
        self.assertIn("Hello, John!", prompt)

    def test_get_prompt_with_direct_text(self):
        prompt = self.pm.get_prompt("Hello, {{name}}!", name="Alice")
        self.assertEqual(prompt, "Hello, Alice!")

    def test_get_prompt_with_file_variable(self):
        prompt = self.pm.get_prompt("Main template with {{sub_template}}", sub_template=self.pm.load_file("sub_template.txt"))
        self.assertIn("Main template with This is a sub template.", prompt)

if __name__ == '__main__':
    unittest.main()
