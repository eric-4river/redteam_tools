import click
import yaml, json
from functools import partial


def toFile(filename, content: str):
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(content)


@click.command()
@click.argument("files", nargs=-1, type=click.File("rb"))
@click.option('--outfile', '-f', help='output file')
def main(files, outfile):
    pocs = []
    if not outfile:
        outfunc = print
    else:
        outfunc = partial(toFile, outfile)

    for file in files:
        pocs.append(yaml.load(file.read()))

    outfunc(json.dumps(pocs))

if __name__ == '__main__':
    main()