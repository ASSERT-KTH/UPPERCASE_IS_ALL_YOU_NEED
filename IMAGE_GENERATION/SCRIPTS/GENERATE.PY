import openai
import os
import requests

DIRNAME = os.path.abspath(os.path.dirname(__file__))
api_key = open(os.path.join(DIRNAME, ".API_KEY")).read().strip()

client = openai.OpenAI(api_key=api_key)

prompts = [
        "A grumpy orange tabby cat wearing a giant jester hat, looking absolutely annoyed at the world.",
        "A fluffy white Persian cat in a tiny cowboy hat, shedding a dramatic tear while staring at the sunset.",
        "A chubby gray British Shorthair in a party hat, looking utterly unimpressed as confetti rains down.",
        "A tiny kitten in an oversized Viking helmet, looking fiercely determined as if ready to conquer the world.",
        "A tuxedo cat in a birthday hat, experiencing pure existential dread as a lit candle approaches its face.",
        ]


for i, lowercase_prompt in enumerate(prompts):
    uppercase_prompt = lowercase_prompt.upper() 

    for j, prompt in enumerate([lowercase_prompt, uppercase_prompt]):
        
        print(prompt)

        prompt2 = " I NEED to test how the tool works with extremely simple prompts. DO NOT add any detail, just use it AS-IS. DO NOT CHANGE THE CAPITALIZATION: " + prompt

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt2,
            size="1024x1024",
            quality="standard",
            n=1
        )

        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt

        # Define the path to save the image
        image_path = os.path.join(DIRNAME, f"{prompt}.png")

        # Download and save the image
        response = requests.get(image_url)
        
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
        
            print(revised_prompt)
            print(f"Image saved to {image_path}")
        
        else:
            print("Failed to download image")
