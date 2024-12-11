import urllib.parse
from load_config import load_config

def build_arxiv_query_url(start_date, end_date, start_index=0, max_results=100):
    """
    Constructs the full URL for querying arXiv API with given parameters.
    
    :param start_date: String in 'YYYYMMDD' format.
    :param end_date: String in 'YYYYMMDD' format.
    :param start_index: Pagination start index.
    :param max_results: Number of results to fetch at once.
    :return: A complete query URL as a string.
    """

    config = load_config()
    categories = config.get("categories", [])
    # Combine categories into an OR query (e.g., (cat:cs.LG OR cat:stat.ML OR cat:math.AP))
    category_query = " OR ".join([f"cat:{cat}" for cat in categories])

    # Date range query using submittedDate
    # We assume inclusive range and that both start_date and end_date are in YYYYMMDD format
    date_query = f"submittedDate:[{start_date} TO {end_date}]"

    # Combine category and date queries
    # Use parentheses to ensure proper grouping, e.g.: (cat:cs.LG OR cat:stat.ML) AND submittedDate:[20240101 TO 20240102]
    search_query = f"({category_query}) AND {date_query}"

    # Base arXiv API endpoint
    base_url = "http://export.arxiv.org/api/query"

    # Parameters dictionary
    params = {
        "search_query": search_query,
        "sortBy": "submittedDate",
        "sortOrder": "ascending",
        "start": start_index,
        "max_results": max_results
    }

    # Encode parameters into the query string
    query_string = urllib.parse.urlencode(params)

    # Construct the final URL
    full_url = f"{base_url}?{query_string}"
    return full_url


# Optional: Test the function
if __name__ == "__main__":
    # Example test: from January 1, 2024 to January 2, 2024
    test_url = build_arxiv_query_url("20240101", "20240102")
    print("Test URL:", test_url)

