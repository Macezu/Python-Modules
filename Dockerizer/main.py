import git
import os


def find_file(filename, path, image):
   for root, dir, files in os.walk(path):
      if filename in files:
         return os.system(f"docker build . -t {image} && docker push {image}")
   return False

while True:
    repo = os.environ['REPO']
    image_name = os.environ['IMAGE']
    try:
        repo = git.Repo.clone_from(repo, os.path.join("./", 'repo'), branch="main")
        with open('./repo/Dockerfile', 'w') as fp:
            pass
            # To write data to new file uncomment
            fp.write("New file created")
        print("Repo cloned succesfully")
        break
    except:
        print ("Repo could not be downloaded")
    