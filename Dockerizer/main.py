import git
import os


def find_and_build(filename, path, image):
   for files in os.walk(path):
      if filename in files:
         return os.system(f"docker build . -t {image} && docker push {image}")
   return False

def main():
    #For testing purposes
    os.environ['REPO'] = 'https://github.com/henri19102/DevOps-with-Docker'
    os.environ['IMAGE'] = 'Bob'
    os.environ['BRANCH'] = "master"
    while True:
        repo = os.environ['REPO']
        image_name = os.environ['IMAGE']
        user_branch = os.environ['BRANCH']
        try:
            repo = git.Repo.clone_from(repo, os.path.join("./", 'repo'), branch=user_branch)
            find_and_build("Dockerfile","./repo",image_name)
            print("Repo cloned succesfully")
            break
        except:
            print ("Repo could not be downloaded or image not found")
            break

if __name__ == '__main__':
    main()
    