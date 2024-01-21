1. Guidelines for Prompting:
you'll practice two prompting principles and their related tactics in order to write effective prompts for large language models.

Setup
Load the API key and relevant Python libaries.
In this course, we've provided some code that loads the OpenAI API key for you.

helper function
we will use OpenAI's gpt-3.5-turbo model and the chat completions endpoint.
This helper function will make it easier to use prompts and look at the generated outputs.
Note: In June 2023, OpenAI updated gpt-3.5-turbo. The results you see in the notebook may be slightly different than those in the video. Some of the prompts have also been slightly modified to product the desired results.

Prompting Principles
Principle 1: Write clear and specific instructions
Principle 2: Give the model time to “think”
Tactics
Tactic 1: Use delimiters to clearly indicate distinct parts of the input.

Tactic 2: Ask for a structured output
JSON, HTML

Tactic 3: Ask the model to check whether conditions are satisfied.

Tactic 4: "Few-shot" prompting

Principle 2: Give the model time to “think”
Tactic 1: Specify the steps required to complete a task¶

Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion.

Model Limitations: Hallucinations
Boie is a real company, the product name is not real.

Notes on using the OpenAI API outside of this classroom
To install the OpenAI Python library:

!pip install openai
The library needs to be configured with your account's secret key, which is available on the website.

You can either set it as the OPENAI_API_KEY environment variable before using the library:

 !export OPENAI_API_KEY='sk-...'
Or, set openai.api_key to its value:

import openai
openai.api_key = "sk-..."
A note about the backslash
In the course, we are using a backslash \ to make the text fit on the screen without inserting newline '\n' characters.
GPT-3 isn't really affected whether you insert newline characters or not. But when working with LLMs in general, you may consider whether newline characters in your prompt may affect the model's performance.

2. Iteratuve Prompt Development

you'll iteratively analyze and refine your prompts to generate marketing copy from a product fact sheet.

Setup:
Generate a marketing product description from a product fact sheet

Issue 1: The text is too long
Limit the number of words/sentences/characters.

Issue 2. Text focuses on the wrong details
Ask it to focus on the aspects that are relevant to the intended audience.

Issue 3. Description needs a table of dimensions
Ask it to extract information and organize it in a table.

Load Python libraries to view HTML

3. Summarizing: 
you will summarize text with a focus on specific topics.

Text to summarize

Summarize with a word/sentence/character limit

Summarize with a focus on shipping and delivery

Summarize with a focus on price and value

Comment
Summaries include topics that are not related to the topic of focus.

Try "extract" instead of "summarize"

Summarize multiple product reviews

4. Inferring:

you will infer sentiment and topics from product reviews and news articles.

Product review text

Sentiment (positive/negative)

Identify types of emotions

Identify anger

Extract product and company name from customer reviews

Doing multiple tasks at once

Inferring topics 

Infer 5 topics

Make a news alert for certain topics

5. Transforming

 we will explore how to use Large Language Models for text transformation tasks such as language translation, spelling and grammar checking, tone adjustment, and format conversion.

Translation 
 ChatGPT is trained with sources in many languages. This gives the model the ability to do translation. Here are some examples of how to use this capability.

Universal Translator
Imagine you are in charge of IT at a large multinational e-commerce company. Users are messaging you with IT issues in all their native languages. Your staff is from all over the world and speaks only their native languages. You need a universal translator!

Tone Transformation
Writing can vary based on the intended audience. ChatGPT can produce different tones.

Format Conversion
ChatGPT can translate between formats. The prompt should describe the input and output formats.

Spellcheck/Grammar check.
Here are some examples of common grammar and spelling problems and the LLM's response.

To signal to the LLM that you want it to proofread your text, you instruct the model to 'proofread' or 'proofread and correct'.

6. Expanding

you will generate customer service emails that are tailored to each customer's review.

Customize the automated reply to a customer email

Remind the model to use details from the customer's email

7. ChatBot

 you will explore how you can utilize the chat format to have extended conversations with chatbots personalized or specialized for specific tasks or behaviors.

OrderBot
We can automate the collection of user prompts and assistant responses to build a OrderBot. The OrderBot will take orders at a pizza restaurant.



