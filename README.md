# pytest-summary

> This action is just an extension of the [`test-summary`](https://github.com/test-summary) action.

Produce an easy-to-read summary of your project's `pytest` data as part of your GitHub Actions CI/CD workflow. This helps you understand at-a-glance the impact to the changes in your pull requests, and see which changes are introducing new problems.

*   Integrates tests easily with your existing GitHub Actions workflow
*   Produces summaries from `pytest` output
*   Customizable to show just a summary, just failed tests, or all test results.

---

## Getting Started

To set up the `pytest` summary action, just add a few lines of YAML to your GitHub Actions workflow:

```yaml
- name: Test Summary
  uses: dariocurr/pytest-summary@main
  with:
    paths: tests
```

Update `paths` to match the tests paths. In addition, you can specify multiple test paths on multiple lines. For example:

```yaml
- name: Test Summary
  uses: dariocurr/pytest-summary@main
  with:
    paths: |
      tests/test_file_1.py
      tests/test_file_2.py
```

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
---

## Options

Options are specified on the [`with`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepswith) map of the action.

*   **`paths`: the path to the folder containing the tests** (optional, by default `tests`)  

*   **`options`: the `pytest` options** (optional, by default no options are specified)
 Before specify it, please have a look [here](https://docs.pytest.org)

*   **`output`: the path to the output file to create** (optional, by default the output will be to the workflow summary)  
  This is the path to the output file to populate with the `pytest` summary markdown data. For example:

  ```yaml
  - uses: dariocurr/pytest-summary@main
    with:
      output: "summary.md"
  ```

*   **`show`: which tests have to be shown in the summary** (optional, by default just the failed tests are shown in the summary)

    *   To show all tests, specify: `show: all`
    *   To show no tests, specify: `show: none`
