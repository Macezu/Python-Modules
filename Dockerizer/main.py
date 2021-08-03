import git
import os


def find_and_build(filename, path, image):
    for root, dir, files in os.walk(path):
        print(f"searching {files}")
        if filename in files:
            print(f"Found Dockerfile, building {image} now!")
            return os.system(f"docker build . -t {image} && docker push {image}")
    return False


def main():
    # For testing purposes
    os.environ['REPO'] = 'https://github.com/karthequian/docker-helloworld'
    os.environ['IMAGE'] = 'test'
    os.environ['BRANCH'] = "master"

    while True:
        repo = os.environ['REPO']
        image_name = os.environ['IMAGE']
        user_branch = os.environ['BRANCH']
        try:
            repo = git.Repo.clone_from(repo, os.path.join(
                "./", 'repo'), branch=user_branch)
            find_and_build("Dockerfile", "./repo", image_name)
            print("Repo cloned succesfully")
            break
        except:
            print("Repo could not be downloaded or image not found")
            break


if __name__ == '__main__':
    main()
