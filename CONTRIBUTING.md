# Contributing to Music-Industry-Insights

Welcome to the team! This guide will help you get started with contributing to the Music-Industry-Insights project. Follow these steps to set up your environment and start collaborating.

## Getting Started

### 1. Clone the Repository

First, you'll need to clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/Music-Industry-Insights.git
cd Music-Industry-Insights
```

### 2. Set Up a Conda Environment

Create and activate a new Conda environment for the project:

```bash
conda create --name music-insights python=3.12 setuptools=75.1.0 -y
conda activate music-insights
```

### 3. Install Project Dependencies

Use the `pyproject.toml` file to install the project in editable mode:

```bash
pip install -e .
```

NOTE: To be able to use this env in jupyter notebook, you may need to install ipyknerl by running the following command:

```bash
conda install ipykernel -y
```

### 4. Set Up DVC

Ensure you have DVC installed
```bash
pip install dvc
```

And set up the data version control:

```bash
dvc pull
```
When you run this command, it will pull the data from the remote repository to your local machine.
If you want to push your changes to the remote repository, you can run the following command:

```bash
dvc add data/
```
This will create a new file called `data.dvc`. This file will contain the information about the data in the `data` directory.

### 5. Create a New Branch

Create a new branch for your work. Use your name.

```bash
git checkout -b yourname_dev
```

### 6. Add Your Name to the README

Add your name to the bottom of the `README.md` file under a "Contributors" section:

```markdown
## Contributors

- Your Name : your-email@example.com
```

### 7. Make a Pull Request

Once you've made your changes and committed them, push your branch to the remote repository:

```bash
git add .
git commit -m "Add your message here"
git push origin yourname_dev
```

You might be prompted to set up upstream repository. If so, do it by running the code given in terminal or by running the following command:

```bash
git push --set-upstream origin yourname_dev
```

Then, go to the GitHub repository and create a pull request (PR) from your branch to the `main` branch. Make sure to provide a clear description of the changes you've made.

Assign the PR to the project maintainer, Shivam Tyagi. (This will notify the maintainer about the PR.)

## Additional Tips

- **Stay Updated**: Regularly pull changes from the `main` branch to keep your branch up to date.
- **Collaborate**: Feel free to ask questions and collaborate with other team members.
- **Document**: Ensure your code is well-documented and includes comments where necessary.

Thank you for contributing to Music-Industry-Insights! Your efforts are greatly appreciated.
