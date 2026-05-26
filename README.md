# datafun-04-notebooks

<!-- TODO: update the GitHub account name to match YOUR GitHub account name -->

[![Docs Deploy](https://github.com/denisecase/datafun-04-notebooks/actions/workflows/deploy-mkdocs.yml/badge.svg?branch=main)](https://github.com/denisecase/datafun-04-notebooks/actions/workflows/deploy-mkdocs.yml)
[![CI](https://github.com/denisecase/datafun-04-notebooks/actions/workflows/ci-basic-mkdocs.yml/badge.svg?branch=main)](https://github.com/denisecase/datafun-04-notebooks/actions/workflows/ci-basic-mkdocs.yml)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/datafun-04-notebooks/)
[![Python](https://img.shields.io/badge/python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)

> Professional Python project: exploratory data analysis with Jupyter notebooks.

## Project Planning

Two languages:

- This file is written in **Markdown**, a simple markup language for presenting text.
- Our analytics logic is written in **Python**, a scripting language for implementing logic.

When we first encounter a **new and unknown data set**, we want to explore: run some quick checks, view the distributions, see if the data is clean (or if there are many missing values or outliers).

This task is commonly called **Exploratory Data Analysis (EDA)**.
For EDA, it is useful to **combine presentation and code**.
For this, we use Jupyter **notebooks**.

Notebooks combine Markdown cells for section headings and narrative with Python Code cells for calculations and charts.

After running the example script and notebook files,
you'll create a similar notebook to explore a different **tabular** data file (a dataset with rows and columns).

---

## 01: Set Up Machine (Once Per Machine)

Follow the detailed instructions at:
[**01. Set Up Your Machine**](https://denisecase.github.io/pro-analytics-02/01-set-up-machine/)

## 02: Set Up Project (Once Per Project)

1. Get Repository: Sign in to GitHub, open this repository in your browser, and click **Copy this template** to get a copy in **YOURACCOUNT**.

2. Configure Repository Settings:
   - Select your repository **Settings** (the gear icon way on the right).
   -  Go to **Pages** tab / Enable GitHub Pages / Build and deployment / set **Source** to **GitHub Actions**
   -  Go to **Advanced Security** tab / Dependabot / **Dependabot security updates** / **Enable**
   -  Go to **Advanced Security** tab / Dependabot / **Grouped security updates** / **Enable**

3. Clone to local: Open a **machine terminal** in your **`Repos`** folder and clone your new repo.

  ```shell
  git clone https://github.com/YOURACCOUNT/datafun-04-notebooks
  ```

4. Open project in VS Code: Change directory into the repo and open the project in VS Code by running `code .` ("code dot"):

  ```shell
  cd datafun-04-notebooks
  code .
  ```

5. Install recommended extensions.

   - When VS Code opens, accept the Extension Recommendations (click **`Install All`** or similar when asked).

6. Set up a project Python environment (managed by `uv`) and align VS Code with it.

   - Use VS Code menu option `Terminal` / `New Terminal` to open a **VS Code terminal** in the root project folder.
   - Run the following commands, one at a time, hitting ENTER after each:

    ```shell
    uv self update
    uv python pin 3.14
    uv sync --extra dev --extra docs --upgrade
    ```

If asked: "We noticed a new environment has been created. Do you want to select it for the workspace folder?" Click **"Yes"**.

If successful, you'll see a new `.venv` folder appear in the root project folder.

Optional (recommended): install and run pre-commit checks (repeat the git `add` and `commit` twice if needed):

```shell
uvx pre-commit install
git add -A
uvx pre-commit run --all-files
git add -A
uvx pre-commit run --all-files
```

For more detailed instructions and troubleshooting, see the pro guide at:
[**02. Set Up Your Project**](https://denisecase.github.io/pro-analytics-02/02-set-up-project/)

🛑 Do not continue until all REQUIRED steps are complete and verified.

## 03: Daily Workflow (Working With Python Project Code)

Follow the detailed instructions at:
[**03. Daily Workflow**](https://denisecase.github.io/pro-analytics-02/03-daily-workflow/)

Commands are provided below to:

1. Git pull
2. Run and check the Python files
3. Build and serve docs
4. Save progress with Git add-commit-push
5. Update project files

VS Code should have only this project (datafun-04-notebooks) open.
Use VS Code menu option `Terminal` / `New Terminal` and run the following commands:

```shell
git pull
```

In this project, **notebooks are the primary analysis artifact**; but scripts can be used to mirror the core logic.

In the same VS Code terminal, run the example Python source files as modules (preferred):

```shell
uv run python -m datafun_04_notebooks.app_case
```

If a command fails, verify:

- Only this project is open in VS Code.
- The terminal is open in the project root folder.
- The `uv sync --extra dev --extra docs --upgrade` command completed successfully.

Run Python checks and tests (as available):

```shell
uv run ruff format .
uv run ruff check . --fix
uv run pytest --cov=src --cov-report=term-missing
```

Build and serve docs (hit **CTRL+c** in the VS Code terminal to quit serving):

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

While editing project code and docs, repeat the commands above to run files, check them, and rebuild docs as needed.

Save progress frequently (some tools may make changes; you may need to **re-run git `add` and `commit`** to ensure everything gets committed before pushing):

```shell
git add -A
git commit -m "update"
git push -u origin main
```

Additional details and troubleshooting are available in the [Pro-Analytics-02 Documentation](https://denisecase.github.io/pro-analytics-02/).

---

## Project Objectives

### Project Task 1. Personalize Your Documentation Links

Open [mkdocs.yaml](./mkdocs.yaml).
This file configures the associated project documentation website (powered by MkDocs)
Use CTRL+f to find each occurrence of the source GitHub account (e.g. `denisecase`).
Change each occurrence to point to your GitHub account instead (spacing and capitalization MUST match the URL of your GitHub account **exactly**.)

### Project Task 2. Personalize This README.md file

Edit this file in VS Code.
Use CTRL+f to find each occurrence of the source GitHub account (e.g. `denisecase`).
Change each occurrence to point to your GitHub account instead (spacing and capitalization MUST match the URL of your GitHub account **exactly**.)

### Project Task 3. Run the Script Example

1. Read the code file in src/.
2. Run the code file in src/ following this README instructions.
3. Confirm that a project.log was generated in the root project folder.
4. Git add, commit, push to GitHub.
5. Verify your project.log file is visible in GitHub.

### Project Task 4. Run the Notebook Example

In VS Code, with this project open, navigate to the notebooks/ folder.
Open `eda_case.ipynb`.

Follow the instructions to:

1. Select the notebook kernel.
2. Run All.
3. Git add, commit, push to GitHub.
4. Verify the executed notebook is visible in GitHub.

If there are any errors, try to figure out how to address them.
After getting a good example notebook, git add-commit-push to GitHub.
Verify the example notebook is presented as you like.

### Project Task 5. Create a New Notebook File and conduct a New EDA

Now apply what you learned. Create a new notebook and perform EDA on a different dataset.

Recommended Option 1: Use a Seaborn Built-in Dataset

Seaborn includes several datasets. To see the list:
```python
import seaborn as sns
print(sns.get_dataset_names())
```

Good choices for practice:
- `iris` - flower measurements (150 rows, 5 columns)
- `tips` - restaurant tipping data (244 rows, 7 columns)
- `diamonds` - diamond prices and attributes (53940 rows, 10 columns)
- `mpg` - car fuel efficiency (398 rows, 9 columns)
- `titanic` - passenger survival data (891 rows, 15 columns)

Load any of these with: `df = sns.load_dataset('dataset_name')`

Alternatively, Option 2: Choose Your Own Tabular Dataset

Put your dataset in data/raw/ as a csv file.
Use pathlib Paths to create a path to your csv file.

Load a CSV file with: `df = pd.read_csv('path_to_your_file.csv')`

Follow the example, and ensure you have:

- Title and header (author, purpose, date, dataset info with source/citation)
- Numbered sections that match the example.
- Good narrative showing your observations and insights as you work through the process.

---

## Notes

- You do not need to add to or modify `tests/`. They are provided for example only.
- You do not need to view or modify any of the supporting **config files**.
- Many of the repo files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything. Understanding builds naturally over time.
- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) with in a file.

## Troubleshooting >>> or ...

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Resources

- [Pro-Analytics-02](https://denisecase.github.io/pro-analytics-02/) - guide to professional Python
- [ANNOTATIONS.md](./ANNOTATIONS.md) - REQ/WHY/OBS annotations used
- [INSTRUCTORS.md](./INSTRUCTORS.md) - guidance and notes for instructors and maintainers
- [POLICIES.md](./POLICIES.md) - project rules and expectations that apply to all contributors
- [SE_MANIFEST.toml](./SE_MANIFEST.toml) - project intent, scope, and role

## Citation

[CITATION.cff](./CITATION.cff) - TODO: update author and repository fields to reflect your creative work

<!--
WHY: Support correct citation and attribution.
-->

## License

[MIT](./LICENSE)

<!--
WHY: Provide terms of reuse and limits of liability.
You are welcome to copyright your own projects or open source them as you like.
-->
