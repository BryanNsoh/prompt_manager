"""
Prompt Manager: A flexible system for managing and processing prompt templates.

This module provides a PromptManager class that simplifies the process of loading,
managing, and formatting prompt templates for use with language models. It supports
loading prompts from files or direct text input, and allows for flexible variable 
insertion.

Classes:
--------
PromptManager
    Main class for managing prompts and their variables.

Functions:
----------
universal_file_opener(file_path: str) -> str
    A utility function to open and read text from various file types.

Example Usage:
--------------
    from prompt_manager import PromptManager

    # Initialize the PromptManager
    pm = PromptManager("path/to/prompts/folder")

    # Load a prompt from a file and insert variables
    prompt = pm.get_prompt("example_prompt", 
                           variable1="value1", 
                           variable2=pm.load_file("path/to/file.txt"))

    # Use a direct text prompt
    prompt = pm.get_prompt("This is a {{variable}} prompt", variable="test")

    # The resulting prompt is ready to be sent to an LLM
"""

import os
import json
import chardet

def universal_file_opener(file_path):
    """Open and read text from various file types, handling encoding issues."""
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
        detected = chardet.detect(raw_data)
        encoding = detected['encoding'] or 'utf-8'
        return raw_data.decode(encoding)
    except Exception as e:
        raise ValueError(f"Error reading file {file_path}: {str(e)}")

class PromptManager:
    def __init__(self, prompts_dir=None):
        self.prompts_dir = prompts_dir

    def load_file(self, file_path):
        """Load the content of a file given its path."""
        if self.prompts_dir:
            file_path = os.path.join(self.prompts_dir, file_path)
        return universal_file_opener(file_path)

    def _process_variable(self, value):
        """Process a variable, converting to string or loading file content if needed."""
        if isinstance(value, str) and os.path.isfile(value):
            return self.load_file(value)
        return str(value)

    def get_prompt(self, main_prompt, **kwargs):
        """
        Generate the final prompt by replacing placeholders in the template with variable values.
        
        :param main_prompt: Can be a filename, direct text, or a variable containing text
        :param kwargs: Variables to be inserted into the prompt
        :return: Formatted prompt string
        """
        if self.prompts_dir and os.path.isfile(os.path.join(self.prompts_dir, main_prompt)):
            template = self.load_file(main_prompt)
        elif os.path.isfile(main_prompt):
            template = self.load_file(main_prompt)
        else:
            template = main_prompt

        processed_kwargs = {k: self._process_variable(v) for k, v in kwargs.items()}

        try:
            return template.format(**{k: f"{{{{{k}}}}}" for k in processed_kwargs.keys()}).format(**processed_kwargs)
        except KeyError as e:
            missing_key = str(e).strip("'")
            raise ValueError(f"Missing argument for prompt: {missing_key}")
        except Exception as e:
            raise ValueError(f"Error formatting prompt: {str(e)}")

# Example usage
if __name__ == "__main__":
    pm = PromptManager("prompts")
    prompt = pm.get_prompt("example_template.txt", name="John", age=30)
    print(prompt)

    direct_prompt = pm.get_prompt("Hello, {{name}}!", name="Alice")
    print(direct_prompt)