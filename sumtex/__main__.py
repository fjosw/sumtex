import sys
from . import latex
from . import requests

if __name__ == '__main__':
    sections = latex.process_latex_file(sys.argv[1])

    my_prompts = [{"context": "",
                   "prompt": "Give the main topic of the following text, the three most important points and the audience",
                   "temperature": 0.0},
                  {"context": "Suggested title:",
                   "prompt": "What title would you give to the following text?",
                   "temperature": 0.0},
                  {"context": "Catchy title:",
                   "prompt": "Give a sensationalist title for the following text",
                   "temperature": 0.8},
                  {"context": "Understandability rating out of 10:",
                   "prompt": "How understandable is the following text for a domain expert on a a scale from 0 to 10? Just return a number.",
                   "temperature": 0.0}]

    for sec_name, sec_text in sections.items():
        sec_name_string = f"Section: {sec_name}"
        print(sec_name_string)
        print("-" * len(sec_name_string))
        for prompt in my_prompts:
            print(f"{prompt['context']}")
            print(requests.openai_request(prompt["prompt"], sec_text, prompt["temperature"]), "\n")
