from git import Repo



if __name__ == '__main__':
	repo_dir = '/home/akhil/Desktop/gitHub/Sloth'
	repo = Repo(repo_dir)
	repo.remotes.origin.pull()
