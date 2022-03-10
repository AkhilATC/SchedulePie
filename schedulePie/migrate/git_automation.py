from git import Repo
from datetime import date
if __name__ == '__main__':
	repo_dir = '/home/akhil/Desktop/gitHub/Sloth'
	repo = Repo(repo_dir)
	repo.remotes.origin.pull()
	today = date.today()
	today = today.strftime("%dth. %B %Y")
	with open('/SchedulePie/note_out.txt', 'w') as f:
		f.write(f"Last pull request no {today}")