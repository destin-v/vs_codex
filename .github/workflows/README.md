# ♾️ Continuous Integration (CI) Tools

## Workflows
Github workflows with continuous integration is included.  The Github workflows send their tasks to Github runners by default.  If you want to route jobs to your **self-hosted** runners make sure to add a **label**.  The steps are:

> [!NOTE]
Settings › Actions › Runners › Self Hosted Runner › Create Label

<p align="center">
  <img src="../docs/pics/self_hosted_runner.png" alt="drawing" width="800"/>
</p>

In the above example, you can now have your workflows send jobs to `macos-latest` runner by specifying the following in the workflow.yml file:

```yml
jobs:
  test:
    # Set the OS and python versions
    runs-on: macos-latest
```

> [!IMPORTANT]
If your self-hosted runner is given a label that also matches a Github runner (i.e. `ubuntu-latest`) then your job can be scheduled by self-hosted or Github runners.  This is useful for situations where you want the job to have the option of running on either kind of runners.

## Badges
The badge at the top of the README.md will update its status to display whether the CI process succeeds/fails.  Modify it to point to your own repo when starting a new project.

## Git Runner Limits
If you are running into rate limiting issues with Git runner you will need to add an authorization token to your Git actions.  The Github token must be generated from the public Github and *not* your self-hosted Github.  This is because the libraries being installed are sourced from the public Github.


* Generate a Github token [**here**](https://github.com/settings/tokens).
* Navigate to Repo › Settings › Secrets and Variables.
* Add secret **GH_GITHUB_COM_TOKEN** and paste the generated Github token.

The `checks.yml` workflow includes code to display your rate limits.  See this [**template**](https://github.com/actions/setup-python/pull/443#issuecomment-1206776401) for a full example.

## Artifact Upload/Download Errors
If you are running self-hosted Git runners, keep in mind that git-action artifacts will upload/download to public Github.  If your goal is to pass artifacts within a self-hosted runner, the best way is to save files to a shared space.  See a discussion [**here**](https://github.com/orgs/community/discussions/26165).

If you want to upload/download artifacts to public Github using self-hosted runner then you must ensure that your CA certificates are used.  These variables should be set in your `.env` file of your self-hosted runner.

```bash
NODE_EXTRA_CA_CERTS=/path/to/ca-certificates.pem # .crt and .pem are interchangeable
NODE_TLS_REJECT_UNAUTHORIZED=0 # disable CA checking for debugging purposes
```

## Runner Debugging
To enable debugging see [**here**](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/enabling-debug-logging).  The secret `ACTIONS_RUNNER_DEBUG=true` should be set and debugging messaging will show up in the runner logs.
