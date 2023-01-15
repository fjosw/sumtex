import openai


def openai_request(question, text, temperature):
    try:
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=f"""{question}:\n\n{text}""",
                                            temperature=temperature,
                                            max_tokens=256,
                                            top_p=1.0,
                                            frequency_penalty=0.2,
                                            presence_penalty=0.0)
    except openai.error.RateLimitError:
        raise Exception("openai rate limit reached. Try again in a minute or so.")
    except openai.error.InvalidRequestError:
        return "Paragraph too long, try splitting it up."

    return response["choices"][0]["text"].strip()
