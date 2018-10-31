
```
git checkout develop
git pull develop
git checkout -b <your branch>
# when complete task
git add .
git commit -m '#<number task> commit messages' 
git push origin <your branch>
```


 - Настройка flake + pre-commit hook
``` 
sudo pip3 install flake8
# https://habrahabr.ru/company/dataart/blog/318776/ (OUTPUT FILTERS -> $FILE_PATH$\:$LINE$\:$COLUMN$\:.*)
flake8 --install-hook git
git config --global --bool flake8.strict true
# Удобный запуск = ctrl + shift + a -> flake -> enter
```
