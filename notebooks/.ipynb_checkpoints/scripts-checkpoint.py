import pyodbc
print(pyodbc.drivers())

#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"#
how do I pull changes from the remote repository?

fatal: Need to specify how to reconcile divergent branches.
# You can pull changes from the remote repository using:
# git pull origin <branch-name>
# If you encounter the error "fatal: Need to specify how to reconcile divergent branches",
# you can specify the reconciliation strategy by using:
# git pull --rebase origin <branch-name>
# or
# git pull --no-rebase origin <branch-name>
# If you want to set a default behavior for all branches, you can use:
# git config pull.rebase true
# git config pull.rebase false
# git config pull.ff only
# To set the default behavior for all branches, you can use:
# git config --global pull.rebase true
# git config --global pull.rebase false
# git config --global pull.ff only
# To set the default behavior for the current branch, you can use:
