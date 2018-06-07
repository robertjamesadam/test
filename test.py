print('test.py')
# to upload the changes we've made
# first you need to git add
# then you need to git commit (which pushes to the local repository)
# when doing this you don't need to follow with file names - it pushes those
# files stored temporarily into the local repository
# then git push pushes these into the cloud
# to pull an updated version from the cloud, use git pull (no need for file
# name)

# but to really manage your code you need use branching
# usually have 2 versions of code: production (which is used) and development
# (which is changed and tested)
# don't want to break entire software just to update little bits
# git checkout -b <branch-name> - Create a new branch and switch to that
# branch.
#git checkout <branch-name> - Switch to the branch you specified.
#git merge <merge-to-branch-name> - Merge current branch to the specified
#branch.
