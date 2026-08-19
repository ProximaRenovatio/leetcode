# Git Commands

## Initial setup

```bash
# Initialize a new local Git repository.
git init

# Show the current repository status and modified/untracked files.
git status

# Stage all changes for the next commit.
git add .

# Create a commit with a descriptive message.
git commit -m "Initial commit"

# (A this point it is required to create the repository manually on GitHub.)

# Connect the local repository to the GitHub remote repository.
git remote add origin https://github.com/USERNAME/leetcode.git

# Rename the current branch to main.
git branch -M main

# Push the local main branch to GitHub and set the upstream branch.
git push -u origin main
```

## Normal workflow

```bash
# Check which files have changed.
git status

# Stage all changes.
git add .

# Create a commit containing the staged changes.
git commit -m "Describe the changes"

#Push committed changes to GitHub.
git push
```

Useful commands

```bash
# Show the commit history.
git log

# Show unstaged changes.
git diff

# Show changes that are staged for commit.
git diff --staged

# Show configured remote repositories.
git remote -v

# List local branches.
git branch

# Fetch and merge changes from the remote repository.
git pull