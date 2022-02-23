

import requests
import json


def repoCount(ID):
    """
    repoCount returns the repos for a given user and the number of commits for each repo
    :param ID: GitHub user ID
    :return: a dictionary of repos for the id, and the number of commits for each of the listed repos
    """

    repos_url = 'https://api.github.com/users/%s/repos' % ID  # url to the user repos list

    user_repos = requests.get(repos_url)  # retrieve data from GitHub API
    if not(user_repos.status_code == requests.codes.ok):   # checks if get call succeeds
        return user_repos.status_code
    repos = user_repos.json()   # convert data to json

    repo_name_list = []     # temp list for storing repo names
    for elem in repos:
        repo_name_list.append(elem['name'])     # add each repo name to the list

    repo_name_count = {}    # dictionary for storing {name: # of commits} for each repo
    for repo in repo_name_list:
        commit_url = 'https://api.github.com/repos/%s/%s/commits' % (ID, repo)  # url to list of commits for repo
        repo_commits = requests.get(commit_url)  # lookup commits for each repo
        if not (repo_commits.status_code == requests.codes.ok):     # checks if get call succeeds
            return user_repos.status_code
        commits = repo_commits.json()   # convert data to json
        repo_name_count[repo] = len(commits)    # sets the number of commits to the number of lines in the json file

    return repo_name_count  # returns dictionary of {name: # of commits} pairs
