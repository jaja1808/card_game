Configuration : 
Git init 
git config --global user.name "Anthony"  
git config --global user.email « riviere.anthony.fr@gmail.com »

Status du git :
git status

Ajouter un git : 
git remote add origin https://github.com/jaja1808/card_game.git 

Récup the git : 
git pull origin main --allow-unrelated-histories

When modi done in local have to add.
git add .
When this motif are add, append a message to rescript what are the modify
git commit -m « coucou »
When the twos steps are done, you push online, 
git push --set-upstream origin main   

Parameters of branch
git branch -m master main

Token for connection. (Hav to go on Github to create it. Settings, developers settings, personal access token) 
git remote set-url origin https://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@github.com/jaja1808/card_game.git