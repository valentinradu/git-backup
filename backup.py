# Usage backup.py list-of-paths-to-repo

import git
import sys
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
              
if __name__ == '__main__':
    
    paths = sys.argv[1:]
    
    fails = []
    for path in paths:
        try:
            repo = git.Repo(path)
            
            if repo.bare:
                continue
            
            if repo.is_dirty():
                repo.git.add(u=True)
                repo.git.commit('-m', '[Backup Commit]', author='radu.v.valentin@gmail.com')
                repo.git.push()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            fails.append(path)
        
    if len(fails) > 0:
        notify('Git auto push', '{} failed.'.format(", ".join(fails)))
        
        
        
        
        