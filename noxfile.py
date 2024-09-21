import nox
import yaml


@nox.session
def update_tags(session: nox.Session):
    with open(file="action.yml") as stream:
        action = yaml.safe_load(stream=stream)
    action = action["runs"]["steps"][2]["uses"]
    version = action.split("@")[1]
    major = version.split(".")[0]
    for tag in [version, major]:
        session.run(
            "git",
            "tag",
            "--annotate",
            "--force",
            "--message",
            "",
            tag,
            external=True,
        )
        session.run(
            "git",
            "push",
            "--force",
            "origin",
            tag,
            external=True,
        )
    output_file = session.env["GITHUB_OUTPUT"]
    with open(file=output_file, mode="a") as f:
        f.write(f"tag={version}\n")
