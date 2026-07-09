# Business Name Generator

This Python script is a lightweight, command-line tool designed to help entrepreneurs and creators brainstorm business names based on a core keyword.

## Features

- **Customizable**: Uses a list of professional adjectives and corporate suffixes to build names.
- **Varied Structure**: Generates three different types of names:
  - Adjective + Keyword + Suffix (e.g., "Apex Data Solutions")
  - Keyword + Suffix (e.g., "Data Systems")
  - Adjective + Keyword (e.g., "Quantum Data")
- **Duplicate Protection**: Uses a `set` data structure to ensure unique results.
- **User-Friendly**: Allows users to specify the number of name ideas generated.

## Requirements

- Python 3.x

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the directory containing `name_generator.py`.
3. Run the following command:

```bash
python name_generator.py
```

4. Follow the prompts:
   - Enter your core keyword.
   - Enter the number of suggestions you'd like to generate.

## Example Output

```text
========================================
🚀 AI-Assisted Business Name Generator
========================================

Enter your core business keyword (e.g., 'Data', 'Bistro', 'Logistics'): Tech
How many ideas do you need? (Default is 5): 3

Generating...

----------------------------------------
1. Luminous Tech
2. Nexus Tech Solutions
3. Tech Dynamics
----------------------------------------
```

## Customizing the Generator

You can modify the vocabulary used by the generator by editing the `adjectives` and `suffixes` lists directly within the `name_generator.py` file:

```python
# Example snippet to modify
adjectives = ['Apex', 'Vanguard', 'Quantum', 'YourNewWord', ...]
suffixes = ['Solutions', 'Labs', 'YourNewSuffix', ...]
```

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.