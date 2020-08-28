```

python3 -m pip install --user --upgrade setuptools wheel

python setup.py sdist bdist_wheel

pip install twine
twine check dist/*

python3 -m twine upload --repository testpypi dist/* 
```