import os
import subprocess
import openai
import requests

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_REPOSITORY = os.environ["GITHUB_REPOSITORY"]
GITHUB_SHA = os.environ["GITHUB_SHA"]

openai.api_key = OPENAI_API_KEY

review_prompt = rf"""You are an expert competitive programming coach and senior software engineer.
Please review the following Git diff, which contains a correct solution to an algorithm problem (e.g., Baekjoon Online Judge or LeetCode).

Focus on:
- Potential performance improvements (time and space complexity)
- Opportunities for cleaner, more concise, or more efficient code
- Removal of redundant or unnecessary operations
- Enhancing readability or structure
- Minor style issues or naming improvements if necessary

The solution has already passed all test cases, so correctness or edge cases do not need to be verified.

Provide a **concise, structured** review highlighting strengths and areas for improvement.

Please respond in Korean."""

def get_git_diff():
    result = subprocess.run(
        ["git", "show", GITHUB_SHA, "--unified=3", "--no-color"],
        capture_output=True,
        text=True
    )
    return result.stdout


def ask_llm(diff_text):
    prompt = review_prompt+f"\n\n{diff_text[:7000]}"

    response = openai.beta.chat.completions.parse(
        model="gpt-4.1",
        messages=[
            {"role": "developer", "content": "You are a professional code reviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content


def post_github_comment(review_text):
    url = f"https://api.github.com/repos/{GITHUB_REPOSITORY}/commits/{GITHUB_SHA}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    data = {
        "body": f"**Automated Code Review by LLM:**\n\n{review_text}"
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Review comment posted successfully.")
    else:
        print("Failed to post comment:", response.text)


if __name__ == "__main__":
    diff = get_git_diff()
    if not diff.strip():
        print("No diff found.")
        exit(0)

    review = ask_llm(diff)
    print("LLM Code Review:\n", review)
    post_github_comment(review)