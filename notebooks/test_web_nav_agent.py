from WebNavigationAgent import WebNavigationAgent

def main():
    # Initialize the Web Navigation Agent
    web_nav_agent = WebNavigationAgent()

    # Example user query
    user_query = "latest autonomous agent news"

    # Perform the search
    print(f"Searching for: {user_query}")
    top_result_url = web_nav_agent.perform_search(user_query)

    if top_result_url:
        print(f"Top result URL: {top_result_url}")
        # Uncomment the line below to actually open the top result in a web browser
        # web_nav_agent.open_web_page(top_result_url)
    else:
        print("Failed to find a result for the query.")

if __name__ == "__main__":
    main()
