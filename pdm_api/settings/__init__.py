from .settings import settings

class settings:
    def __init__(self):
        self.settings = settings()
        self.repo = self.settings['repo']
        self.repo_path = self.repo['repo_path']
        self.repo_url = self.repo['repo_url']
        self.key = self.repo['ssh_key']
        self.slack = self.settings['slack']
        self.slack_token = self.slack['token']

    def repo(self):
        return(self.repo)

    def repo_url(self):
        return(self.repo_url)

    def repo_path(self):
        return(self.repo_path)

    def ssh_key(self):
        return(self.key)

    def slack(self):
        return(self.slack)

    def slack_token(self):
        return(self.slack_token)
