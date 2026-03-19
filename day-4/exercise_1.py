import sys
import urllib.request
import urllib.error
import json

def fetch_github_profile(username):
    profile_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        # Fetch Profile
        req = urllib.request.Request(profile_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            profile_data = json.loads(response.read().decode())
            
            # Print the raw JSON first (as per instructions, uncomment to see the shape)
            # print("--- Raw Profile JSON ---")
            # print(json.dumps(profile_data, indent=2))
            
            print(f"Username: {profile_data.get('login')}")
            print(f"Bio: {profile_data.get('bio')}")
            print(f"Public Repos: {profile_data.get('public_repos')}")
            print(f"Followers: {profile_data.get('followers')}")
            
        # Fetch Repositories
        req_repos = urllib.request.Request(repos_url, headers=headers)
        with urllib.request.urlopen(req_repos) as response_repos:
            repos_data = json.loads(response_repos.read().decode())
            
            # print("--- Raw Repos JSON (first repo) ---")
            # if repos_data:
            #     print(json.dumps(repos_data[0], indent=2))
            
            # Sort repos by stars (stargazers_count) descending
            sorted_repos = sorted(repos_data, key=lambda x: x.get('stargazers_count', 0), reverse=True)
            top_5_repos = sorted_repos[:5]
            
            print("\nTop 5 Repositories by Stars:")
            for repo in top_5_repos:
                print(f"- {repo.get('name')} | {repo.get('stargazers_count')} stars | {repo.get('language')}")

    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found. (404)")
        elif e.code == 403:
            print(f"Error: API rate limit hit. Try again later. (403)\nDetails: {e.reason}")
        else:
            print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"Network Error: Failed to reach GitHub API.\nDetails: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username_input = sys.argv[1]
    else:
        username_input = input("Enter GitHub username: ")
    fetch_github_profile(username_input)
