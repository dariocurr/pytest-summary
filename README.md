# pytest-summary

![Workflow badge](https://github.com/dariocurr/pytest-summary/actions/workflows/validate_action.yml/badge.svg)

![Example summary](https://user-images.githubusercontent.com/48800335/171606700-86ff892f-11d6-43e9-8f8c-ef9b1e459d3a.png)

> This action is just an extension of the [`test-summary`](https://github.com/test-summary) action

Run your pytests and produce an easy-to-read summary as part of your GitHub Actions CI/CD workflow.
This helps you understand at-a-glance the impact to the changes in your pull requests, and see which changes are introducing new problems.

*   Integrates tests easily with your existing GitHub Actions workflow
*   Produces summaries from `pytest` output
*   Customizable to show just a summary, just failed tests, or all test results.

---

## Getting Started

> This action requires a python set up before its usage (e.g [setup-python](https://github.com/actions/setup-python)).
>For example:
>
>```yaml
>- name: Set up Python
>   uses: actions/setup-python@main
>   with:
>     python-version: "3.10"
>```

To set up the `pytest` summary action, just add the following line of YAML to your GitHub Actions workflow:

```yaml
-  uses: dariocurr/pytest-summary@main
```

---

## Options

Options are specified on the [`with`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepswith) map of the action.

*   **extensions**: the `pytest` extensions to install along `pytest` (optional, by default no extensions are included)
For example:

    ```yaml
    - uses: dariocurr/pytest-summary@main
      with:
        extensions: pytest-asyncio pytest-cov
    ```

*   **`options`**: the `pytest` options (optional, by default no options are include)
To specify them correctly, please have a look [here](https://docs.pytest.org). For example:

    ```yaml
    - uses: dariocurr/pytest-summary@main
      with:
        options: -vv -s
    ```

*   **`output`**: the path where to create the output (optional, by default the output will be the workflow summary)
  The path to the GitHub-flavored Markdown (GFM) output file to populate with the `pytest` summary markdown data. For example:

    ```yaml
    - uses: dariocurr/pytest-summary@main
      with:
        output: test-summary.md
    ```

*   **`paths`**: the path to the folders or files containing the tests (optional, by default `tests`)
  You can specify glob patterns, including `**` to match the pattern recursively or specify multiple test paths on multiple lines. For example:

    ```yaml
    uses: dariocurr/pytest-summary@main
    with:
      paths: tests/**.py
    ```

    or

    ```yaml
    uses: dariocurr/pytest-summary@main
    with:
      paths: |
        tests/test_file_1.py \
        tests/test_file_2.py
    ```

*   **`show`**: which tests have to be shown in the summary (optional, by default just the failed tests are shown in the summary)

    *   To show all tests, specify: `show: all`
    *   To show no tests, specify: `show: none`

---

## Upload the markdown

The `pytest-summary` step generates a summary in GitHub-flavored Markdown (GFM). Once the markdown is generated, you can upload it as a build artifact, add it to a pull request comment, or add it to an issue. For example, to upload the markdown generated in the prior example as a build artifact:

```yaml
- name: Upload test summary
  uses: actions/upload-artifact@v3
  with:
    name: test-summary
    path: test-summary.md
  if: always()
```

> Note the if: always() conditional in this workflow step: you should always use this so that the test summary creation step runs even if the previous steps have failed. This allows your test step to fail -- due to failing tests -- but still produce a test summary.
