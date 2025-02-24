# Work Smarter Setup Guide

Follow these steps to set up your own automated workflow using GitHub Actions.

---

## Step 1: Create Your Own GitHub Repository

1. Navigate to [GitHub](https://github.com/) and click **New Repository**.
2. Name your repository (choose private or public as needed).
3. **Do not** initialize it with a README (we will push one later).

---

## Step 2: Generate a GitHub Token with Workflow Permissions

You need a Personal Access Token (PAT) to push changes to the workflow file.

1. Go to [GitHub Token Settings](https://github.com/settings/tokens).
2. Click **Generate new token (classic)**.
3. Choose an expiration date (or select "No expiration" for permanent use).
4. Under **Scopes**, check the following:
   - `repo` (Full control of private repositories)
   - `workflow` (Update and manage GitHub Actions workflows)
5. Click **Generate Token** and copy the token.

> **Note:** Keep this token secure and save it somewhere safe.

---

## Step 3: Clone This Repository and Push It to Yours

Clone this repository locally and push it to your new GitHub repository using the following commands:

    ```bash
    # Clone this repository
    git clone https://github.com/AdrienViault/work_smarter.git

    # Change into the cloned directory
    cd work_smarter

    # Initialize it as a new Git repository (if not already initialized)
    git init

    # Link it to your GitHub repository (replace YOUR_GITHUB_USERNAME and YOUR_REPO_NAME)
    git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git

    # Set the main branch and push the code to your repository
    git branch -M main
    git push -u origin main

---

# Step 4: Modify the Workflow File

Open the file `.github/workflows/update-folder.yml` in your text editor and update it as follows:

1. **Update Git Configuration:**  
   Replace the default Git configuration lines with your own details:
   ```yaml
   git config --local user.email "your-email@example.com"
   git config --local user.name "YourGitHubUsername"

1. **Commit Your Changes:**  
   After editing, add, commit, and push your changes:
   ```bash
    git add .github/workflows/update-folder.yml
    git commit -m "Update workflow file with my GitHub details"
    git push

---

# Step 5: Test Your Workflow

Before relying on scheduled runs, it's a good idea to test your workflow manually. Follow these steps:

1. **Go to Your Repository on GitHub:**  
   Open your repository page in GitHub.

2. **Navigate to the Actions Tab:**  
   Click on the **Actions** tab in the repository navigation menu.

3. **Select the Relevant Workflow:**  
   Find and click on your workflow (for example, "Update Folder Workflow" or the job labeled "updates").

4. **Run the Workflow Manually:**  
   Look for the **Run workflow** button (sometimes located in the upper-right corner of the workflow details page) and click it.  
   - You might be prompted to select a branch—ensure you choose the correct one (usually `main`).

5. **Monitor the Job:**  
   After triggering the workflow, monitor the job's execution to ensure all steps complete successfully.  
   - Check for any errors or issues in the logs.

Once confirmed, your workflow is ready and will run automatically according to the scheduled cron expression.


---


# Step 6: Enjoy Easy Smart Work Visibility

Your GitHub Actions workflow is now set up and will run automatically on a schedule. With this automation, you’ll see a randomized number of commits each day—giving you a unique visualization of your activity.

**To Monitor Your Workflow:**
- Navigate to your repository on GitHub.
- Click on the **Actions** tab to view logs and workflow execution details.

Happy automating!