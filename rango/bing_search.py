__author__ = 'diego'
import json
import requests

# Add your BING_API_KEY

BING_API_KEY = 'Q8zc6mDMyj5Ldbupw3vRW/sIMiXz7lpr8+HVuPQcpng'


def main():
    search_input = input("Please enter your search terms: ")
    search_results = run_query(search_input)
    for result in search_results:
        print("title: {a}, rank: {b}, URL: {c}").format(result['title'], result['link'], result['summary'])

def run_query(search_terms):
    # Specify the base
    root_url = 'https://api.datamarket.azure.com/Bing/Search/'
    source = 'Web'

    # Specify how many results we wish to be returned per page.
    # Offset specifies where in the results list to start from.
    # With results_per_page = 10 and offset = 11, this would start from page 2.
    results_per_page = 10
    offset = 0

    # Wrap quotes around our query terms as required by the Bing API.
    # The query we will then use is stored within variable query.
    query = "'{0}'".format(search_terms)

    # Construct the latter part of our request's URL.
    # Sets the format of the response to JSON and sets other properties.
    search_url = "{0}{1}?$format=json&$top={2}&$skip={3}&Query={4}".format(
        root_url,
        source,
        results_per_page,
        offset,
        query)

    # Setup authentication with the Bing servers.
    # The username MUST be a blank string, and put in your API key!
    username = ''

    # Create our results list which we'll populate.
    results = []

    try:
         # Connect to the server and read the response generated.
        response = requests.get(search_url, auth=(username, BING_API_KEY))

        # Convert the string response to a Python dictionary object.
        json_response = response.json()

        # Loop through each page returned, populating out results list.
        for result in json_response['d']['results']:
            results.append({
            'title': result['Title'],
            'link': result['Url'],
            'summary': result['Description']})

    # Catch a URLError exception - something went wrong when connecting!
    except urllib.error.URLError as e:
        print(("Error when querying the Bing API: ", e))

    # Return the list of results to the calling function.
    return results

if __name__ == '__main__':
    main()
