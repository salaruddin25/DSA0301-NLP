
# gpt3_text_generator.py

import openai

# Step 1: Set your OpenAI API key


# Step 2: Define a function to generate text from a prompt
def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=100):
    try:
        # Step 3: Use the ChatCompletion API (for newer models)
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7
        )
        # Step 4: Extract and return the generated text
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Step 5: Take user input and generate output
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    generated = generate_text(user_prompt)
    print("\nGenerated Text:\n", generated)