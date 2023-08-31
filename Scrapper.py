import requests
import bs4

def scrape_linkedin_comments(post_url):
  """Scrape comments from a LinkedIn post.

  Args:
    post_url: The URL of the LinkedIn post.

  Returns:
    A list of dictionaries, where each dictionary contains the following information
    for a comment:
      - name: The name of the commenter.
      - profile_url: The URL of the commenter's profile.
      - comment: The text of the comment.
  """

  # Get the HTML of the LinkedIn post.
  response = requests.get(post_url)
  soup = bs4.BeautifulSoup(response.content, 'html.parser')

  # Find all of the comments on the post.
  comments = soup.find_all('div', class_='comment-body')

  # Create a list to store the information about the comments.
  comment_info = []

  # Iterate over the comments and extract the information about each comment.
  for comment in comments:
    name = comment.find('a', class_='comment-author-name').text
    profile_url = comment.find('a', class_='comment-author-name')['href']
    comment_text = comment.find('p', class_='comment-text').text

    comment_info.append({
      'name': name,
      'profile_url': profile_url,
      'comment': comment_text,
    })

  return comment_info

if __name__ == '__main__':
  # Get the URL of the LinkedIn post from the user.
  post_url = input('Enter the URL of the LinkedIn post: ')

  # Scrape the comments from the post.
  comments = scrape_linkedin_comments(post_url)

  # Print the information about the comments.
  for comment in comments:
    print('Name:', comment['name'])
    print('Profile URL:', comment['profile_url'])
    print('Comment:', comment['comment'])
