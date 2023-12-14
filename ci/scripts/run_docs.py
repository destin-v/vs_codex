import os
import webbrowser


def generate_html():
    """Generate the HTML files that are necessary to display the information."""

    os.system("mkdir -p docs/html/src/")
    os.system("cp -rf docs/pics docs/html/src/")

    # Modern way to open files. The closing in handled cleanly
    with open("README.md", mode="r") as in_file, open("src/__init__.py", mode="w") as out_file:
        # Header
        out_file.write('"""')

        # Write
        for in_line in in_file:
            mod_line = in_line.replace("docs/pics/", "pics/")
            out_file.write(mod_line)

        # Footer
        out_file.write('"""')

    os.system("pdoc3 --html src --template-dir ci/templates/ -o ./docs/html --force")


def show_docs():
    """Generate the HTML webpage and open a browser to display it."""

    generate_html()
    cwd = os.getcwd()
    webbrowser.get("chrome").open(f"file://{cwd}/docs/html/src/index.html")


if __name__ == "__main__":
    show_docs()
