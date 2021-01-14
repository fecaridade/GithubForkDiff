import requests
import json


class GithubForksDiff:
    def __init__(self, user, repo, branch):
        self.user = user
        self.repo = repo
        self.branch = branch

    def make_diff_link(self, repo1, branch1, repo2, branch2):
        return f"https://api.github.com/repos/{self.user}/{self.repo}/compare/{repo1}:{branch1}...{repo2}:{branch2}"

    def req_api(self):
        resp = requests.get(
            f"https://api.github.com/repos/{self.user}/{self.repo}/forks")
        return resp.json()

    def get_fork_list(self):
        api_data = self.req_api()
        infos = []
        for data in api_data:
            user_info = {}
            user_info['nome'] = data['owner']['login']
            user_info['url'] = data['url']
            user_info['diff'] = self.make_diff_link(
                self.user, self.branch, data['owner']['login'], data['default_branch'])
            infos.append(user_info)
        return infos

    def generate_output(self):
        users_info = self.get_fork_list()
        output_file = open('output.txt', 'w')
        for user in users_info:
            output_file.write(f'''
nome: {user['nome']}
repositorio: {user['url']}
diff_fork: {user['diff']}\n''')
        output_file.close()


