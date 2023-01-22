import sys
from . import latex
from . import requests


def main():
    if len(sys.argv) != 2:
        raise Exception("Please provide a latex file as argument to sumtex.")

    sections = latex.process_latex_file(sys.argv[1])

    my_prompts = [{"context": "",
                   "prompt": "Give the main topic of the following text, the three most important points and the audience.",
                   "temperature": 0.1},
                  {"context": "Title suggestions:",
                   "prompt": "Generate an objective title and a catchy title for the following text.",
                   "temperature": 0.3}]  # Add additional prompts here.

    for sec_name, sec_text in sections.items():
        sec_name_string = f"Section: {sec_name}"
        print(sec_name_string)
        print("-" * len(sec_name_string))
        for prompt in my_prompts:
            print(f"{prompt['context']}")
            print(requests.openai_request(prompt["prompt"], sec_text, prompt["temperature"]), "\n")


if __name__ == '__main__':
    main()
