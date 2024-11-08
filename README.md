# GitHub Auto Follow Back Script

Automatically follow back users who follow you on GitHub. This action also unfollows ~~assholes~~ users who don't follow you back (with exceptions).



## 🚀 Quick Setup
1. Fork this repository
2. Generate a GitHub Personal Access Token:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens)
   - You can generate a token using either the classic or beta method:
     - **Classic Method:**
       - Click on "Generate new token (classic)"
       - Set a note for the token (e.g., "GitHub Follow Back Token")
       - Select the following scopes:
         - `read:user`
         - `user:follow`
       - Click "Generate token"
       - Copy the generated token (you will need it in the next step)
     - **Beta Method:**
       - Click on "Generate new token (beta)"
       - Set a token name (e.g., "GitHub Follow Back Token")
       - Set expiration for the token
       - Under "Permissions", click "Account permissions"
       - Under "Followers", select "Read and Write"
       - Click "Generate token"
       - Copy the generated token (you will need it in the next step)
3. Add your GitHub secrets:
   - Go to your repository `Settings` > `Secrets and variables` > `Actions` > `New repository secret`
   - Add two new secrets:
     - `USERNAME`: Your GitHub username
     - `TOKEN`: The GitHub Personal Access Token you generated in the previous step


## Whitelist Users
Edit `whitelist.txt` file in the root directory with usernames you never want to unfollow:
```txt
username1
username2