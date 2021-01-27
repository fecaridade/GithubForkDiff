import requests
import json
from time import sleep


class GithubForksDiff:
    def __init__(self, user, repo, branch):
        self.user = user
        self.repo = repo
        self.branch = branch

    def make_diff_link(self, repo1, branch1, repo2, branch2):
        return f"https://api.github.com/repos/{self.user}/{self.repo}/compare/{repo1}:{branch1}...{repo2}:{branch2}"

    def verify_if_content(self, diff_link):
        resp = requests.get(diff_link)
        if len(resp.json()) == 0:
            return False
        else:
            return True

    def req_api(self):

        page = 0
        data = []
        while True:
            sleep(2)
            resp = requests.get(
                f"https://api.github.com/repos/{self.user}/{self.repo}/forks?page={page}")
            if len(resp.json()) == 0:
                break
            elif len(resp.json()) == 2:
                print("LIMITE DO GITHUB EXCEDIDO")
            else:
                data.append(resp.json())
                page += 1
        return data

    def get_fork_list(self):
        api_data = self.req_api()
        infos = []
        for data in api_data:
            user_info = {}
            for key in data:
                user_info['nome'] = key['owner']['login']
                user_info['url'] = key['url']
                user_info['diff'] = self.make_diff_link(
                    self.user, self.branch, user_info['nome'], key['default_branch'])
            if self.verify_if_content(user_info['diff']):
                infos.append(user_info)
        return infos

    def generate_output(self):
        users = self.get_fork_list()
        output_file = open('output.txt', 'w')
        for user in users:
            output_file.write(f'''
nome: {user['nome']}
repositorio: {user['url']}
diff_fork: {user['diff']}\n''')
        output_file.close()



