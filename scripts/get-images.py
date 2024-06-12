import os
import argparse
from google_images_search import GoogleImagesSearch
from pathlib import Path


# api_key=os.getenv("GOOGLE_API_KEY"), cse_id=os.getenv("CSE_ID")
def fetch_images(query, num_images, output_path, api_key, cse_id):
    """
    Fetches images from Google Images and saves them to a specified directory as .png files.

    Args:
        query (str): The search query for fetching images from Google Images.
        num_images (int): The number of images to fetch.
        output_path (str): The directory where the fetched images will be saved.
        api_key (str): The API key for Google Custom Search.
        cse_id (str): The Custom Search Engine ID for Google Custom Search.

    Raises:
        FileNotFoundError: If the specified output directory does not exist and cannot be created.
        ValueError: If the number of images to fetch is not a positive integer.
        Exception: For any other exceptions that occur during the fetching and saving process.

    Returns:
        None
    """

    # Initialize the GoogleImagesSearch object with your API key and CSE ID
    gis = GoogleImagesSearch(api_key, cse_id)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Search parameters
    _search_params = {
        "q": query,
        "num": num_images,
        "fileType": "png",
        "safe": "off",  # safe search
    }

    # Perform the search
    gis.search(search_params=_search_params)

    # Fetch and save the images
    for i, image in enumerate(gis.results()):
        image.download(output_path)
        image.resize(500, 500)
        print(f"Saved image {i+1} to {output_path}")


# Main function to handle arguments
def main():
    parser = argparse.ArgumentParser(
        description="Fetch images from Google Images and save them to a folder."
    )
    parser.add_argument("query", type=str, help="Search query for fetching images.")
    parser.add_argument("num_images", type=int, help="Number of images to fetch.")
    parser.add_argument(
        "output_path", type=str, help="Output directory to save images."
    )
    parser.add_argument("api_key", type=str, help="Google Custom Search API key.")
    parser.add_argument("cse_id", type=str, help="Google Custom Search Engine ID.")

    args = parser.parse_args()

    fetch_images(
        args.query, args.num_images, args.output_path, args.api_key, args.cse_id
    )


if __name__ == "__main__":
    main()
