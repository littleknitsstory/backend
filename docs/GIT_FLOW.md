
- Easy git flow
```
git checkout develop
git pull develop
git checkout -b <your branch>
# when complete task
git add .
git commit -m '#<number task> commit messages' 
git push origin <your branch>
```

- Git flow healthy person
[git-flow-cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)

 - Settings flake + pre-commit hook
``` 
sudo pip3 install flake8
# https://habrahabr.ru/company/dataart/blog/318776/ (OUTPUT FILTERS -> $FILE_PATH$\:$LINE$\:$COLUMN$\:.*)
flake8 --install-hook git
git config --global --bool flake8.strict true
# Easy start -> ctrl + shift + a -> flake -> enter
```
