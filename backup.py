# Usage backup.py list-of-paths-to-repo

import git
import sys


if __name__ == '__main__':
    
    paths = sys.argv[1:]
    
    for path in paths:
        
        repo = git.Repo(path)
        
        if repo.bare:
            continue
        
        if repo.is_dirty():
            repo.git.add(u=True)
            repo.git.commit('-m', '[Backup Commit]', author='radu.v.valentin@gmail.com')
            repo.git.push()
        