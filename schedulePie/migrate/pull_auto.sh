echo "pull automation"
echo "change directory to git repo"
cd "/home/akhil/Desktop/gitHub/Sloth"
git_pull_cmd=$(git pull)
Date=$(date)
echo last pull request on ${Date}> /SchedulePie/note_out.txt