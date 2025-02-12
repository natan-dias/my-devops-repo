import requests
import argparse
import json

def get_tags(repository, image_name):

    if repository is None or image_name is None:
        raise TypeError("Repository name and image name must not be None")

    url = f'https://hub.docker.com/v2/repositories/{repository}/{image_name}/tags?page_size=10&order_by=last_updated'
    response = requests.get(url)
    if response.status_code == 200:
        tags = response.json()['results']
        output = [
            {
                'name': tag['name'],
                'status': tag['tag_status'],
                'last_pushed': tag['tag_last_pushed']
            }
            for tag in tags
        ]

        return output
    else:
        print(f"Failed to fetch tags: {response.status_code}")
        return []

if __name__ == '__main__':

    # USAGE
    # python docker-hub-tags.py -r <repository> -i <image_name>

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repository', type=str, required=True, help='Repository name')
    parser.add_argument('-i', '--image_name', type=str, required=True, help='Image name')
    args = parser.parse_args()

    repository = args.repository
    image_name = args.image_name

    tags = get_tags(repository, image_name)
    print(json.dumps(tags, indent=4))