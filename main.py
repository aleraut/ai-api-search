from src.parser import load_swagger
from src.search import search_api

def main():
    swagger_path = "swagger_data/swagger.json"
    swagger_data = load_swagger(swagger_path)

    while True:
        question = input("\n🧠 Esitä kysymys API-dokumentaatiosta ('exit' lopettaa): ")
        if question.lower() in ["exit", "quit"]:
            break
        response = search_api(swagger_data, question)
        print("\n💡 Vastaus:")
        print(response)

if __name__ == "__main__":
    main()
