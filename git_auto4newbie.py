import git
import datetime
def get_commits_by_author(repo_path, author_name):
    # Initialize the repository
    repo = git.Repo(repo_path)

    # Retrieve the commits
    commits = list(repo.iter_commits())

    # Filter the commits by author name
    author_commits = [commit for commit in commits if commit.author.name == author_name]

    return author_commits


# Example usage:
repo_path = r'C:\MIDAS\gnew_Commit'
author_name = 'ljh0620'
repo_path2 = r'C:\MIDAS\genw_NS'
commits = get_commits_by_author(repo_path, author_name)
commits2 = get_commits_by_author(repo_path2, author_name)

end_day = datetime.date(2023, 10, 13)
# Print the filtered commits
cnt = 1
for commit in commits:
    if commit.committed_datetime.date() <= end_day  :
        print(f"{cnt}. {commit.author.name}: {commit.message}".strip(), commit.committed_datetime.date())
        cnt+=1

for commit in commits2:
    if commit.committed_datetime.date() <= end_day:
        print(f"{cnt}. {commit.author.name}: {commit.message}".strip(), commit.committed_datetime.date())
        cnt+=1