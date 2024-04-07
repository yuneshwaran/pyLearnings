import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_response(prompt, max_length=100):
    # Tokenize input text and generate response
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
    output = model.generate(input_ids, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    print("Welcome to Advanced ChatBot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye!")
            break
        response = generate_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
