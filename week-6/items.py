# Import necessary libraries and modules
from ast import If
import re
from typing import Optional
from transformers import AutoTokenizer

# Define constants for token limits and model
BASE_MODEL = "meta-llama/Meta-Llama-3.1-8B"

MIN_TOKENS = 150 # Any less than this, and we don't have enough useful content
MAX_TOKENS = 160 # Truncate after this many tokens. Then after adding in prompt text, we will get to around 180 tokens

MIN_CHARS = 300
CEILING_CHARS = MAX_TOKENS * 7

# Define the Item class - responsible for cleaning, curating, pricing and preparing product data
class Item:
    """
    An Item is a cleaned, curated datapoint of a Product with a Price
    
    **What the code does?**
    
    - Defines an Item class for representing a product with a price, title, category, and details.
    - Cleans and curates product data for use in machine learning, especially for price prediction tasks.
    - Uses a tokenizer from Hugging Face Transformers (AutoTokenizer) to process and count tokens for each product text.
    - Scrubs irrelevant details from product descriptions and features, removing unnecessary text and product numbers.
    - Prepares prompts for training or testing a model to estimate product prices.

    **Key functions and logic:**

    - **Initialization (__init__)**: Takes product data and price, sets up the item, and parses the data.
    - **scrub_details** and **scrub**: Remove unwanted text and clean up the product information.
    - **parse**: Combines product description, features, and details, cleans them, and checks if the resulting text is long enough and within token limits. If so, it creates a prompt for training.
    - **make_prompt**: Builds a prompt string for training, including the question and the cleaned product info, and appends the price.
    - **test_prompt**: Returns a prompt for testing, with the actual price removed.
    - **__repr__**: Returns a string representation of the item.
    """
    
    # Initialize tokenizer with model - inside the Item class is executed when the Python interpreter first loads the class definition—that is, when the module containing this class is imported or run.
    # It is not executed each time you create an Item object; it runs once when the class is defined, and the resulting tokenizer is shared by all instances of the class.
    # If the tokenizer files for BASE_MODEL are not already present locally, they will be downloaded at that time.
    # This line creates a tokenizer object using Hugging Face’s Transformers library.
    # It loads the tokenizer for the model specified by BASE_MODEL (here, "meta-llama/Meta-Llama-3.1-8B").
    # If the tokenizer files are not already present locally, it will download them from Hugging Face.
    # The tokenizer is used to convert text into tokens for processing by the model.
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    PREFIX = "Price is $"
    QUESTION = "How much does this cost to the nearest dollar?"
    REMOVALS = ['"Batteries Included?": "No"', '"Batteries Included?": "Yes"', '"Batteries Required?": "No"', '"Batteries Required?": "Yes"', "By Manufacturer", "Item", "Date First", "Package", ":", "Number of", "Best Sellers", "Number", "Product "]

    # Define attributes for the Item class
    title: str
    price: float
    category: str
    token_count: int = 0
    details: Optional[str]
    prompt: Optional[str] = None
    include = False

    # Constructor - Initialize Item - it initializes product’s title and price, and then processes rest of product data.
    def __init__(self, data, price):
        self.title = data['title']
        self.price = price
        self.parse(data)

    # Remove unnecessary details from the product information that are defined in REMOVALS
    def scrub_details(self):
        """
        Clean up the details string by removing common text that doesn't add value
        """
        details = self.details
        for remove in self.REMOVALS:
            details = details.replace(remove, "")
        return details

    def scrub(self, stuff):
        """
        Clean up the provided text by removing unnecessary characters and whitespace
        Also remove words that are 7+ chars and contain numbers, as these are likely irrelevant product numbers
        """
        stuff = re.sub(r'[:\[\]"{}【】\s]+', ' ', stuff).strip()
        stuff = stuff.replace(" ,", ",").replace(",,,",",").replace(",,",",")
        words = stuff.split(' ')
        select = [word for word in words if len(word)<7 or not any(char.isdigit() for char in word)]
        return " ".join(select)
    
    def parse(self, data):
        """
        Parse this data point and if it fits within the allowed Token range, then set include to True
        """
        contents = '\n'.join(data['description'])
        if contents:
            contents += '\n'
        features = '\n'.join(data['features'])
        if features:
            contents += features + '\n'
        self.details = data['details']
        if self.details:
            contents += self.scrub_details() + '\n'
        if len(contents) > MIN_CHARS:
            contents = contents[:CEILING_CHARS]
            text = f"{self.scrub(self.title)}\n{self.scrub(contents)}"
            tokens = self.tokenizer.encode(text, add_special_tokens=False)
            if len(tokens) > MIN_TOKENS:
                tokens = tokens[:MAX_TOKENS]
                text = self.tokenizer.decode(tokens)
                self.make_prompt(text)
                self.include = True

    def make_prompt(self, text):
        """
        Set the prompt instance variable to be a prompt appropriate for training
        """
        self.prompt = f"{self.QUESTION}\n\n{text}\n\n"
        self.prompt += f"{self.PREFIX}{str(round(self.price))}.00"
        self.token_count = len(self.tokenizer.encode(self.prompt, add_special_tokens=False))

    def test_prompt(self):
        """
        Return a prompt suitable for testing, with the actual price removed
        """
        return self.prompt.split(self.PREFIX)[0] + self.PREFIX

    def __repr__(self):
        """
        Return a String version of this Item
        """
        return f"<{self.title} = ${self.price}>"
