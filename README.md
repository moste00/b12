# B12 Application Submission

Automated job application submission for B12 via GitHub Actions.

## Setup

1. Create a new GitHub repository and push these files to it.

2. Add the following secrets to your repository (Settings → Secrets and variables → Actions → New repository secret):
   - `APPLICANT_NAME`: Your full name
   - `APPLICANT_EMAIL`: Your email address
   - `RESUME_LINK`: URL to your resume (PDF, HTML, or LinkedIn profile)

3. The workflow will automatically construct the repository and action run links.

## Running the submission

The workflow runs automatically on push to main, or you can trigger it manually:
- Go to Actions tab in your repository
- Select "Submit B12 Application" workflow
- Click "Run workflow"

The receipt will be printed in the action logs once the submission succeeds.

## Local testing

You can test locally by setting environment variables:

```bash
export NAME="Your Name"
export EMAIL="your@email.com"
export RESUME_LINK="https://your-resume-link.com"
export REPOSITORY_LINK="https://github.com/yourusername/yourrepo"
export ACTION_RUN_LINK="https://github.com/yourusername/yourrepo/actions/runs/12345"

python submit_application.py
```
