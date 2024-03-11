import openai

openai.api_key = "ENTER-YOUR_OPENAI_KEY_HERE"

company_name = input("Enter the company name: ")
company_description = input("Enter a brief description of the company: ")

prompt = f"""**Attention:**

**Write a short captivating introduction about {company_name} that grabs the reader's attention.**

**Interest:**

**Briefly summarize {company_description}, highlighting what makes them stand out.**

**Desire:**

**Explain how {company_name} helps customers overcome a challenge like [mention a relevant problem]. Describe the benefits of using their products or services.**

**Action:**

**Conclude with a clear call to action, encouraging the reader to visit {company_name}'s website or contact them.**
"""


response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=350  
)


print(response.choices[0].text)
