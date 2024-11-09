# GitHub Auto Follow Back

This Github Action Automatically follow back users who follow you on GitHub. This action also unfollows ~~assholes~~ users who don't follow you back (with exceptions).



## 🚀 Quick Setup
1. Fork this repository
2. Generate a GitHub Personal Access Token:
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens)
   - You can generate a token using either the classic or beta method:
     - **Classic Method:**
       - Click on "Generate new token (classic)"
       - Set a note for the token (e.g., "GitHub Follow Back Token")
       - Select the following scopes:
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
4. The action will run everyday at midnight, you can change this in the github_follow_back.yaml file.

## ⚠️ Enable GitHub Actions on Your Fork

After forking this repository, GitHub Actions are disabled by default on your fork. To enable the action:

1. **Go to your forked repository** on GitHub.
2. Click on the **Actions** tab.
3. You will see a message stating **"Workflows aren’t being run on this forked repository."**
4. Click the **"I understand my workflows, go ahead and enable them"** button.
5. Go to **GitHub Follow Back** and enable the workflow.
6. Manually trigger the workflow to ensure it runs:
   - Click on the **"GitHub Follow Back"** workflow.
   - Click the **"Run workflow"** button on the right side.
   - In the modal that appears, click **"Run workflow"**.
   
Once you have manually triggered the workflow, it will automatically run according to the specified schedule (everyday at midnight).


## Whitelist Users
Edit `whitelist.txt` file in the root directory with usernames you never want to unfollow:
```txt
username1
username2