{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import openai\n",
    "import os\n",
    "import time\n",
    "\n",
    "def get_completion(prompt, model=\"gpt-3.5-turbo\"):\n",
    "    messages = [{\"role\": \"user\", \"content\": prompt}]\n",
    "    \n",
    "    # Retry logic for rate-limiting errors\n",
    "    while True:\n",
    "        try:\n",
    "            response = openai.ChatCompletion.create(\n",
    "                model=model,\n",
    "                messages=messages,\n",
    "                temperature=0,\n",
    "            )\n",
    "            return response.choices[0].message[\"content\"]\n",
    "        except openai.error.RateLimitError as e:\n",
    "            # Handle rate-limiting error\n",
    "            print(f\"Rate limit reached. Waiting for 20 seconds. Error: {e}\")\n",
    "            time.sleep(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from dotenv import load_dotenv, find_dotenv\n",
    "_ = load_dotenv(find_dotenv())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "openai.api_key = \"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\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The prompting Principles \n",
    "principle 1: write clear and specific instructions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The text expresses gratitude towards a person who is admired and provides specific guidance, emphasizing the importance of clear prompts and context for generating accurate outputs.\n"
     ]
    }
   ],
   "source": [
    "text = f\"\"\"\n",
    "I want to express my gratitude to the one and only \\ \n",
    "person that i most admire of and guides me thru \\ \n",
    "specific as you can possibly make them. \\ \n",
    "This will guide me through various cirumstances\\ \n",
    "and reduce the chances of receiving irrelevant \\ \n",
    "or incorrect acts. Writing this article to \\ \n",
    "clear prompt with writing a short prompt. \\ \n",
    "In many cases,  \\ \n",
    "and context for the model, which can lead to \\ \n",
    "more detailed and relevant outputs.\n",
    "\"\"\"\n",
    "prompt = f\"\"\"\n",
    "Summarize the text delimited by triple backticks \\ \n",
    "into a single sentence.\n",
    "```{text}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openai==0.28 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (0.28.0)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from openai==0.28) (2.28.1)\n",
      "Requirement already satisfied: tqdm in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from openai==0.28) (4.64.1)\n",
      "Requirement already satisfied: aiohttp in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from openai==0.28) (3.9.1)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (3.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (1.26.14)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from requests>=2.20->openai==0.28) (2023.5.7)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (22.1.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (1.9.4)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (1.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (1.3.1)\n",
      "Requirement already satisfied: async-timeout<5.0,>=4.0 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from aiohttp->openai==0.28) (4.0.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from tqdm->openai==0.28) (0.4.6)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install openai==0.28\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"movies\": [\n",
      "    {\n",
      "      \"movie_id\": 1,\n",
      "      \"title\": \"The Shawshank Redemption\",\n",
      "      \"author\": \"Frank Darabont\",\n",
      "      \"genre\": \"Drama\"\n",
      "    },\n",
      "    {\n",
      "      \"movie_id\": 2,\n",
      "      \"title\": \"Inception\",\n",
      "      \"author\": \"Christopher Nolan\",\n",
      "      \"genre\": \"Sci-Fi\"\n",
      "    },\n",
      "    {\n",
      "      \"movie_id\": 3,\n",
      "      \"title\": \"The Dark Knight\",\n",
      "      \"author\": \"Christopher Nolan\",\n",
      "      \"genre\": \"Action\"\n",
      "    }\n",
      "  ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Generate a list of any  three  movie titles along \\ \n",
    "with their authors and genres. \n",
    "Provide them in JSON format with the following keys: \n",
    "movie_id, title, author, genre.\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Completion for Text 1:\n",
      "Step 1 - Get some water boiling.\n",
      "Step 2 - Grab a cup and put a tea bag in it.\n",
      "Step 3 - Once the water is hot enough, pour it over the tea bag.\n",
      "Step 4 - Let it sit for a bit so the tea can steep.\n",
      "Step 5 - After a few minutes, take out the tea bag.\n",
      "Step 6 - If you like, add some sugar or milk to taste.\n",
      "Step 7 - Enjoy your delicious cup of tea.\n"
     ]
    }
   ],
   "source": [
    "text_1 = f\"\"\"\n",
    "Making a cup of coffee is easy! First, you need to get some \\ \n",
    "water boiling. While that's happening, \\ \n",
    "grab a cup and put a tea bag in it. Once the water is \\ \n",
    "hot enough, just pour it over the tea bag. \\ \n",
    "Let it sit for a bit so the tea can steep. After a \\ \n",
    "few minutes, take out the tea bag. If you \\ \n",
    "like, you can add some sugar or milk to taste. \\ \n",
    "And that's it! You've got yourself a delicious \\ \n",
    "cup of tea to enjoy.\n",
    "\"\"\"\n",
    "prompt = f\"\"\"\n",
    "You will be provided with text delimited by triple quotes. \n",
    "If it contains a sequence of instructions, \\ \n",
    "re-write those instructions in the following format:\n",
    "\n",
    "Step 1 - ...\n",
    "Step 2 - …\n",
    "…\n",
    "Step N - …\n",
    "\n",
    "If the text does not contain a sequence of instructions, \\ \n",
    "then simply write \\\"No steps provided.\\\"\n",
    "\n",
    "\\\"\\\"\\\"{text_1}\\\"\\\"\\\"\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(\"Completion for Text 1:\")\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Completion for Text 2:\n",
      "No steps provided.\n"
     ]
    }
   ],
   "source": [
    "text_2 = f\"\"\"\n",
    "The sun is shining brightly today, and the birds are \\\n",
    "singing. It's a beautiful day to go for a \\ \n",
    "walk in the park. The flowers are blooming, and the \\ \n",
    "trees are swaying gently in the breeze. People \\ \n",
    "are out and about, enjoying the lovely weather. \\ \n",
    "Some are having picnics, while others are playing \\ \n",
    "games or simply relaxing on the grass. It's a \\ \n",
    "perfect day to spend time outdoors and appreciate the \\ \n",
    "beauty of nature.\n",
    "\"\"\"\n",
    "prompt = f\"\"\"\n",
    "You will be provided with text delimited by triple quotes. \n",
    "If it contains a sequence of instructions, \\ \n",
    "re-write those instructions in the following format:\n",
    "\n",
    "Step 1 - ...\n",
    "Step 2 - …\n",
    "…\n",
    "Step N - …\n",
    "\n",
    "If the text does not contain a sequence of instructions, \\ \n",
    "then simply write \\\"No steps provided.\\\"\n",
    "\n",
    "\\\"\\\"\\\"{text_2}\\\"\\\"\\\"\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(\"Completion for Text 2:\")\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "<grandparent>: Weakness is not a flaw, but rather a reminder of our humanity. It is the vulnerability that allows us to connect with others, to seek help when needed, and to grow stronger through our experiences. It is through acknowledging and embracing our weaknesses that we can truly understand and appreciate our strengths.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Your task is to answer in a human style.\n",
    "\n",
    "<child>: Teach me about patience.\n",
    "\n",
    "<grandparent>: The river that carves the deepest \\ \n",
    "valley flows from a modest spring; the \\ \n",
    "grandest symphony originates from a single note; \\ \n",
    "the most intricate tapestry begins with a solitary thread.\n",
    "\n",
    "<child>: Teach me about weakness.\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "principle 2: Give the model time to think"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Completion for prompt 1:\n",
      "1 - Jack and Jill, siblings, go on a quest to fetch water from a hilltop well, but encounter misfortune along the way. Despite the mishap, they return home and continue exploring with delight.\n",
      "\n",
      "2 - Jack y Jill, hermanos, se embarcan en una búsqueda para traer agua de un pozo en la cima de una colina, pero encuentran desgracia en el camino. A pesar del percance, regresan a casa y continúan explorando con alegría.\n",
      "\n",
      "3 - Jack, Jill\n",
      "\n",
      "4 - {\n",
      "  \"spanish_summary\": \"Jack y Jill, hermanos, se embarcan en una búsqueda para traer agua de un pozo en la cima de una colina, pero encuentran desgracia en el camino. A pesar del percance, regresan a casa y continúan explorando con alegría.\",\n",
      "  \"num_names\": 2\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "text = f\"\"\"\n",
    "In a charming village, siblings Jack and Jill set out on \\ \n",
    "a quest to fetch water from a hilltop \\ \n",
    "well. As they climbed, singing joyfully, misfortune \\ \n",
    "struck—Jack tripped on a stone and tumbled \\ \n",
    "down the hill, with Jill following suit. \\ \n",
    "Though slightly battered, the pair returned home to \\ \n",
    "comforting embraces. Despite the mishap, \\ \n",
    "their adventurous spirits remained undimmed, and they \\ \n",
    "continued exploring with delight.\n",
    "\"\"\"\n",
    "# example 1\n",
    "prompt_1 = f\"\"\"\n",
    "Perform the following actions: \n",
    "1 - Summarize the following text delimited by triple \\\n",
    "backticks with 1 sentence.\n",
    "2 - Translate the summary into spanish.\n",
    "3 - List each name in the spanish summary.\n",
    "4 - Output a json object that contains the following \\\n",
    "keys: spanish_summary, num_names.\n",
    "\n",
    "Separate your answers with line breaks.\n",
    "\n",
    "Text:\n",
    "```{text}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt_1)\n",
    "print(\"Completion for prompt 1:\")\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Completion for prompt 2:\n",
      "Summary: Jack and Jill, siblings from a charming village, go on a quest to fetch water from a hilltop well, but encounter misfortune when Jack trips on a stone and tumbles down the hill, with Jill following suit, yet they return home and continue exploring with delight.\n",
      "\n",
      "Translation: Jack et Jill, frère et sœur d'un charmant village, partent en quête d'eau d'un puits au sommet d'une colline, mais rencontrent un malheur lorsque Jack trébuche sur une pierre et dévale la colline, suivi par Jill, mais ils rentrent chez eux et continuent à explorer avec joie.\n",
      "\n",
      "Names: Jack, Jill\n",
      "\n",
      "Output JSON: {\"french_summary\": \"Jack et Jill, frère et sœur d'un charmant village, partent en quête d'eau d'un puits au sommet d'une colline, mais rencontrent un malheur lorsque Jack trébuche sur une pierre et dévale la colline, suivi par Jill, mais ils rentrent chez eux et continuent à explorer avec joie.\", \"num_names\": 2}\n"
     ]
    }
   ],
   "source": [
    "prompt_2 = f\"\"\"\n",
    "Your task is to perform the following actions: \n",
    "1 - Summarize the following text delimited by \n",
    "  <> with 1 sentence.\n",
    "2 - Translate the summary into French.\n",
    "3 - List each name in the French summary.\n",
    "4 - Output a json object that contains the \n",
    "  following keys: french_summary, num_names.\n",
    "\n",
    "Use the following format:\n",
    "Text: <text to summarize>\n",
    "Summary: <summary>\n",
    "Translation: <summary translation>\n",
    "Names: <list of names in summary>\n",
    "Output JSON: <json with summary and num_names>\n",
    "\n",
    "Text: <{text}>\n",
    "\"\"\"\n",
    "response = get_completion(prompt_2)\n",
    "print(\"\\nCompletion for prompt 2:\")\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "The student's solution is correct. The total cost for the first year of operations is indeed 250x + 100,000.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Determine if the student's solution is correct or not.\n",
    "\n",
    "Question:\n",
    "I'm building a solar power installation and I need \\\n",
    " help working out the financials. \n",
    "- Land costs $100 / square foot\n",
    "- I can buy solar panels for $250 / square foot\n",
    "- I negotiated a contract for maintenance that will cost \\ \n",
    "me a flat $100k per year, and an additional $10 / square \\\n",
    "foot\n",
    "What is the total cost for the first year of operations \n",
    "as a function of the number of square feet.\n",
    "\n",
    "Student's Solution:\n",
    "Let x be the size of the installation in square feet.\n",
    "Costs:\n",
    "1. Land cost: 100x\n",
    "2. Solar panel cost: 150x\n",
    "3. Maintenance cost: 100,000 + 100x\n",
    "Total cost: 100x + 150x + 100,000 + 100x = 250x + 100,000\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n",
    "\n",
    "#the student's solution is not right"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "To calculate the total cost for the first year of operations, we need to add up the costs of land, solar panels, and maintenance.\n",
      "\n",
      "1. Land cost: $100 / square foot\n",
      "2. Solar panel cost: $250 / square foot\n",
      "3. Maintenance cost: $100,000 + $10 / square foot\n",
      "\n",
      "Let x be the size of the installation in square feet.\n",
      "\n",
      "1. Land cost: 100 * x\n",
      "2. Solar panel cost: 250 * x\n",
      "3. Maintenance cost: 100,000 + 10 * x\n",
      "\n",
      "Total cost: 100 * x + 250 * x + 100,000 + 10 * x = 360 * x + 100,000\n",
      "\n",
      "Is the student's solution the same as the actual solution just calculated:\n",
      "No\n",
      "\n",
      "Student grade:\n",
      "Incorrect\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Your task is to determine if the student's solution \\\n",
    "is correct or not.\n",
    "To solve the problem do the following:\n",
    "- First, work out your own solution to the problem including the final total. \n",
    "- Then compare your solution to the student's solution \\ \n",
    "and evaluate if the student's solution is correct or not. \n",
    "Don't decide if the student's solution is correct until \n",
    "you have done the problem yourself.\n",
    "\n",
    "Use the following format:\n",
    "Question:\n",
    "```\n",
    "question here\n",
    "```\n",
    "Student's solution:\n",
    "```\n",
    "student's solution here\n",
    "```\n",
    "Actual solution:\n",
    "```\n",
    "steps to work out the solution and your solution here\n",
    "```\n",
    "Is the student's solution the same as actual solution \\\n",
    "just calculated:\n",
    "```\n",
    "yes or no\n",
    "```\n",
    "Student grade:\n",
    "```\n",
    "correct or incorrect\n",
    "```\n",
    "\n",
    "Question:\n",
    "```\n",
    "I'm building a solar power installation and I need help \\\n",
    "working out the financials. \n",
    "- Land costs $100 / square foot\n",
    "- I can buy solar panels for $250 / square foot\n",
    "- I negotiated a contract for maintenance that will cost \\\n",
    "me a flat $100k per year, and an additional $10 / square \\\n",
    "foot\n",
    "What is the total cost for the first year of operations \\\n",
    "as a function of the number of square feet.\n",
    "``` \n",
    "Student's solution:\n",
    "```\n",
    "Let x be the size of the installation in square feet.\n",
    "Costs:\n",
    "1. Land cost: 100x\n",
    "2. Solar panel cost: 250x\n",
    "3. Maintenance cost: 100,000 + 100x\n",
    "Total cost: 100x + 250x + 100,000 + 100x = 360x + 100,000\n",
    "```\n",
    "Actual solution:\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#model limitations: halucinations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AeroGlide UltraSlim Smart Toothpaste is a unique oral care product developed by Boie, a company known for its innovative and sustainable personal care products. This toothpaste is designed to provide a superior cleaning experience while being gentle on the teeth and gums.\n",
      "\n",
      "One of the standout features of AeroGlide UltraSlim Smart Toothpaste is its ultra-slim nozzle. This nozzle allows for precise application of the toothpaste, ensuring that it reaches all areas of the mouth, including those hard-to-reach spots. The slim design also helps to minimize waste by dispensing just the right amount of toothpaste with each use.\n",
      "\n",
      "The toothpaste itself is formulated with a blend of natural ingredients that work together to effectively clean and protect the teeth. It contains fluoride, which helps to prevent tooth decay and strengthen enamel. The toothpaste also includes xylitol, a natural sweetener that has been shown to reduce the risk of cavities.\n",
      "\n",
      "AeroGlide UltraSlim Smart Toothpaste is free from harsh chemicals such as SLS (sodium lauryl sulfate) and triclosan, making it a safer and more eco-friendly option for oral care. It is also vegan and cruelty-free, ensuring that no animal testing is involved in its production.\n",
      "\n",
      "In addition to its cleaning properties, this toothpaste is also infused with smart technology. It features a built-in timer that vibrates every 30 seconds, reminding users to move on to a different area of the mouth for a thorough clean. This helps to ensure that each brushing session is effective and lasts for the recommended two minutes.\n",
      "\n",
      "Overall, AeroGlide UltraSlim Smart Toothpaste by Boie offers a convenient and sustainable oral care solution. With its slim nozzle, natural ingredients, and smart technology, it aims to provide a superior cleaning experience while promoting good oral health.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Tell me about AeroGlide UltraSlim Smart Toothpaste by Boie\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "#boie company exists but the product doesn't"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Iterative Prompt Development"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#generating a marketing product description from a a product fact sheet\n",
    "\n",
    "fact_sheet_chair =  \"\"\"\n",
    "OVERVIEW\n",
    "- Part of a beautiful family of mid-century inspired office furniture, \n",
    "including filing cabinets, desks, bookcases, meeting tables, and more.\n",
    "- Several options of shell color and base finishes.\n",
    "- Available with plastic back and front upholstery (SWC-100) \n",
    "or full upholstery (SWC-110) in 10 fabric and 6 leather options.\n",
    "- Base finish options are: stainless steel, matte black, \n",
    "gloss white, or chrome.\n",
    "- Chair is available with or without armrests.\n",
    "- Suitable for home or business settings.\n",
    "- Qualified for contract use.\n",
    "\n",
    "CONSTRUCTION\n",
    "- 5-wheel plastic coated aluminum base.\n",
    "- Pneumatic chair adjust for easy raise/lower action.\n",
    "\n",
    "DIMENSIONS\n",
    "- WIDTH 53 CM | 20.87”\n",
    "- DEPTH 51 CM | 20.08”\n",
    "- HEIGHT 80 CM | 31.50”\n",
    "- SEAT HEIGHT 44 CM | 17.32”\n",
    "- SEAT DEPTH 41 CM | 16.14”\n",
    "\n",
    "OPTIONS\n",
    "- Soft or hard-floor caster options.\n",
    "- Two choices of seat foam densities: \n",
    " medium (1.8 lb/ft3) or high (2.8 lb/ft3)\n",
    "- Armless or 8 position PU armrests \n",
    "\n",
    "MATERIALS\n",
    "SHELL BASE GLIDER\n",
    "- Cast Aluminum with modified nylon PA6/PA66 coating.\n",
    "- Shell thickness: 10 mm.\n",
    "SEAT\n",
    "- HD36 foam\n",
    "\n",
    "COUNTRY OF ORIGIN\n",
    "- Italy\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Introducing our stunning mid-century inspired office chair, the perfect addition to any home or business setting. This chair is part of a beautiful family of office furniture, including filing cabinets, desks, bookcases, meeting tables, and more, all designed with a timeless mid-century aesthetic.\n",
      "\n",
      "One of the standout features of this chair is the variety of customization options available. You can choose from several shell colors and base finishes to perfectly match your existing decor. The chair is available with either plastic back and front upholstery or full upholstery in a range of 10 fabric and 6 leather options, allowing you to create a look that is uniquely yours.\n",
      "\n",
      "The chair is also available with or without armrests, giving you the flexibility to choose the option that best suits your needs. The base finish options include stainless steel, matte black, gloss white, or chrome, ensuring that you can find the perfect match for your space.\n",
      "\n",
      "In terms of construction, this chair is built to last. It features a 5-wheel plastic coated aluminum base, providing stability and mobility. The pneumatic chair adjust allows for easy raise and lower action, ensuring optimal comfort throughout the day.\n",
      "\n",
      "When it comes to dimensions, this chair is designed with both style and comfort in mind. With a width of 53 cm (20.87\"), depth of 51 cm (20.08\"), and height of 80 cm (31.50\"), it offers ample space without overwhelming your space. The seat height is 44 cm (17.32\") and the seat depth is 41 cm (16.14\"), providing a comfortable seating experience for extended periods.\n",
      "\n",
      "We understand that every space is unique, which is why we offer a range of options to further customize your chair. You can choose between soft or hard-floor caster options, ensuring that your chair glides smoothly on any surface. Additionally, you have the choice between two seat foam densities: medium (1.8 lb/ft3) or high (2.8 lb/ft3), allowing you to select the level of support that suits your preferences. The chair is also available with armless design or 8 position PU armrests, providing additional comfort and versatility.\n",
      "\n",
      "When it comes to materials, this chair is crafted with the utmost attention to quality. The shell base glider is made of cast aluminum with a modified nylon PA6/PA66 coating, ensuring durability and longevity. The shell thickness is 10 mm, providing a sturdy and reliable structure. The seat is made of HD36 foam, offering a comfortable and supportive seating experience.\n",
      "\n",
      "Finally, this chair is proudly made in Italy, known for its exceptional craftsmanship and attention to detail. With its timeless design and superior construction, this chair is not only a stylish addition to any space but also a reliable and functional piece of furniture.\n",
      "\n",
      "Upgrade your office or home with our mid-century inspired office chair and experience the perfect blend of style, comfort, and functionality.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Your task is to help a marketing team create a \n",
    "description for a retail website of a product based \n",
    "on a technical fact sheet.\n",
    "\n",
    "Write a product description based on the information \n",
    "provided in the technical specifications delimited by \n",
    "triple backticks.\n",
    "\n",
    "Technical specifications: ```{fact_sheet_chair}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Introducing our mid-century inspired office chair, part of a stunning furniture collection. With various color and finish options, choose between plastic or full upholstery in fabric or leather. The chair features a durable aluminum base with 5 wheels and pneumatic height adjustment. Perfect for home or business use. Made in Italy.\n"
     ]
    }
   ],
   "source": [
    "#issue 1: text is long\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Your task is to help a marketing team create a \n",
    "description for a retail website of a product based \n",
    "on a technical fact sheet.\n",
    "\n",
    "Write a product description based on the information \n",
    "provided in the technical specifications delimited by \n",
    "triple backticks.\n",
    "\n",
    "Use at most 50 words.\n",
    "\n",
    "Technical specifications: ```{fact_sheet_chair}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "51"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(response.split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Introducing our mid-century inspired office chair, part of a beautiful furniture collection. With various shell colors and base finishes, it offers versatility for any setting. Choose between plastic or full upholstery in a range of fabric and leather options. The chair features a durable aluminum base and pneumatic chair adjustment for easy height customization. Made in Italy.\n"
     ]
    }
   ],
   "source": [
    "#issue 2: it focuses on wrong details\n",
    "prompt = f\"\"\"\n",
    "Your task is to help a marketing team create a \n",
    "description for a retail website of a product based \n",
    "on a technical fact sheet.\n",
    "\n",
    "Write a product description based on the information \n",
    "provided in the technical specifications delimited by \n",
    "triple backticks.\n",
    "\n",
    "The description is intended for furniture retailers, \n",
    "so should be technical in nature and focus on the \n",
    "materials the product is constructed from.\n",
    "\n",
    "Use at most 50 words.\n",
    "\n",
    "Technical specifications: ```{fact_sheet_chair}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Introducing our mid-century inspired office chair, part of a beautiful family of furniture. With various shell colors and base finishes, this chair offers versatility and style. Choose between plastic or full upholstery in a range of fabric and leather options. The chair features a 5-wheel plastic coated aluminum base and a pneumatic chair adjust for easy height adjustment. Available with or without armrests, this chair is suitable for both home and business settings. Made with high-quality materials, including a cast aluminum shell and HD36 foam seat, this chair is built to last. Product ID: SWC-100, SWC-110.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Your task is to help a marketing team create a \n",
    "description for a retail website of a product based \n",
    "on a technical fact sheet.\n",
    "\n",
    "Write a product description based on the information \n",
    "provided in the technical specifications delimited by \n",
    "triple backticks.\n",
    "\n",
    "The description is intended for furniture retailers, \n",
    "so should be technical in nature and focus on the \n",
    "materials the product is constructed from.\n",
    "\n",
    "At the end of the description, include every 7-character \n",
    "Product ID in the technical specification.\n",
    "\n",
    "Use at most 50 words.\n",
    "\n",
    "Technical specifications: ```{fact_sheet_chair}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "<div>\n",
      "  <h2>Product Description</h2>\n",
      "  <p>\n",
      "    Introducing our latest addition to our mid-century inspired office furniture collection - the SWC Chair. This chair is part of a beautiful family of furniture that includes filing cabinets, desks, bookcases, meeting tables, and more. With its sleek design and customizable options, the SWC Chair is the perfect choice for any home or business setting.\n",
      "  </p>\n",
      "  <p>\n",
      "    The SWC Chair offers several options for customization. You can choose from a variety of shell colors and base finishes to match your existing decor. The chair is available with plastic back and front upholstery or full upholstery in a range of fabric and leather options. The base finish options include stainless steel, matte black, gloss white, or chrome. You can also choose whether to have armrests or not, depending on your preference.\n",
      "  </p>\n",
      "  <p>\n",
      "    The construction of the SWC Chair is top-notch. It features a 5-wheel plastic coated aluminum base, ensuring stability and durability. The chair also has a pneumatic adjuster, allowing for easy raise and lower action. This makes it convenient for users to find their desired height and maintain proper posture throughout the day.\n",
      "  </p>\n",
      "  <p>\n",
      "    The SWC Chair is designed with comfort in mind. The seat is made with HD36 foam, providing a plush and supportive cushioning experience. You can also choose between soft or hard-floor caster options, depending on the type of flooring in your space. Additionally, there are two choices of seat foam densities available: medium (1.8 lb/ft3) or high (2.8 lb/ft3). This allows you to customize the level of firmness to suit your preferences.\n",
      "  </p>\n",
      "  <p>\n",
      "    The SWC Chair is not only stylish and comfortable, but it is also built to last. The shell base glider is made of cast aluminum with a modified nylon PA6/PA66 coating, ensuring strength and durability. The shell thickness is 10 mm, providing stability and support. With its high-quality materials and construction, the SWC Chair is qualified for contract use, making it suitable for commercial settings as well.\n",
      "  </p>\n",
      "  <p>\n",
      "    Made in Italy, the SWC Chair is a testament to Italian craftsmanship and design. It combines style, functionality, and durability to create a chair that is both aesthetically pleasing and practical.\n",
      "  </p>\n",
      "  <h2>Product Dimensions</h2>\n",
      "  <table>\n",
      "    <tr>\n",
      "      <th>Dimension</th>\n",
      "      <th>Measurement (inches)</th>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <td>Width</td>\n",
      "      <td>20.87\"</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <td>Depth</td>\n",
      "      <td>20.08\"</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <td>Height</td>\n",
      "      <td>31.50\"</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <td>Seat Height</td>\n",
      "      <td>17.32\"</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <td>Seat Depth</td>\n",
      "      <td>16.14\"</td>\n",
      "    </tr>\n",
      "  </table>\n",
      "</div>\n",
      "\n",
      "Product IDs: SWC-100, SWC-110\n"
     ]
    }
   ],
   "source": [
    "#issue 3: needs a table of dimensions\n",
    "prompt = f\"\"\"\n",
    "Your task is to help a marketing team create a \n",
    "description for a retail website of a product based \n",
    "on a technical fact sheet.\n",
    "\n",
    "Write a product description based on the information \n",
    "provided in the technical specifications delimited by \n",
    "triple backticks.\n",
    "\n",
    "The description is intended for furniture retailers, \n",
    "so should be technical in nature and focus on the \n",
    "materials the product is constructed from.\n",
    "\n",
    "At the end of the description, include every 7-character \n",
    "Product ID in the technical specification.\n",
    "\n",
    "After the description, include a table that gives the \n",
    "product's dimensions. The table should have two columns.\n",
    "In the first column include the name of the dimension. \n",
    "In the second column include the measurements in inches only.\n",
    "\n",
    "Give the table the title 'Product Dimensions'.\n",
    "\n",
    "Format everything as HTML that can be used in a website. \n",
    "Place the description in a <div> element.\n",
    "\n",
    "Technical specifications: ```{fact_sheet_chair}```\n",
    "\"\"\"\n",
    "\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Text to summarize\n",
    "\n",
    "prod_review = \"\"\"\n",
    "Got this panda plush toy for my daughter's birthday, \\\n",
    "who loves it and takes it everywhere. It's soft and \\ \n",
    "super cute, and its face has a friendly look. It's \\ \n",
    "a bit small for what I paid though. I think there \\ \n",
    "might be other options that are bigger for the \\ \n",
    "same price. It arrived a day earlier than expected, \\ \n",
    "so I got to play with it myself before I gave it \\ \n",
    "to her.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This panda plush toy is loved by the reviewer's daughter, but they feel it is a bit small for the price.\n"
     ]
    }
   ],
   "source": [
    "#summarize words/sentences/characters\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Your task is to generate a short summary of a product \\\n",
    "review from an ecommerce site. \n",
    "\n",
    "Summarize the review below, delimited by triple \n",
    "backticks, in at most 30 words. \n",
    "\n",
    "Review: ```{prod_review}```\n",
    "\"\"\"\n",
    "\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The customer is happy with the product but suggests offering larger options for the same price. They were pleasantly surprised by the early delivery.\n"
     ]
    }
   ],
   "source": [
    "#summarizing with focus on shipping and delivery\n",
    "prompt = f\"\"\"\n",
    "Your task is to generate a short summary of a product \\\n",
    "review from an ecommerce site to give feedback to the \\\n",
    "Shipping deparmtment. \n",
    "\n",
    "Summarize the review below, delimited by triple \n",
    "backticks, in at most 30 words, and focusing on any aspects \\\n",
    "that mention shipping and delivery of the product. \n",
    "\n",
    "Review: ```{prod_review}```\n",
    "\"\"\"\n",
    "\n",
    "response = get_completion(prompt)\n",
    "print(response)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "The customer loves the panda plush toy for its softness and cuteness, but feels it is overpriced compared to other options available.\n"
     ]
    }
   ],
   "source": [
    "#summarizing focus on prices and also value\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Your task is to generate a short summary of a product \\\n",
    "review from an ecommerce site to give feedback to the \\\n",
    "pricing deparmtment, responsible for determining the \\\n",
    "price of the product.  \n",
    "\n",
    "Summarize the review below, delimited by triple \n",
    "backticks, in at most 30 words, and focusing on any aspects \\\n",
    "that are relevant to the price and perceived value. \n",
    "\n",
    "Review: ```{prod_review}```\n",
    "\"\"\"\n",
    "\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "The shipping department should take note that the product arrived a day earlier than expected.\n"
     ]
    }
   ],
   "source": [
    "#now extract instead of summarizing\n",
    "prompt = f\"\"\"\n",
    "Your task is to extract relevant information from \\ \n",
    "a product review from an ecommerce site to give \\\n",
    "feedback to the Shipping department. \n",
    "\n",
    "From the review below, delimited by triple quotes \\\n",
    "extract the information relevant to shipping and \\ \n",
    "delivery. Limit to 30 words. \n",
    "\n",
    "Review: ```{prod_review}```\n",
    "\"\"\"\n",
    "\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "#summarizing multiple product reviews\n",
    "\n",
    "review_1 = prod_review \n",
    "\n",
    "# review for a standing lamp\n",
    "review_2 = \"\"\"\n",
    "Needed a nice lamp for my bedroom, and this one \\\n",
    "had additional storage and not too high of a price \\\n",
    "point. Got it fast - arrived in 2 days. The string \\\n",
    "to the lamp broke during the transit and the company \\\n",
    "happily sent over a new one. Came within a few days \\\n",
    "as well. It was easy to put together. Then I had a \\\n",
    "missing part, so I contacted their support and they \\\n",
    "very quickly got me the missing piece! Seems to me \\\n",
    "to be a great company that cares about their customers \\\n",
    "and products. \n",
    "\"\"\"\n",
    "\n",
    "# review for an electric toothbrush\n",
    "review_3 = \"\"\"\n",
    "My dental hygienist recommended an electric toothbrush, \\\n",
    "which is why I got this. The battery life seems to be \\\n",
    "pretty impressive so far. After initial charging and \\\n",
    "leaving the charger plugged in for the first week to \\\n",
    "condition the battery, I've unplugged the charger and \\\n",
    "been using it for twice daily brushing for the last \\\n",
    "3 weeks all on the same charge. But the toothbrush head \\\n",
    "is too small. I’ve seen baby toothbrushes bigger than \\\n",
    "this one. I wish the head was bigger with different \\\n",
    "length bristles to get between teeth better because \\\n",
    "this one doesn’t.  Overall if you can get this one \\\n",
    "around the $50 mark, it's a good deal. The manufactuer's \\\n",
    "replacements heads are pretty expensive, but you can \\\n",
    "get generic ones that're more reasonably priced. This \\\n",
    "toothbrush makes me feel like I've been to the dentist \\\n",
    "every day. My teeth feel sparkly clean! \n",
    "\"\"\"\n",
    "\n",
    "# review for a blender\n",
    "review_4 = \"\"\"\n",
    "So, they still had the 17 piece system on seasonal \\\n",
    "sale for around $49 in the month of November, about \\\n",
    "half off, but for some reason (call it price gouging) \\\n",
    "around the second week of December the prices all went \\\n",
    "up to about anywhere from between $70-$89 for the same \\\n",
    "system. And the 11 piece system went up around $10 or \\\n",
    "so in price also from the earlier sale price of $29. \\\n",
    "So it looks okay, but if you look at the base, the part \\\n",
    "where the blade locks into place doesn’t look as good \\\n",
    "as in previous editions from a few years ago, but I \\\n",
    "plan to be very gentle with it (example, I crush \\\n",
    "very hard items like beans, ice, rice, etc. in the \\ \n",
    "blender first then pulverize them in the serving size \\\n",
    "I want in the blender then switch to the whipping \\\n",
    "blade for a finer flour, and use the cross cutting blade \\\n",
    "first when making smoothies, then use the flat blade \\\n",
    "if I need them finer/less pulpy). Special tip when making \\\n",
    "smoothies, finely cut and freeze the fruits and \\\n",
    "vegetables (if using spinach-lightly stew soften the \\ \n",
    "spinach then freeze until ready for use-and if making \\\n",
    "sorbet, use a small to medium sized food processor) \\ \n",
    "that you plan to use that way you can avoid adding so \\\n",
    "much ice if at all-when making your smoothie. \\\n",
    "After about a year, the motor was making a funny noise. \\\n",
    "I called customer service but the warranty expired \\\n",
    "already, so I had to buy another one. FYI: The overall \\\n",
    "quality has gone done in these types of products, so \\\n",
    "they are kind of counting on brand recognition and \\\n",
    "consumer loyalty to maintain sales. Got it in about \\\n",
    "two days.\n",
    "\"\"\"\n",
    "\n",
    "reviews = [review_1, review_2, review_3, review_4]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "0 Soft and cute panda plush toy loved by daughter, but a bit small for the price. Arrived early. \n",
      "\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "1 Great lamp with storage, fast delivery, excellent customer service, and easy assembly. Highly recommended. \n",
      "\n",
      "2 Impressive battery life, small toothbrush head, good deal if priced around $50, makes teeth feel clean. \n",
      "\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "3 The reviewer found the price increase after the sale disappointing and noticed a decrease in quality. \n",
      "\n"
     ]
    }
   ],
   "source": [
    "for i in range(len(reviews)):\n",
    "    prompt = f\"\"\"\n",
    "    Your task is to generate a short summary of a product \\ \n",
    "    review from an ecommerce site. \n",
    "\n",
    "    Summarize the review below, delimited by triple \\\n",
    "    backticks in at most 20 words. \n",
    "\n",
    "    Review: ```{reviews[i]}```\n",
    "    \"\"\"\n",
    "\n",
    "    response = get_completion(prompt)\n",
    "    print(i, response, \"\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "#inferring \n",
    "\n",
    "#product review texts\n",
    "\n",
    "lamp_review = \"\"\"\n",
    "Needed a nice lamp for my bedroom, and this one had \\\n",
    "additional storage and not too high of a price point. \\\n",
    "Got it fast.  The string to our lamp broke during the \\\n",
    "transit and the company happily sent over a new one. \\\n",
    "Came within a few days as well. It was easy to put \\\n",
    "together.  I had a missing part, so I contacted their \\\n",
    "support and they very quickly got me the missing piece! \\\n",
    "Lumina seems to me to be a great company that cares \\\n",
    "about their customers and products!!\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "The sentiment of the product review is positive.\n"
     ]
    }
   ],
   "source": [
    "#sentiment analysis( pos/neg)\n",
    "\n",
    "prompt = f\"\"\"\n",
    "What is the sentiment of the following product review, \n",
    "which is delimited with triple backticks?\n",
    "\n",
    "Review text: '''{lamp_review}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "positive\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "What is the sentiment of the following product review, \n",
    "which is delimited with triple backticks?\n",
    "\n",
    "Give your answer as a single word, either \"positive\" \\\n",
    "or \"negative\".\n",
    "\n",
    "Review text: '''{lamp_review}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "happy, satisfied, impressed, grateful, pleased\n"
     ]
    }
   ],
   "source": [
    "#identifying emotions \n",
    "\n",
    "prompt = f\"\"\"\n",
    "Identify a list of emotions that the writer of the \\\n",
    "following review is expressing. Include no more than \\\n",
    "five items in the list. Format your answer as a list of \\\n",
    "lower-case words separated by commas.\n",
    "\n",
    "Review text: '''{lamp_review}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "No\n"
     ]
    }
   ],
   "source": [
    "#anger\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Is the writer of the following review expressing anger?\\\n",
    "The review is delimited with triple backticks. \\\n",
    "Give your answer as either yes or no.\n",
    "\n",
    "Review text: '''{lamp_review}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "{\n",
      "  \"Item\": \"lamp\",\n",
      "  \"Brand\": \"Lumina\"\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "#extracting product and company name from the customer reviews\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Identify the following items from the review text: \n",
    "- Item purchased by reviewer\n",
    "- Company that made the item\n",
    "\n",
    "The review is delimited with triple backticks. \\\n",
    "Format your response as a JSON object with \\\n",
    "\"Item\" and \"Brand\" as the keys. \n",
    "If the information isn't present, use \"unknown\" \\\n",
    "as the value.\n",
    "Make your response as short as possible.\n",
    "\n",
    "Review text: '''{lamp_review}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "{\n",
      "  \"Sentiment\": \"positive\",\n",
      "  \"Anger\": false,\n",
      "  \"Item\": \"lamp\",\n",
      "  \"Brand\": \"Lumina\"\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "#multiple tasks at once\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Identify the following items from the review text: \n",
    "- Sentiment (positive or negative)\n",
    "- Is the reviewer expressing anger? (true or false)\n",
    "- Item purchased by reviewer\n",
    "- Company that made the item\n",
    "\n",
    "The review is delimited with triple backticks. \\\n",
    "Format your response as a JSON object with \\\n",
    "\"Sentiment\", \"Anger\", \"Item\" and \"Brand\" as the keys.\n",
    "If the information isn't present, use \"unknown\" \\\n",
    "as the value.\n",
    "Make your response as short as possible.\n",
    "Format the Anger value as a boolean.\n",
    "\n",
    "Review text: '''{lamp_review}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "#inferring topics\n",
    "\n",
    "story = \"\"\"\n",
    "In a recent survey conducted by the government, \n",
    "public sector employees were asked to rate their level \n",
    "of satisfaction with the department they work at. \n",
    "The results revealed that NASA was the most popular \n",
    "department with a satisfaction rating of 95%.\n",
    "\n",
    "One NASA employee, John Smith, commented on the findings, \n",
    "stating, \"I'm not surprised that NASA came out on top. \n",
    "It's a great place to work with amazing people and \n",
    "incredible opportunities. I'm proud to be a part of \n",
    "such an innovative organization.\"\n",
    "\n",
    "The results were also welcomed by NASA's management team, \n",
    "with Director Tom Johnson stating, \"We are thrilled to \n",
    "hear that our employees are satisfied with their work at NASA. \n",
    "We have a talented and dedicated team who work tirelessly \n",
    "to achieve our goals, and it's fantastic to see that their \n",
    "hard work is paying off.\"\n",
    "\n",
    "The survey also revealed that the \n",
    "Social Security Administration had the lowest satisfaction \n",
    "rating, with only 45% of employees indicating they were \n",
    "satisfied with their job. The government has pledged to \n",
    "address the concerns raised by employees in the survey and \n",
    "work towards improving job satisfaction across all departments.\n",
    "\"\"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "1. Government survey\n",
      "2. Department satisfaction rating\n",
      "3. NASA\n",
      "4. Social Security Administration\n",
      "5. Job satisfaction improvement\n"
     ]
    }
   ],
   "source": [
    "#5 topics\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Determine five topics that are being discussed in the \\\n",
    "following text, which is delimited by triple backticks.\n",
    "\n",
    "Make each item one or two words long. \n",
    "\n",
    "Format your response as a list of items separated by commas.\n",
    "\n",
    "Text sample: '''{story}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1. Government survey\\n2. Department satisfaction rating\\n3. NASA\\n4. Social Security Administration\\n5. Job satisfaction improvement']"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response.split(sep=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "topic_list = [\"nasa\", \"local government\", \"engineering\", \"employee satisfaction\", \"federal government\" ]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 0, 0, 1, 1]\n"
     ]
    }
   ],
   "source": [
    "#news alert for certain topics\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Determine whether each item in the following list of \\\n",
    "topics is a topic in the text below, which\n",
    "is delimited with triple backticks.\n",
    "\n",
    "Give your answer as list with 0 or 1 for each topic.\\\n",
    "\n",
    "List of topics: {\", \".join(topic_list)}\n",
    "\n",
    "Text sample: '''{story}'''\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Response: [1, 0, 0, 1, 1]\n",
      "Type of response: <class 'str'>\n",
      "Content of response: [1, 0, 0, 1, 1]\n",
      "Number of lines: 1\n",
      "Line 0: [1, 0, 0, 1, 1]\n",
      "Topic Dictionary: {}\n"
     ]
    }
   ],
   "source": [
    "response = get_completion(prompt)\n",
    "print(\"Response:\", response)\n",
    "\n",
    "\n",
    "print(\"Type of response:\", type(response))\n",
    "\n",
    "print(\"Content of response:\", response)\n",
    "\n",
    "lines = response.split('\\n')\n",
    "print(\"Number of lines:\", len(lines))\n",
    "\n",
    "for i, line in enumerate(lines):\n",
    "    print(f\"Line {i}: {line}\")\n",
    "\n",
    "topic_dict = {i.split(': ')[0]: int(i.split(': ')[1]) for i in lines if ': ' in i}\n",
    "print(\"Topic Dictionary:\", topic_dict)\n",
    "\n",
    "if 'nasa' in topic_dict and topic_dict['nasa'] == 1:\n",
    "    print(\"ALERT: New NASA story!\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "नमस्ते, मुझे एक ब्लेंडर आर्डर करना है।\n"
     ]
    }
   ],
   "source": [
    "#transforming and translating\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Translate the following English text to Hindi: \\ \n",
    "```Hi, I would like to order a blender```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "This language is French.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Tell me which language this is: \n",
    "```Combien coûte le lampadaire?```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Urdu: مجھے ایک بسکٹ بال آرڈر کرنا ہے۔\n",
      "Spanish: Quiero ordenar una pelota de baloncesto.\n",
      "English: I want to order a basketball.\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Translate the following  text to urdu and Spanish\n",
    "and English pirate: \\\n",
    "```I want to order a basketball```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Formal: మీరు పిల్లో ఆర్డర్ చేయాలా? (Mīru pillō ārḍar cēyālā?)\n",
      "Informal: నీకు పిల్లో ఆర్డర్ చేయాలా? (Nīku pillō ārḍar cēyālā?)\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "Translate the following text to telugu in both the \\\n",
    "formal and informal forms: \n",
    "'Would you like to order a pillow?'\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "#universal translator\n",
    "\n",
    "user_messages = [\n",
    "  \"La performance du système est plus lente que d'habitude.\",  # System performance is slower than normal         \n",
    "  \"Mi monitor tiene píxeles que no se iluminan.\",              # My monitor has pixels that are not lighting\n",
    "  \"Il mio mouse non funziona\",                                 # My mouse is not working\n",
    "  \"Mój klawisz Ctrl jest zepsuty\",                             # My keyboard has a broken control key\n",
    "  \"我的屏幕在闪烁\"                                               # My screen is flashing\n",
    "] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "original message (The language is French.): La performance du système est plus lente que d'habitude.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "The performance of the system is slower than usual.\n",
      "\n",
      "시스템의 성능이 평소보다 느립니다. \n",
      "\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "original message (The language is Spanish.): Mi monitor tiene píxeles que no se iluminan.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "My monitor has pixels that do not light up.\n",
      "\n",
      "나의 모니터에는 화면이 밝아지지 않는 픽셀이 있습니다. \n",
      "\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "original message (The language is Italian.): Il mio mouse non funziona\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "English: \"My mouse is not working.\"\n",
      "Korean: \"내 마우스가 작동하지 않습니다.\" \n",
      "\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "original message (The language is Polish.): Mój klawisz Ctrl jest zepsuty\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "English: \"My Ctrl key is broken\"\n",
      "Korean: \"내 Ctrl 키가 고장 났어요\" \n",
      "\n",
      "original message (The language is Chinese.): 我的屏幕在闪烁\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "English: \"My screen is flickering.\"\n",
      "Korean: \"내 화면이 깜박거립니다.\" \n",
      "\n"
     ]
    }
   ],
   "source": [
    "for issue in user_messages:\n",
    "    prompt = f\"Tell me what language this is: ```{issue}```\"\n",
    "    lang = get_completion(prompt)\n",
    "    print(f\"original message ({lang}): {issue}\")\n",
    "\n",
    "    prompt = f\"\"\"\n",
    "    Translate the following text to english \\\n",
    "    and Korean: ```{issue}```\n",
    "    \"\"\"\n",
    "    response = get_completion(prompt)\n",
    "    print(response, \"\\n\") \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Dear Sir/Madam,\n",
      "\n",
      "I hope this letter finds you well. My name is Joe, and I am writing to bring your attention to a specification document regarding a standing lamp. \n",
      "\n",
      "I kindly request that you take a moment to review the attached spec, as it contains important details about the standing lamp in question. \n",
      "\n",
      "Thank you for your time and consideration. I look forward to hearing from you soon.\n",
      "\n",
      "Sincerely,\n",
      "Joe\n"
     ]
    }
   ],
   "source": [
    "#tone transformation\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Translate the following from slang to a business letter: \n",
    "'Dude, This is Joe, check out this spec on this standing lamp.'\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "<!DOCTYPE html>\n",
      "<html>\n",
      "<head>\n",
      "<style>\n",
      "table {\n",
      "  font-family: arial, sans-serif;\n",
      "  border-collapse: collapse;\n",
      "  width: 100%;\n",
      "}\n",
      "\n",
      "td, th {\n",
      "  border: 1px solid #dddddd;\n",
      "  text-align: left;\n",
      "  padding: 8px;\n",
      "}\n",
      "\n",
      "tr:nth-child(even) {\n",
      "  background-color: #dddddd;\n",
      "}\n",
      "</style>\n",
      "</head>\n",
      "<body>\n",
      "\n",
      "<h2>Restaurant Employees</h2>\n",
      "\n",
      "<table>\n",
      "  <tr>\n",
      "    <th>Name</th>\n",
      "    <th>Email</th>\n",
      "  </tr>\n",
      "  <tr>\n",
      "    <td>Shyam</td>\n",
      "    <td>shyamjaiswal@gmail.com</td>\n",
      "  </tr>\n",
      "  <tr>\n",
      "    <td>Bob</td>\n",
      "    <td>bob32@gmail.com</td>\n",
      "  </tr>\n",
      "  <tr>\n",
      "    <td>Jai</td>\n",
      "    <td>jai87@gmail.com</td>\n",
      "  </tr>\n",
      "</table>\n",
      "\n",
      "</body>\n",
      "</html>\n"
     ]
    }
   ],
   "source": [
    "#format conversion\n",
    "\n",
    "data_json = { \"resturant employees\" :[ \n",
    "    {\"name\":\"Shyam\", \"email\":\"shyamjaiswal@gmail.com\"},\n",
    "    {\"name\":\"Bob\", \"email\":\"bob32@gmail.com\"},\n",
    "    {\"name\":\"Jai\", \"email\":\"jai87@gmail.com\"}\n",
    "]}\n",
    "\n",
    "prompt = f\"\"\"\n",
    "Translate the following python dictionary from JSON to an HTML \\\n",
    "table with column headers and title: {data_json}\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<!DOCTYPE html>\n",
       "<html>\n",
       "<head>\n",
       "<style>\n",
       "table {\n",
       "  font-family: arial, sans-serif;\n",
       "  border-collapse: collapse;\n",
       "  width: 100%;\n",
       "}\n",
       "\n",
       "td, th {\n",
       "  border: 1px solid #dddddd;\n",
       "  text-align: left;\n",
       "  padding: 8px;\n",
       "}\n",
       "\n",
       "tr:nth-child(even) {\n",
       "  background-color: #dddddd;\n",
       "}\n",
       "</style>\n",
       "</head>\n",
       "<body>\n",
       "\n",
       "<h2>Restaurant Employees</h2>\n",
       "\n",
       "<table>\n",
       "  <tr>\n",
       "    <th>Name</th>\n",
       "    <th>Email</th>\n",
       "  </tr>\n",
       "  <tr>\n",
       "    <td>Shyam</td>\n",
       "    <td>shyamjaiswal@gmail.com</td>\n",
       "  </tr>\n",
       "  <tr>\n",
       "    <td>Bob</td>\n",
       "    <td>bob32@gmail.com</td>\n",
       "  </tr>\n",
       "  <tr>\n",
       "    <td>Jai</td>\n",
       "    <td>jai87@gmail.com</td>\n",
       "  </tr>\n",
       "</table>\n",
       "\n",
       "</body>\n",
       "</html>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from IPython.display import display, Markdown, Latex, HTML,JSON\n",
    "display(HTML(response))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The girl with the black and white puppies has a ball.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "No errors found.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "No errors found.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "There goes my freedom. They're going to bring their suitcases.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "You're going to need your notebook.\n",
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "That medicine affects my ability to sleep. Have you heard of the butterfly effect?\n",
      "This phrase is to check chatGPT for spelling ability.\n"
     ]
    }
   ],
   "source": [
    "#spell and grammar check\n",
    "\n",
    "text = [ \n",
    "  \"The girl with the black and white puppies have a ball.\",  # The girl has a ball.\n",
    "  \"Yolanda has her notebook.\", # ok\n",
    "  \"Its going to be a long day. Does the car need it’s oil changed?\",  # Homonyms\n",
    "  \"Their goes my freedom. There going to bring they’re suitcases.\",  # Homonyms\n",
    "  \"Your going to need you’re notebook.\",  # Homonyms\n",
    "  \"That medicine effects my ability to sleep. Have you heard of the butterfly affect?\", # Homonyms\n",
    "  \"This phrase is to cherck chatGPT for speling abilitty\"  # spelling\n",
    "]\n",
    "for t in text:\n",
    "    prompt = f\"\"\"Proofread and correct the following text\n",
    "    and rewrite the corrected version. If you don't find\n",
    "    and errors, just say \"No errors found\". Don't use \n",
    "    any punctuation around the text:\n",
    "    ```{t}```\"\"\"\n",
    "    response = get_completion(prompt)\n",
    "    print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Got this for my daughter for her birthday because she keeps taking mine from my room. Yes, adults also like pandas too. She takes it everywhere with her, and it's super soft and cute. However, one of the ears is a bit lower than the other, and I don't think that was designed to be asymmetrical. Additionally, it's a bit small for what I paid for it. I believe there might be other options that are bigger for the same price. On the positive side, it arrived a day earlier than expected, so I got to play with it myself before I gave it to my daughter.\n"
     ]
    }
   ],
   "source": [
    "text = f\"\"\"\n",
    "Got this for my daughter for her birthday cuz she keeps taking \\\n",
    "mine from my room.  Yes, adults also like pandas too.  She takes \\\n",
    "it everywhere with her, and it's super soft and cute.  One of the \\\n",
    "ears is a bit lower than the other, and I don't think that was \\\n",
    "designed to be asymmetrical. It's a bit small for what I paid for it \\\n",
    "though. I think there might be other options that are bigger for \\\n",
    "the same price.  It arrived a day earlier than expected, so I got \\\n",
    "to play with it myself before I gave it to my daughter.\n",
    "\"\"\"\n",
    "prompt = f\"proofread and correct this review: ```{text}```\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: redlines in c:\\users\\thor0\\anaconda3\\lib\\site-packages (0.4.2)\n",
      "Requirement already satisfied: click<9.0.0,>=8.1.3 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from redlines) (8.1.7)\n",
      "Requirement already satisfied: rich<14.0.0,>=13.3.5 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from redlines) (13.7.0)\n",
      "Requirement already satisfied: rich-click<2.0.0,>=1.6.1 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from redlines) (1.7.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from click<9.0.0,>=8.1.3->redlines) (0.4.6)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from rich<14.0.0,>=13.3.5->redlines) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from rich<14.0.0,>=13.3.5->redlines) (2.17.2)\n",
      "Requirement already satisfied: typing-extensions in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from rich-click<2.0.0,>=1.6.1->redlines) (4.8.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\thor0\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14.0.0,>=13.3.5->redlines) (0.1.2)\n"
     ]
    },
    {
     "data": {
      "text/markdown": [
       "Got this for my daughter for her birthday <span style='color:red;font-weight:700;text-decoration:line-through;'>cuz </span><span style='color:green;font-weight:700;'>because </span>she keeps taking mine from my <span style='color:red;font-weight:700;text-decoration:line-through;'>room.  </span><span style='color:green;font-weight:700;'>room. </span>Yes, adults also like pandas <span style='color:red;font-weight:700;text-decoration:line-through;'>too.  </span><span style='color:green;font-weight:700;'>too. </span>She takes it everywhere with her, and it's super soft and <span style='color:red;font-weight:700;text-decoration:line-through;'>cute.  One </span><span style='color:green;font-weight:700;'>cute. However, one </span>of the ears is a bit lower than the other, and I don't think that was designed to be asymmetrical. <span style='color:red;font-weight:700;text-decoration:line-through;'>It's </span><span style='color:green;font-weight:700;'>Additionally, it's </span>a bit small for what I paid for <span style='color:red;font-weight:700;text-decoration:line-through;'>it though. </span><span style='color:green;font-weight:700;'>it. </span>I <span style='color:red;font-weight:700;text-decoration:line-through;'>think </span><span style='color:green;font-weight:700;'>believe </span>there might be other options that are bigger for the same <span style='color:red;font-weight:700;text-decoration:line-through;'>price.  It </span><span style='color:green;font-weight:700;'>price. On the positive side, it </span>arrived a day earlier than expected, so I got to play with it myself before I gave it to my daughter."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "!pip install redlines\n",
    "\n",
    "from redlines import Redlines\n",
    "\n",
    "diff = Redlines(text,response)\n",
    "display(Markdown(diff.output_markdown))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/markdown": [
       "**Title: A Delightful Gift for Panda Enthusiasts: A Review of the Soft and Adorable Panda Plush Toy**\n",
       "\n",
       "*Reviewer: [Your Name]*\n",
       "\n",
       "---\n",
       "\n",
       "I recently purchased this charming panda plush toy as a birthday gift for my daughter, who has a penchant for \"borrowing\" my belongings from time to time. As an adult, I must admit that I too have fallen under the spell of these lovable creatures. This review aims to provide an in-depth analysis of the product, catering to advanced readers who appreciate a comprehensive evaluation.\n",
       "\n",
       "First and foremost, the softness and cuteness of this panda plush toy are simply unparalleled. Its irresistibly plush exterior makes it a joy to touch and hold, ensuring a delightful sensory experience for both children and adults alike. The attention to detail is evident, with its endearing features capturing the essence of a real panda. However, it is worth noting that one of the ears appears to be slightly asymmetrical, which may not have been an intentional design choice.\n",
       "\n",
       "While the overall quality of the product is commendable, I must express my slight disappointment regarding its size in relation to its price. Considering the investment made, I expected a larger plush toy. It is worth exploring alternative options that offer a more substantial size without compromising on the price point. Nevertheless, the undeniable charm and softness of this panda plush toy compensate for its relatively smaller dimensions.\n",
       "\n",
       "In terms of delivery, I was pleasantly surprised to receive the product a day earlier than anticipated. This unexpected early arrival allowed me to indulge in some personal playtime with the panda plush toy before presenting it to my daughter. This added bonus further enhanced my overall satisfaction with the purchase.\n",
       "\n",
       "In conclusion, this panda plush toy is a delightful gift for both children and adults who appreciate the enchanting allure of these beloved creatures. Its softness, cuteness, and attention to detail make it a truly captivating addition to any collection. While the size may not fully justify the price, the overall quality and timely delivery contribute to a positive purchasing experience. For those seeking a charming and huggable companion, this panda plush toy is sure to bring joy and comfort to its lucky recipient.\n",
       "\n",
       "---\n",
       "\n",
       "**References**\n",
       "\n",
       "*Please note that APA style does not require references for personal reviews."
      ],
      "text/plain": [
       "<IPython.core.display.Markdown object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "proofread and correct this review. Make it more compelling. \n",
    "Ensure it follows APA style guide and targets an advanced reader. \n",
    "Output in markdown format.\n",
    "Text: ```{text}```\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "display(Markdown(response))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "#expanding\n",
    "\n",
    "#customizing automated reply to customer email\n",
    "\n",
    "# given the sentiment from the lesson on \"inferring\",\n",
    "# and the original customer message, customize the email\n",
    "sentiment = \"negative\"\n",
    "\n",
    "# review for a blender\n",
    "review = f\"\"\"\n",
    "So, they still had the 17 piece system on seasonal \\\n",
    "sale for around $49 in the month of November, about \\\n",
    "half off, but for some reason (call it price gouging) \\\n",
    "around the second week of December the prices all went \\\n",
    "up to about anywhere from between $70-$89 for the same \\\n",
    "system. And the 11 piece system went up around $10 or \\\n",
    "so in price also from the earlier sale price of $29. \\\n",
    "So it looks okay, but if you look at the base, the part \\\n",
    "where the blade locks into place doesn’t look as good \\\n",
    "as in previous editions from a few years ago, but I \\\n",
    "plan to be very gentle with it (example, I crush \\\n",
    "very hard items like beans, ice, rice, etc. in the \\ \n",
    "blender first then pulverize them in the serving size \\\n",
    "I want in the blender then switch to the whipping \\\n",
    "blade for a finer flour, and use the cross cutting blade \\\n",
    "first when making smoothies, then use the flat blade \\\n",
    "if I need them finer/less pulpy). Special tip when making \\\n",
    "smoothies, finely cut and freeze the fruits and \\\n",
    "vegetables (if using spinach-lightly stew soften the \\ \n",
    "spinach then freeze until ready for use-and if making \\\n",
    "sorbet, use a small to medium sized food processor) \\ \n",
    "that you plan to use that way you can avoid adding so \\\n",
    "much ice if at all-when making your smoothie. \\\n",
    "After about a year, the motor was making a funny noise. \\\n",
    "I called customer service but the warranty expired \\\n",
    "already, so I had to buy another one. FYI: The overall \\\n",
    "quality has gone done in these types of products, so \\\n",
    "they are kind of counting on brand recognition and \\\n",
    "consumer loyalty to maintain sales. Got it in about \\\n",
    "two days.\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dear Valued Customer,\n",
      "\n",
      "Thank you for taking the time to share your review with us. We appreciate your feedback and apologize for any inconvenience you may have experienced.\n",
      "\n",
      "We are sorry to hear about the price increase you noticed in December. We strive to provide competitive pricing for our products, and we understand your frustration. If you have any further concerns regarding pricing, we recommend reaching out to our customer service team who will be happy to assist you.\n",
      "\n",
      "We also appreciate your feedback regarding the base of the system. We continuously work to improve the quality of our products, and your comments will be taken into consideration for future enhancements.\n",
      "\n",
      "Regarding the motor issue you encountered, we apologize for any inconvenience caused. Our customer service team is available to assist you with any technical difficulties you may encounter, even if the warranty has expired. Please do not hesitate to reach out to them for further assistance.\n",
      "\n",
      "Thank you once again for your review. We value your loyalty and appreciate your support. If you have any further questions or concerns, please feel free to contact our customer service team.\n",
      "\n",
      "Best regards,\n",
      "\n",
      "AI customer agent\n"
     ]
    }
   ],
   "source": [
    "prompt = f\"\"\"\n",
    "You are a customer service AI assistant.\n",
    "Your task is to send an email reply to a valued customer.\n",
    "Given the customer email delimited by ```, \\\n",
    "Generate a reply to thank the customer for their review.\n",
    "If the sentiment is positive or neutral, thank them for \\\n",
    "their review.\n",
    "If the sentiment is negative, apologize and suggest that \\\n",
    "they can reach out to customer service. \n",
    "Make sure to use specific details from the review.\n",
    "Write in a concise and professional tone.\n",
    "Sign the email as `AI customer agent`.\n",
    "Customer review: ```{review}```\n",
    "Review sentiment: {sentiment}\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rate limit reached. Waiting for 20 seconds. Error: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.\n",
      "Dear Valued Customer,\n",
      "\n",
      "Thank you for taking the time to share your review with us. We appreciate your feedback and apologize for any inconvenience you may have experienced.\n",
      "\n",
      "We are sorry to hear about the price increase you noticed in December. We strive to provide competitive pricing for our products, and we understand your frustration. If you have any further concerns regarding pricing, we recommend reaching out to our customer service team who will be happy to assist you.\n",
      "\n",
      "We also appreciate your feedback regarding the base of the system. We continuously work to improve the quality of our products, and your comments will be taken into consideration for future enhancements.\n",
      "\n",
      "Regarding the motor issue you encountered, we apologize for any inconvenience caused. Our customer service team is available to assist you with any technical difficulties you may encounter, even if the warranty has expired. Please do not hesitate to reach out to them for further assistance.\n",
      "\n",
      "Thank you once again for your review. We value your loyalty and appreciate your support. If you have any further questions or concerns, please feel free to contact our customer service team.\n",
      "\n",
      "Best regards,\n",
      "\n",
      "AI customer agent\n"
     ]
    }
   ],
   "source": [
    "#reminding the model to use details from the customer email\n",
    "\n",
    "prompt = f\"\"\"\n",
    "You are a customer service AI assistant.\n",
    "Your task is to send an email reply to a valued customer.\n",
    "Given the customer email delimited by ```, \\\n",
    "Generate a reply to thank the customer for their review.\n",
    "If the sentiment is positive or neutral, thank them for \\\n",
    "their review.\n",
    "If the sentiment is negative, apologize and suggest that \\\n",
    "they can reach out to customer service. \n",
    "Make sure to use specific details from the review.\n",
    "Write in a concise and professional tone.\n",
    "Sign the email as `AI customer agent`.\n",
    "Customer review: ```{review}```\n",
    "Review sentiment: {sentiment}\n",
    "\"\"\"\n",
    "response = get_completion(prompt)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_completion_from_messages(messages, model=\"gpt-3.5-turbo\", temperature=0):\n",
    "    while True:\n",
    "        try:\n",
    "            response = openai.ChatCompletion.create(\n",
    "                model=model,\n",
    "                messages=messages,\n",
    "                temperature=temperature,\n",
    "            )\n",
    "            return response.choices[0].message[\"content\"]\n",
    "        except openai.error.RateLimitError as e:\n",
    "            # Handle rate-limiting error\n",
    "            print(f\"Rate limit reached. Waiting for 20 seconds. Error: {e}\")\n",
    "            time.sleep(20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Because it had an egg-cellent sense of timing!\n"
     ]
    },
    {
     "ename": "RateLimitError",
     "evalue": "Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRateLimitError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[64], line 25\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[38;5;28mprint\u001b[39m(response)\n\u001b[0;32m     22\u001b[0m messages \u001b[38;5;241m=\u001b[39m  [  \n\u001b[0;32m     23\u001b[0m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrole\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124msystem\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mYou are friendly chatbot.\u001b[39m\u001b[38;5;124m'\u001b[39m},    \n\u001b[0;32m     24\u001b[0m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrole\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124muser\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mHi, my name is gowtham\u001b[39m\u001b[38;5;124m'\u001b[39m}  ]\n\u001b[1;32m---> 25\u001b[0m response \u001b[38;5;241m=\u001b[39m \u001b[43mget_completion_from_messages\u001b[49m\u001b[43m(\u001b[49m\u001b[43mmessages\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtemperature\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;241;43m1\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     26\u001b[0m \u001b[38;5;28mprint\u001b[39m(response)\n\u001b[0;32m     28\u001b[0m messages \u001b[38;5;241m=\u001b[39m [\n\u001b[0;32m     29\u001b[0m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrole\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124msystem\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m'\u001b[39m: \u001b[38;5;124m'\u001b[39m\u001b[38;5;124myou are a friendly chatbot\u001b[39m\u001b[38;5;124m'\u001b[39m},\n\u001b[0;32m     30\u001b[0m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrole\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124muser\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124myes, can u remind me, who am i?\u001b[39m\u001b[38;5;124m'\u001b[39m} ]\n",
      "Cell \u001b[1;32mIn[64], line 4\u001b[0m, in \u001b[0;36mget_completion_from_messages\u001b[1;34m(messages, model, temperature)\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_completion_from_messages\u001b[39m(messages, model \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgpt-3.5-turbo\u001b[39m\u001b[38;5;124m\"\u001b[39m, temperature\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m):\n\u001b[1;32m----> 4\u001b[0m     response \u001b[38;5;241m=\u001b[39m \u001b[43mopenai\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mChatCompletion\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcreate\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m      5\u001b[0m \u001b[43m        \u001b[49m\u001b[43mmodel\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mmodel\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m      6\u001b[0m \u001b[43m        \u001b[49m\u001b[43mmessages\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mmessages\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m      7\u001b[0m \u001b[43m        \u001b[49m\u001b[43mtemperature\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43m \u001b[49m\u001b[43mtemperature\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;66;43;03m#degree of randomness pf model's output\u001b[39;49;00m\n\u001b[0;32m      8\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m     10\u001b[0m   \u001b[38;5;66;03m#  print(str(response.choices[0].message))\u001b[39;00m\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m response\u001b[38;5;241m.\u001b[39mchoices[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m.\u001b[39mmessage[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcontent\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n",
      "File \u001b[1;32mc:\\Users\\thor0\\anaconda3\\lib\\site-packages\\openai\\api_resources\\chat_completion.py:25\u001b[0m, in \u001b[0;36mChatCompletion.create\u001b[1;34m(cls, *args, **kwargs)\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28;01mTrue\u001b[39;00m:\n\u001b[0;32m     24\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m---> 25\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28msuper\u001b[39m()\u001b[38;5;241m.\u001b[39mcreate(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n\u001b[0;32m     26\u001b[0m     \u001b[38;5;28;01mexcept\u001b[39;00m TryAgain \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[0;32m     27\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m timeout \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m time\u001b[38;5;241m.\u001b[39mtime() \u001b[38;5;241m>\u001b[39m start \u001b[38;5;241m+\u001b[39m timeout:\n",
      "File \u001b[1;32mc:\\Users\\thor0\\anaconda3\\lib\\site-packages\\openai\\api_resources\\abstract\\engine_api_resource.py:153\u001b[0m, in \u001b[0;36mEngineAPIResource.create\u001b[1;34m(cls, api_key, api_base, api_type, request_id, api_version, organization, **params)\u001b[0m\n\u001b[0;32m    127\u001b[0m \u001b[38;5;129m@classmethod\u001b[39m\n\u001b[0;32m    128\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcreate\u001b[39m(\n\u001b[0;32m    129\u001b[0m     \u001b[38;5;28mcls\u001b[39m,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    136\u001b[0m     \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mparams,\n\u001b[0;32m    137\u001b[0m ):\n\u001b[0;32m    138\u001b[0m     (\n\u001b[0;32m    139\u001b[0m         deployment_id,\n\u001b[0;32m    140\u001b[0m         engine,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    150\u001b[0m         api_key, api_base, api_type, api_version, organization, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mparams\n\u001b[0;32m    151\u001b[0m     )\n\u001b[1;32m--> 153\u001b[0m     response, _, api_key \u001b[38;5;241m=\u001b[39m \u001b[43mrequestor\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrequest\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    154\u001b[0m \u001b[43m        \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mpost\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[0;32m    155\u001b[0m \u001b[43m        \u001b[49m\u001b[43murl\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    156\u001b[0m \u001b[43m        \u001b[49m\u001b[43mparams\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mparams\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    157\u001b[0m \u001b[43m        \u001b[49m\u001b[43mheaders\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    158\u001b[0m \u001b[43m        \u001b[49m\u001b[43mstream\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mstream\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    159\u001b[0m \u001b[43m        \u001b[49m\u001b[43mrequest_id\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest_id\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    160\u001b[0m \u001b[43m        \u001b[49m\u001b[43mrequest_timeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrequest_timeout\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    161\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    163\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m stream:\n\u001b[0;32m    164\u001b[0m         \u001b[38;5;66;03m# must be an iterator\u001b[39;00m\n\u001b[0;32m    165\u001b[0m         \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(response, OpenAIResponse)\n",
      "File \u001b[1;32mc:\\Users\\thor0\\anaconda3\\lib\\site-packages\\openai\\api_requestor.py:298\u001b[0m, in \u001b[0;36mAPIRequestor.request\u001b[1;34m(self, method, url, params, headers, files, stream, request_id, request_timeout)\u001b[0m\n\u001b[0;32m    277\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mrequest\u001b[39m(\n\u001b[0;32m    278\u001b[0m     \u001b[38;5;28mself\u001b[39m,\n\u001b[0;32m    279\u001b[0m     method,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    286\u001b[0m     request_timeout: Optional[Union[\u001b[38;5;28mfloat\u001b[39m, Tuple[\u001b[38;5;28mfloat\u001b[39m, \u001b[38;5;28mfloat\u001b[39m]]] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[0;32m    287\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Tuple[Union[OpenAIResponse, Iterator[OpenAIResponse]], \u001b[38;5;28mbool\u001b[39m, \u001b[38;5;28mstr\u001b[39m]:\n\u001b[0;32m    288\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mrequest_raw(\n\u001b[0;32m    289\u001b[0m         method\u001b[38;5;241m.\u001b[39mlower(),\n\u001b[0;32m    290\u001b[0m         url,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    296\u001b[0m         request_timeout\u001b[38;5;241m=\u001b[39mrequest_timeout,\n\u001b[0;32m    297\u001b[0m     )\n\u001b[1;32m--> 298\u001b[0m     resp, got_stream \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_interpret_response\u001b[49m\u001b[43m(\u001b[49m\u001b[43mresult\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mstream\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    299\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m resp, got_stream, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapi_key\n",
      "File \u001b[1;32mc:\\Users\\thor0\\anaconda3\\lib\\site-packages\\openai\\api_requestor.py:700\u001b[0m, in \u001b[0;36mAPIRequestor._interpret_response\u001b[1;34m(self, result, stream)\u001b[0m\n\u001b[0;32m    692\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m (\n\u001b[0;32m    693\u001b[0m         \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_interpret_response_line(\n\u001b[0;32m    694\u001b[0m             line, result\u001b[38;5;241m.\u001b[39mstatus_code, result\u001b[38;5;241m.\u001b[39mheaders, stream\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[0;32m    695\u001b[0m         )\n\u001b[0;32m    696\u001b[0m         \u001b[38;5;28;01mfor\u001b[39;00m line \u001b[38;5;129;01min\u001b[39;00m parse_stream(result\u001b[38;5;241m.\u001b[39miter_lines())\n\u001b[0;32m    697\u001b[0m     ), \u001b[38;5;28;01mTrue\u001b[39;00m\n\u001b[0;32m    698\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    699\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m (\n\u001b[1;32m--> 700\u001b[0m         \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_interpret_response_line\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    701\u001b[0m \u001b[43m            \u001b[49m\u001b[43mresult\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mcontent\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdecode\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mutf-8\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    702\u001b[0m \u001b[43m            \u001b[49m\u001b[43mresult\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mstatus_code\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    703\u001b[0m \u001b[43m            \u001b[49m\u001b[43mresult\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mheaders\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    704\u001b[0m \u001b[43m            \u001b[49m\u001b[43mstream\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m,\u001b[49m\n\u001b[0;32m    705\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m,\n\u001b[0;32m    706\u001b[0m         \u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[0;32m    707\u001b[0m     )\n",
      "File \u001b[1;32mc:\\Users\\thor0\\anaconda3\\lib\\site-packages\\openai\\api_requestor.py:765\u001b[0m, in \u001b[0;36mAPIRequestor._interpret_response_line\u001b[1;34m(self, rbody, rcode, rheaders, stream)\u001b[0m\n\u001b[0;32m    763\u001b[0m stream_error \u001b[38;5;241m=\u001b[39m stream \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124merror\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01min\u001b[39;00m resp\u001b[38;5;241m.\u001b[39mdata\n\u001b[0;32m    764\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m stream_error \u001b[38;5;129;01mor\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;241m200\u001b[39m \u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39m rcode \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m300\u001b[39m:\n\u001b[1;32m--> 765\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandle_error_response(\n\u001b[0;32m    766\u001b[0m         rbody, rcode, resp\u001b[38;5;241m.\u001b[39mdata, rheaders, stream_error\u001b[38;5;241m=\u001b[39mstream_error\n\u001b[0;32m    767\u001b[0m     )\n\u001b[0;32m    768\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m resp\n",
      "\u001b[1;31mRateLimitError\u001b[0m: Rate limit reached for gpt-3.5-turbo in organization org-ifKfb3706mMs6lyQ6ImbeXTl on requests per min (RPM): Limit 3, Used 3, Requested 1. Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing."
     ]
    }
   ],
   "source": [
    "#the chatbot\n",
    "\n",
    "def get_completion_from_messages(messages, model = \"gpt-3.5-turbo\", temperature=0):\n",
    "    response = openai.ChatCompletion.create(\n",
    "        model = model,\n",
    "        messages = messages,\n",
    "        temperature = temperature, #degree of randomness pf model's output\n",
    "    )\n",
    "\n",
    "  #  print(str(response.choices[0].message))\n",
    "    return response.choices[0].message[\"content\"]\n",
    "\n",
    "messages = [\n",
    "{'role':'system', 'content':'you are an assistant that speaks like stephen hawking.'},\n",
    "{'role':'user', 'content':'tell me a joke '},\n",
    "{'role': 'assistant', 'content': 'why did chicken came first'},\n",
    "{'role':'user', 'content': 'i dont know'} ]\n",
    "\n",
    "response = get_completion_from_messages(messages, temperature=1)\n",
    "print(response)\n",
    "\n",
    "messages =  [  \n",
    "{'role':'system', 'content':'You are friendly chatbot.'},    \n",
    "{'role':'user', 'content':'Hi, my name is gowtham'}  ]\n",
    "response = get_completion_from_messages(messages, temperature=1)\n",
    "print(response)\n",
    "\n",
    "messages = [\n",
    "{'role':'system', 'content': 'you are a friendly chatbot'},\n",
    "{'role':'user', 'content':'yes, can u remind me, who am i?'} ]\n",
    "response = get_completion_from_messages(messages, temperature=1)\n",
    "print(response)    \n",
    "\n",
    "\n",
    "\n",
    "messages = [ {'role':'system', 'content':'You are friendly chatbot.'},\n",
    "{'role':'user', 'content':'Hi, my name is Isa'},\n",
    "{'role':'assistant', 'content': \"Hi Isa! It's nice to meet you. \\\n",
    "Is there anything I can help you with today?\"},\n",
    "{'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]\n",
    "response = get_completion_from_messages(messages, temperature=1)\n",
    "print(response)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "#orderbot of an pizza restaurant \n",
    "\n",
    "def collect_messages(_):\n",
    "    prompt = inp.value_input\n",
    "    inp.value = ''\n",
    "    context.append({'role':'user', 'content':f\"{prompt}\"})\n",
    "    response = get_completion_from_messages(context) \n",
    "    context.append({'role':'assistant', 'content':f\"{response}\"})\n",
    "    panels.append(\n",
    "        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))\n",
    "    panels.append(\n",
    "        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))\n",
    " \n",
    "    return pn.Column(*panels)\n",
    "\n",
    "                    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": "(function(root) {\n  function now() {\n    return new Date();\n  }\n\n  var force = true;\n\n  if (typeof root._bokeh_onload_callbacks === \"undefined\" || force === true) {\n    root._bokeh_onload_callbacks = [];\n    root._bokeh_is_loading = undefined;\n  }\n\n  if (typeof (root._bokeh_timeout) === \"undefined\" || force === true) {\n    root._bokeh_timeout = Date.now() + 5000;\n    root._bokeh_failed_load = false;\n  }\n\n  function run_callbacks() {\n    try {\n      root._bokeh_onload_callbacks.forEach(function(callback) {\n        if (callback != null)\n          callback();\n      });\n    } finally {\n      delete root._bokeh_onload_callbacks\n    }\n    console.debug(\"Bokeh: all callbacks have finished\");\n  }\n\n  function load_libs(css_urls, js_urls, js_modules, callback) {\n    if (css_urls == null) css_urls = [];\n    if (js_urls == null) js_urls = [];\n    if (js_modules == null) js_modules = [];\n\n    root._bokeh_onload_callbacks.push(callback);\n    if (root._bokeh_is_loading > 0) {\n      console.debug(\"Bokeh: BokehJS is being loaded, scheduling callback at\", now());\n      return null;\n    }\n    if (js_urls.length === 0 && js_modules.length === 0) {\n      run_callbacks();\n      return null;\n    }\n    console.debug(\"Bokeh: BokehJS not loaded, scheduling load and callback at\", now());\n\n    function on_load() {\n      root._bokeh_is_loading--;\n      if (root._bokeh_is_loading === 0) {\n        console.debug(\"Bokeh: all BokehJS libraries/stylesheets loaded\");\n        run_callbacks()\n      }\n    }\n\n    function on_error() {\n      console.error(\"failed to load \" + url);\n    }\n\n    for (var i = 0; i < css_urls.length; i++) {\n      var url = css_urls[i];\n      const element = document.createElement(\"link\");\n      element.onload = on_load;\n      element.onerror = on_error;\n      element.rel = \"stylesheet\";\n      element.type = \"text/css\";\n      element.href = url;\n      console.debug(\"Bokeh: injecting link tag for BokehJS stylesheet: \", url);\n      document.body.appendChild(element);\n    }\n\n    var skip = [];\n    if (window.requirejs) {\n      window.requirejs.config({'packages': {}, 'paths': {'gridstack': 'https://cdn.jsdelivr.net/npm/gridstack@4.2.5/dist/gridstack-h5', 'notyf': 'https://cdn.jsdelivr.net/npm/notyf@3/notyf.min'}, 'shim': {'gridstack': {'exports': 'GridStack'}}});\n      require([\"gridstack\"], function(GridStack) {\n\twindow.GridStack = GridStack\n\ton_load()\n      })\n      require([\"notyf\"], function() {\n\ton_load()\n      })\n      root._bokeh_is_loading = css_urls.length + 2;\n    } else {\n      root._bokeh_is_loading = css_urls.length + js_urls.length + js_modules.length;\n    }    if (((window['GridStack'] !== undefined) && (!(window['GridStack'] instanceof HTMLElement))) || window.requirejs) {\n      var urls = ['https://cdn.holoviz.org/panel/0.14.3/dist/bundled/gridstack/gridstack@4.2.5/dist/gridstack-h5.js'];\n      for (var i = 0; i < urls.length; i++) {\n        skip.push(urls[i])\n      }\n    }    if (((window['Notyf'] !== undefined) && (!(window['Notyf'] instanceof HTMLElement))) || window.requirejs) {\n      var urls = ['https://cdn.holoviz.org/panel/0.14.3/dist/bundled/notificationarea/notyf@3/notyf.min.js'];\n      for (var i = 0; i < urls.length; i++) {\n        skip.push(urls[i])\n      }\n    }    for (var i = 0; i < js_urls.length; i++) {\n      var url = js_urls[i];\n      if (skip.indexOf(url) >= 0) {\n\tif (!window.requirejs) {\n\t  on_load();\n\t}\n\tcontinue;\n      }\n      var element = document.createElement('script');\n      element.onload = on_load;\n      element.onerror = on_error;\n      element.async = false;\n      element.src = url;\n      console.debug(\"Bokeh: injecting script tag for BokehJS library: \", url);\n      document.head.appendChild(element);\n    }\n    for (var i = 0; i < js_modules.length; i++) {\n      var url = js_modules[i];\n      if (skip.indexOf(url) >= 0) {\n\tif (!window.requirejs) {\n\t  on_load();\n\t}\n\tcontinue;\n      }\n      var element = document.createElement('script');\n      element.onload = on_load;\n      element.onerror = on_error;\n      element.async = false;\n      element.src = url;\n      element.type = \"module\";\n      console.debug(\"Bokeh: injecting script tag for BokehJS library: \", url);\n      document.head.appendChild(element);\n    }\n    if (!js_urls.length && !js_modules.length) {\n      on_load()\n    }\n  };\n\n  function inject_raw_css(css) {\n    const element = document.createElement(\"style\");\n    element.appendChild(document.createTextNode(css));\n    document.body.appendChild(element);\n  }\n\n  var js_urls = [\"https://cdn.bokeh.org/bokeh/release/bokeh-2.4.3.min.js\", \"https://cdn.bokeh.org/bokeh/release/bokeh-gl-2.4.3.min.js\", \"https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.3.min.js\", \"https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.4.3.min.js\", \"https://cdn.bokeh.org/bokeh/release/bokeh-mathjax-2.4.3.min.js\", \"https://unpkg.com/@holoviz/panel@0.14.3/dist/panel.min.js\"];\n  var js_modules = [];\n  var css_urls = [\"https://cdn.holoviz.org/panel/0.14.3/dist/css/alerts.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/card.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/dataframe.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/debugger.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/json.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/loading.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/markdown.css\", \"https://cdn.holoviz.org/panel/0.14.3/dist/css/widgets.css\"];\n  var inline_js = [    function(Bokeh) {\n      inject_raw_css(\"\\n    .bk.pn-loading.arc:before {\\n      background-image: url(\\\"data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJtYXJnaW46IGF1dG87IGJhY2tncm91bmQ6IG5vbmU7IGRpc3BsYXk6IGJsb2NrOyBzaGFwZS1yZW5kZXJpbmc6IGF1dG87IiB2aWV3Qm94PSIwIDAgMTAwIDEwMCIgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQiPiAgPGNpcmNsZSBjeD0iNTAiIGN5PSI1MCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjYzNjM2MzIiBzdHJva2Utd2lkdGg9IjEwIiByPSIzNSIgc3Ryb2tlLWRhc2hhcnJheT0iMTY0LjkzMzYxNDMxMzQ2NDE1IDU2Ljk3Nzg3MTQzNzgyMTM4Ij4gICAgPGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJyb3RhdGUiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIiBkdXI9IjFzIiB2YWx1ZXM9IjAgNTAgNTA7MzYwIDUwIDUwIiBrZXlUaW1lcz0iMDsxIj48L2FuaW1hdGVUcmFuc2Zvcm0+ICA8L2NpcmNsZT48L3N2Zz4=\\\");\\n      background-size: auto calc(min(50%, 400px));\\n    }\\n    \");\n    },    function(Bokeh) {\n      Bokeh.set_log_level(\"info\");\n    },\nfunction(Bokeh) {} // ensure no trailing comma for IE\n  ];\n\n  function run_inline_js() {\n    if ((root.Bokeh !== undefined) || (force === true)) {\n      for (var i = 0; i < inline_js.length; i++) {\n        inline_js[i].call(root, root.Bokeh);\n      }} else if (Date.now() < root._bokeh_timeout) {\n      setTimeout(run_inline_js, 100);\n    } else if (!root._bokeh_failed_load) {\n      console.log(\"Bokeh: BokehJS failed to load within specified timeout.\");\n      root._bokeh_failed_load = true;\n    }\n  }\n\n  if (root._bokeh_is_loading === 0) {\n    console.debug(\"Bokeh: BokehJS loaded, going straight to plotting\");\n    run_inline_js();\n  } else {\n    load_libs(css_urls, js_urls, js_modules, function() {\n      console.debug(\"Bokeh: BokehJS plotting callback run at\", now());\n      run_inline_js();\n    });\n  }\n}(window));",
      "application/vnd.holoviews_load.v0+json": ""
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": "\nif ((window.PyViz === undefined) || (window.PyViz instanceof HTMLElement)) {\n  window.PyViz = {comms: {}, comm_status:{}, kernels:{}, receivers: {}, plot_index: []}\n}\n\n\n    function JupyterCommManager() {\n    }\n\n    JupyterCommManager.prototype.register_target = function(plot_id, comm_id, msg_handler) {\n      if (window.comm_manager || ((window.Jupyter !== undefined) && (Jupyter.notebook.kernel != null))) {\n        var comm_manager = window.comm_manager || Jupyter.notebook.kernel.comm_manager;\n        comm_manager.register_target(comm_id, function(comm) {\n          comm.on_msg(msg_handler);\n        });\n      } else if ((plot_id in window.PyViz.kernels) && (window.PyViz.kernels[plot_id])) {\n        window.PyViz.kernels[plot_id].registerCommTarget(comm_id, function(comm) {\n          comm.onMsg = msg_handler;\n        });\n      } else if (typeof google != 'undefined' && google.colab.kernel != null) {\n        google.colab.kernel.comms.registerTarget(comm_id, (comm) => {\n          var messages = comm.messages[Symbol.asyncIterator]();\n          function processIteratorResult(result) {\n            var message = result.value;\n            console.log(message)\n            var content = {data: message.data, comm_id};\n            var buffers = []\n            for (var buffer of message.buffers || []) {\n              buffers.push(new DataView(buffer))\n            }\n            var metadata = message.metadata || {};\n            var msg = {content, buffers, metadata}\n            msg_handler(msg);\n            return messages.next().then(processIteratorResult);\n          }\n          return messages.next().then(processIteratorResult);\n        })\n      }\n    }\n\n    JupyterCommManager.prototype.get_client_comm = function(plot_id, comm_id, msg_handler) {\n      if (comm_id in window.PyViz.comms) {\n        return window.PyViz.comms[comm_id];\n      } else if (window.comm_manager || ((window.Jupyter !== undefined) && (Jupyter.notebook.kernel != null))) {\n        var comm_manager = window.comm_manager || Jupyter.notebook.kernel.comm_manager;\n        var comm = comm_manager.new_comm(comm_id, {}, {}, {}, comm_id);\n        if (msg_handler) {\n          comm.on_msg(msg_handler);\n        }\n      } else if ((plot_id in window.PyViz.kernels) && (window.PyViz.kernels[plot_id])) {\n        var comm = window.PyViz.kernels[plot_id].connectToComm(comm_id);\n        comm.open();\n        if (msg_handler) {\n          comm.onMsg = msg_handler;\n        }\n      } else if (typeof google != 'undefined' && google.colab.kernel != null) {\n        var comm_promise = google.colab.kernel.comms.open(comm_id)\n        comm_promise.then((comm) => {\n          window.PyViz.comms[comm_id] = comm;\n          if (msg_handler) {\n            var messages = comm.messages[Symbol.asyncIterator]();\n            function processIteratorResult(result) {\n              var message = result.value;\n              var content = {data: message.data};\n              var metadata = message.metadata || {comm_id};\n              var msg = {content, metadata}\n              msg_handler(msg);\n              return messages.next().then(processIteratorResult);\n            }\n            return messages.next().then(processIteratorResult);\n          }\n        }) \n        var sendClosure = (data, metadata, buffers, disposeOnDone) => {\n          return comm_promise.then((comm) => {\n            comm.send(data, metadata, buffers, disposeOnDone);\n          });\n        };\n        var comm = {\n          send: sendClosure\n        };\n      }\n      window.PyViz.comms[comm_id] = comm;\n      return comm;\n    }\n    window.PyViz.comm_manager = new JupyterCommManager();\n    \n\n\nvar JS_MIME_TYPE = 'application/javascript';\nvar HTML_MIME_TYPE = 'text/html';\nvar EXEC_MIME_TYPE = 'application/vnd.holoviews_exec.v0+json';\nvar CLASS_NAME = 'output';\n\n/**\n * Render data to the DOM node\n */\nfunction render(props, node) {\n  var div = document.createElement(\"div\");\n  var script = document.createElement(\"script\");\n  node.appendChild(div);\n  node.appendChild(script);\n}\n\n/**\n * Handle when a new output is added\n */\nfunction handle_add_output(event, handle) {\n  var output_area = handle.output_area;\n  var output = handle.output;\n  if ((output.data == undefined) || (!output.data.hasOwnProperty(EXEC_MIME_TYPE))) {\n    return\n  }\n  var id = output.metadata[EXEC_MIME_TYPE][\"id\"];\n  var toinsert = output_area.element.find(\".\" + CLASS_NAME.split(' ')[0]);\n  if (id !== undefined) {\n    var nchildren = toinsert.length;\n    var html_node = toinsert[nchildren-1].children[0];\n    html_node.innerHTML = output.data[HTML_MIME_TYPE];\n    var scripts = [];\n    var nodelist = html_node.querySelectorAll(\"script\");\n    for (var i in nodelist) {\n      if (nodelist.hasOwnProperty(i)) {\n        scripts.push(nodelist[i])\n      }\n    }\n\n    scripts.forEach( function (oldScript) {\n      var newScript = document.createElement(\"script\");\n      var attrs = [];\n      var nodemap = oldScript.attributes;\n      for (var j in nodemap) {\n        if (nodemap.hasOwnProperty(j)) {\n          attrs.push(nodemap[j])\n        }\n      }\n      attrs.forEach(function(attr) { newScript.setAttribute(attr.name, attr.value) });\n      newScript.appendChild(document.createTextNode(oldScript.innerHTML));\n      oldScript.parentNode.replaceChild(newScript, oldScript);\n    });\n    if (JS_MIME_TYPE in output.data) {\n      toinsert[nchildren-1].children[1].textContent = output.data[JS_MIME_TYPE];\n    }\n    output_area._hv_plot_id = id;\n    if ((window.Bokeh !== undefined) && (id in Bokeh.index)) {\n      window.PyViz.plot_index[id] = Bokeh.index[id];\n    } else {\n      window.PyViz.plot_index[id] = null;\n    }\n  } else if (output.metadata[EXEC_MIME_TYPE][\"server_id\"] !== undefined) {\n    var bk_div = document.createElement(\"div\");\n    bk_div.innerHTML = output.data[HTML_MIME_TYPE];\n    var script_attrs = bk_div.children[0].attributes;\n    for (var i = 0; i < script_attrs.length; i++) {\n      toinsert[toinsert.length - 1].childNodes[1].setAttribute(script_attrs[i].name, script_attrs[i].value);\n    }\n    // store reference to server id on output_area\n    output_area._bokeh_server_id = output.metadata[EXEC_MIME_TYPE][\"server_id\"];\n  }\n}\n\n/**\n * Handle when an output is cleared or removed\n */\nfunction handle_clear_output(event, handle) {\n  var id = handle.cell.output_area._hv_plot_id;\n  var server_id = handle.cell.output_area._bokeh_server_id;\n  if (((id === undefined) || !(id in PyViz.plot_index)) && (server_id !== undefined)) { return; }\n  var comm = window.PyViz.comm_manager.get_client_comm(\"hv-extension-comm\", \"hv-extension-comm\", function () {});\n  if (server_id !== null) {\n    comm.send({event_type: 'server_delete', 'id': server_id});\n    return;\n  } else if (comm !== null) {\n    comm.send({event_type: 'delete', 'id': id});\n  }\n  delete PyViz.plot_index[id];\n  if ((window.Bokeh !== undefined) & (id in window.Bokeh.index)) {\n    var doc = window.Bokeh.index[id].model.document\n    doc.clear();\n    const i = window.Bokeh.documents.indexOf(doc);\n    if (i > -1) {\n      window.Bokeh.documents.splice(i, 1);\n    }\n  }\n}\n\n/**\n * Handle kernel restart event\n */\nfunction handle_kernel_cleanup(event, handle) {\n  delete PyViz.comms[\"hv-extension-comm\"];\n  window.PyViz.plot_index = {}\n}\n\n/**\n * Handle update_display_data messages\n */\nfunction handle_update_output(event, handle) {\n  handle_clear_output(event, {cell: {output_area: handle.output_area}})\n  handle_add_output(event, handle)\n}\n\nfunction register_renderer(events, OutputArea) {\n  function append_mime(data, metadata, element) {\n    // create a DOM node to render to\n    var toinsert = this.create_output_subarea(\n    metadata,\n    CLASS_NAME,\n    EXEC_MIME_TYPE\n    );\n    this.keyboard_manager.register_events(toinsert);\n    // Render to node\n    var props = {data: data, metadata: metadata[EXEC_MIME_TYPE]};\n    render(props, toinsert[0]);\n    element.append(toinsert);\n    return toinsert\n  }\n\n  events.on('output_added.OutputArea', handle_add_output);\n  events.on('output_updated.OutputArea', handle_update_output);\n  events.on('clear_output.CodeCell', handle_clear_output);\n  events.on('delete.Cell', handle_clear_output);\n  events.on('kernel_ready.Kernel', handle_kernel_cleanup);\n\n  OutputArea.prototype.register_mime_type(EXEC_MIME_TYPE, append_mime, {\n    safe: true,\n    index: 0\n  });\n}\n\nif (window.Jupyter !== undefined) {\n  try {\n    var events = require('base/js/events');\n    var OutputArea = require('notebook/js/outputarea').OutputArea;\n    if (OutputArea.prototype.mime_types().indexOf(EXEC_MIME_TYPE) == -1) {\n      register_renderer(events, OutputArea);\n    }\n  } catch(err) {\n  }\n}\n",
      "application/vnd.holoviews_load.v0+json": ""
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<style>.bk-root, .bk-root .bk:before, .bk-root .bk:after {\n",
       "  font-family: var(--jp-ui-font-size1);\n",
       "  font-size: var(--jp-ui-font-size1);\n",
       "  color: var(--jp-ui-font-color1);\n",
       "}\n",
       "</style>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import panel as pn  # GUI\n",
    "pn.extension()\n",
    "\n",
    "panels = [] # collect display \n",
    "\n",
    "context = [ {'role':'system', 'content':\"\"\"\n",
    "You are OrderBot, an automated service to collect orders for a pizza restaurant. \\\n",
    "You first greet the customer, then collects the order, \\\n",
    "and then asks if it's a pickup or delivery. \\\n",
    "You wait to collect the entire order, then summarize it and check for a final \\\n",
    "time if the customer wants to add anything else. \\\n",
    "If it's a delivery, you ask for an address. \\\n",
    "Finally you collect the payment.\\\n",
    "Make sure to clarify all options, extras and sizes to uniquely \\\n",
    "identify the item from the menu.\\\n",
    "You respond in a short, very conversational friendly style. \\\n",
    "The menu includes \\\n",
    "pepperoni pizza  12.95, 10.00, 7.00 \\\n",
    "cheese pizza   10.95, 9.25, 6.50 \\\n",
    "eggplant pizza   11.95, 9.75, 6.75 \\\n",
    "fries 4.50, 3.50 \\\n",
    "greek salad 7.25 \\\n",
    "Toppings: \\\n",
    "extra cheese 2.00, \\\n",
    "mushrooms 1.50 \\\n",
    "sausage 3.00 \\\n",
    "canadian bacon 3.50 \\\n",
    "AI sauce 1.50 \\\n",
    "peppers 1.00 \\\n",
    "Drinks: \\\n",
    "coke 3.00, 2.00, 1.00 \\\n",
    "sprite 3.00, 2.00, 1.00 \\\n",
    "bottled water 5.00 \\\n",
    "\"\"\"} ]  # accumulate messages\n",
    "\n",
    "\n",
    "inp = pn.widgets.TextInput(value=\"Hi\", placeholder='Enter text here…')\n",
    "button_conversation = pn.widgets.Button(name=\"Chat!\")\n",
    "\n",
    "interactive_conversation = pn.bind(collect_messages, button_conversation)\n",
    "\n",
    "dashboard = pn.Column(\n",
    "    inp,\n",
    "    pn.Row(button_conversation),\n",
    "    pn.panel(interactive_conversation, loading_indicator=True, height=300),\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sure! Here's a JSON summary of your food order:\n",
      "\n",
      "{\n",
      "  \"pizza\": {\n",
      "    \"size\": \"12.95\",\n",
      "    \"toppings\": [\"extra cheese\", \"mushrooms\"]\n",
      "  },\n",
      "  \"drinks\": [\n",
      "    {\n",
      "      \"name\": \"coke\",\n",
      "      \"size\": \"3.00\"\n",
      "    },\n",
      "    {\n",
      "      \"name\": \"sprite\",\n",
      "      \"size\": \"2.00\"\n",
      "    }\n",
      "  ],\n",
      "  \"sides\": [\n",
      "    {\n",
      "      \"name\": \"fries\",\n",
      "      \"size\": \"4.50\"\n",
      "    }\n",
      "  ],\n",
      "  \"total_price\": \"22.45\"\n",
      "}\n",
      "\n",
      "Please let me know if there's anything else you'd like to add to your order!\n"
     ]
    }
   ],
   "source": [
    "messages = context.copy()\n",
    "messages.append(\n",
    "    {'role':'system', 'content':'create a json summary of the previous food order. Itemize the price for each item\\\n",
    "     The fields should be 1) pizza, include size 2) list of toppings 3) list of drinks, include size 4) list of sides inlcude size 5)total price '},\n",
    "\n",
    ")\n",
    "\n",
    "response = get_completion_from_messages(messages, temperature=0)\n",
    "print(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
