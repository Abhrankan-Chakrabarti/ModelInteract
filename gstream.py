def stream(input, model):
    """Evaluate the input using the genai model"""
    completion = model.generate_content(
    input,
    stream=True,
    )
    for chunk in completion:
        yield chunk.text