#!/usr/bin/env bash

message="${1:-Автоматический коммит}"

# Remove ignored files that were committed previously from the Git index.
git ls-files -ci --exclude-standard -z |
  xargs -0 -r git rm --cached --ignore-unmatch --

# Add all remaining project files, including deletions and untracked files.
git add -A

# Commit despite pre-commit hooks and missing changes.
git commit --no-verify --allow-empty -m "$message"

# Force-push the current commit directly to the main branch.
git push --force origin HEAD:main

#что бы запустить коммит
# bash commit-to-main.sh "Сообщение коммита"