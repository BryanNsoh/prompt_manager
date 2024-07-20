# Prompt Manager

Prompt Manager is a flexible system for managing and processing prompt templates for use with language models. It simplifies the process of loading, managing, and formatting prompts, allowing you to focus on developing your AI applications.

## Features

- Load prompts from text files or direct text input
- Insert variables into prompts using double braces `{{variable}}`
- Handle various file types and encoding issues with a universal file opener
- Flexible API for ease of use

## Installation

Install the package using pip:

```sh
pip install prompt_manager
```

## Usage

### Basic Usage

To load and process a template named `example_template` with no dependencies:

```python
from prompt_manager import PromptManager

# Initialize the PromptManager with the path to the prompts folder
pm = PromptManager("path/to/prompts/folder")

# Load a prompt template and insert variables
prompt = pm.get_prompt("example_template.txt", name="John Doe", age=30)
print(prompt)
```

### Using Direct Text Prompts

To use a direct text prompt and replace placeholders with direct values:

```python
from prompt_manager import PromptManager

pm = PromptManager()

# Use a direct text prompt
prompt = pm.get_prompt("Hello, {{name}}!", name="Alice")
print(prompt)
```

### Loading File Content as Variables

To load and process a template and replace placeholders with the content of other files:

```python
from prompt_manager import PromptManager

pm = PromptManager("path/to/prompts/folder")

# Load a prompt template and insert file content as variables
prompt = pm.get_prompt("example_template.txt", variable1=pm.load_file("sub_template1.txt"), variable2=pm.load_file("sub_template2.txt"))
print(prompt)
```

## Exception Handling

- Raises `FileNotFoundError` if the template file does not exist.
- Raises `ValueError` if required placeholders are not provided or if there are issues with file dependencies.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improvements, feel free to submit a pull request or open an issue.

## Contact

Author: Bryan Anye  
Email: bryan.anye.5@gmail.com  
GitHub: [BryanNsoh](https://github.com/BryanNsoh)