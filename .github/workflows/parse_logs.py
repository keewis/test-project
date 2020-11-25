# type: ignore
import pathlib

files = pathlib.Path("logs").rglob("**/*-log")
files = sorted(filter(lambda x: x.is_file(), files))

message = "\n"

print("Parsing logs ...")
for file in files:
    with open(file) as fpt:
        print(f"Parsing {file.absolute()}")
        data = fpt.read().split("test summary info")[-1].splitlines()[1:-1]
        data = "\n".join(data)
        version = file.name.split("-")[1]
        message = "\n".join(
            message,
            "<details><summary>Python {version} Test Summary Info</summary>",
            "",
            "```bash",
            data,
            "```",
            "</details>",
            "",
        )

output_file = pathlib.Path("pytest-logs.txt")
with open(output_file, "w") as fpt:
    print(f"Writing output file to: {output_file.absolute()} ")
    fpt.write(message)
