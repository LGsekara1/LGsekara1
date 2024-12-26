import requests
from bs4 import BeautifulSoup

# Step 1: Fetch Badge Data from HackerRank Profile
def fetch_hackerrank_badges(profile_url):
    response = requests.get(profile_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Update this selector to match HackerRank's badge section
        badges = soup.find_all("img", {"class": "badge-image-class"})  # Replace 'badge-image-class' with actual class

        # Create HTML tags for the badges
        badge_tags = [f'<img src="{badge["src"]}" alt="{badge["alt"]}" height="100">' for badge in badges]
        return badge_tags
    else:
        print(f"Failed to fetch profile: {response.status_code}")
        return []

# Step 2: Update README File with Badges
def update_readme(badges, readme_path="README.md"):
    # Define placeholders
    start_marker = "<!-- HACKERRANK_BADGES_START -->\n"
    end_marker = "<!-- HACKERRANK_BADGES_END -->\n"

    with open(readme_path, "r") as file:
        content = file.readlines()

    # Find marker positions
    start_idx = content.index(start_marker) if start_marker in content else None
    end_idx = content.index(end_marker) if end_marker in content else None

    if start_idx is not None and end_idx is not None:
        content = content[:start_idx + 1] + [f"{tag}\n" for tag in badges] + content[end_idx:]
    else:
        content.append(f"\n{start_marker}{'\n'.join(badges)}\n{end_marker}")

    with open(readme_path, "w") as file:
        file.writelines(content)

# Main Execution
if __name__ == "__main__":
    # Replace with your HackerRank profile URL
    https://www.hackerrank.com/profile/lg_sekara123
