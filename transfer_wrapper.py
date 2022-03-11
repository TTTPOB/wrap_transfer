from wrap_transfer.wrapper import execute_transfer, parse_output
import click
import pyperclip


@click.command()
@click.option(
    "--path-to-upload", "-u", required=True, help="Path to the file to upload."
)
@click.option(
    "--transfer-binary",
    "-t",
    default="transfer.exe",
    help="Path to the transfer binary.",
)
@click.option(
    "--transfer-backend", "-b", default="wss", help="Transfer backend to use."
)
def cli(path_to_upload, transfer_binary, transfer_backend):
    """
    Wrapper for the transfer.exe binary.
    """
    stdout = execute_transfer(path_to_upload, transfer_binary, transfer_backend)
    parsed = parse_output(stdout)
    download_link = parsed["Download Link"]
    pyperclip.copy(download_link)


if __name__ == "__main__":
    cli()
