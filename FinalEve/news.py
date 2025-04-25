import requests
import webbrowser
from speak_command import speak, takecommand  # Importing speak and takecommand from main.py

def NewsFromBBC():
    """Fetches top news from BBC and allows user interaction via voice commands."""
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "14c4fe6f53fc4f4b84ff7bfed0e5123f"
    }
    main_url = "https://newsapi.org/v1/articles"

    try:
        res = requests.get(main_url, params=query_params)
        res.raise_for_status()
        open_bbc_page = res.json()

        articles = open_bbc_page.get("articles", [])
        if not articles:
            speak("Sorry, I couldn't find any news articles at the moment.")
            return
        top_articles = articles[:4]
        speak("Here are the top news headlines from BBC.")
        print("Top news from BBC:")
        for idx, ar in enumerate(top_articles, start=1):
            title = ar.get("title", "No title available")
            speak(f"Headline {idx}: {title}")
            print(f"{idx}. {title}")

    except requests.exceptions.RequestException as e:
        speak("An error occurred while fetching the news.")
        print(f"Error fetching news: {e}")

if __name__ == '__main__':
    speak("Fetching the latest news from BBC.")
    NewsFromBBC()