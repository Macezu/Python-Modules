import git
import os

while True:
    url = input("Please paste repo url. ")
    inputted_branch = input("Please specify Branch. ")
    try:
        repo = git.Repo.clone_from(url, os.path.join("./", 'repo'), branch=inputted_branch)
        with open('./repo/Dockerfile', 'w') as fp:
            pass
            # To write data to new file uncomment
            fp.write("New file created")
        print("Repo cloned succesfully")
        break
    except:
        print ("Repo could not be downloaded")
    