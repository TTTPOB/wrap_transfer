import sys
import subprocess
import re


def execute_transfer(
    path_to_upload: str,
    transfer_binary: str = "transfer.exe",
    transfer_backend: str = "wss",
):
    cmd_args = [transfer_binary, transfer_backend, path_to_upload]
    shell_cmd = " ".join(cmd_args)
    print(shell_cmd, file=sys.stderr)
    # output = subprocess.check_output(cmd_args).decode("utf-8")
    output = subprocess.check_output(shell_cmd, shell=True).decode("utf-8")
    return output


def parse_output(output: str) -> dict:
    """
    Parse the output of the transfer.exe binary.
    """
    lines = [line for line in output.strip().split("\n")]
    splited_lines = [re.split(r": ", line) for line in lines]
    parsed = {line[0]: line[1] for line in splited_lines}
    return parsed
