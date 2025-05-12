# AI-powered API Documentation Search Tool

This project was built for my thesis (Tekoälyavusteinen luonnollisen kielen haku API-dokumentaatiossa) in Haaga-Helia University of Applied Sciences.

## Features
  - Ask a question about API-documentation with natural language like "How do I create a user?"
  - Uses local Swagger JSON file as the source
  - Powered by OpenAI's GPT-3.5 Turbo
  - Simple command line interface

## Technologies
  - Python 3.13.3
  - OpenAI GPT-3.5 Turbo
  - JSON parsing
  - .env for secure API key management

## Setup
  ### install dependencies:
    - pip install -r requirements.txt

  ### add your OpenAI API key to .env:
    - OPENAI_API_KEY = key_here

  ### run the program:
     - python main.py

## Notes
- This is a prototype, tested with swagger petstore documentation
- Does not parse request body structure atm
- For local testing
