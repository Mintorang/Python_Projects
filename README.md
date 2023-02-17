This is how to edit, commit and push to github using in gut in the terminal
We are going to edit the readme file saying Hello World
Make sure you have cd into your github folder

1) This command will install GIT: 

```bash
sudo apt install git-all
```

2) This command will clone your github files to whatever computer you are in:

```bash
git clone https://github.com/<your username>/<your repository name>.git
```

2) This command will check whether you have something to commit: 


```bash
git status
```


3) This command will add Hello World to your readme file: 



```bash
echo "Hello World" >> README.md
```
4) This command will commit this to your file:

```bash
git commit -m README.md
```

5)This command will push the updated read me file to your github:


```bash
git push origin main
```


It will ask you for your username and password for your github.
A of a new update fo github it will require you to get a token of github, you can paste that token in instead of your password

There you have
