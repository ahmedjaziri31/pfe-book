import os
import requests
from pathlib import Path

def download_image(url, save_path):
    """
    Download an image from a URL and save it to the specified path.
    
    Args:
        url (str): URL of the image to download
        save_path (str): Path where the image should be saved
    """
    try:
        # Create directory if it doesn't exist
        directory = os.path.dirname(save_path)
        Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Download the image
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Save the image
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        print(f"Successfully downloaded: {save_path}")
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print(f"Connection Error: Could not connect to {url}")
    except requests.exceptions.Timeout:
        print(f"Timeout Error: Request to {url} timed out")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"I/O Error: {e}")

# Example usage
if __name__ == "__main__":
    # Dictionary of image URLs and their save paths
    images = {
        # Technology Icons
        "https://raw.githubusercontent.com/expo/expo/master/style/expo-logo.png": "images/icons/expo.png",
        "https://raw.githubusercontent.com/microsoft/TypeScript/main/doc/logo.svg": "images/icons/typescript.png",
        "https://avatars.githubusercontent.com/u/72518640": "images/icons/tanstack.png",  # TanStack GitHub avatar
        "https://clerk.com/images/clerk-logo.svg": "images/icons/clerk.png",
        "https://avatars.githubusercontent.com/u/7308666": "images/icons/maestro.png",  # Placeholder for Maestro
        "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/azure.png": "images/icons/azure.png",
        "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png": "images/icons/github.png",
        "https://expressjs.com/images/express-facebook-share.png": "images/icons/express.png",
        "https://www.postman.com/favicon-32x32.png": "images/icons/postman.png",
        "https://vitejs.dev/logo.svg": "images/icons/vite.png",
        "https://reactjs.org/favicon.ico": "images/icons/react.png",
        "https://labs.mysql.com/common/logos/mysql-logo.svg": "images/icons/mysql.png",
        "https://www.docker.com/wp-content/uploads/2022/03/vertical-logo-monochromatic.png": "images/icons/docker.png",
        "https://playwright.dev/img/playwright-logo.svg": "images/icons/playwright.png",
        "https://storybook.js.org/images/placeholders/140x140.png": "images/icons/storybook.png",
        
        # Tools
        "https://www.overleaf.com/favicon.ico": "images/icons/overleaf.png",
        "https://staruml.io/image/staruml_logo.png": "images/icons/staruml.png",
        "https://www.canva.com/favicon.ico": "images/icons/canva.png",
    }
    
    # Download each image
    for url, path in images.items():
        print(f"Downloading {url} to {path}...")
        download_image(url, path)