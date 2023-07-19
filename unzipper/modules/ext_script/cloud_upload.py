# Copyright (c) 2023 EDM115
import json
import subprocess

from unzipper.modules.bot_data import Messages


async def jsonized(command):
    run = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    shell_output = run.stdout.read()[:-1].decode("utf-8").rstrip('\n')
    run.stdout.close()
    if "true" in shell_output:
        shell_output.replace("true", "True")
    elif "false" in shell_output:
        shell_output.replace("false", "False")
    else:
        pass
    try:
        return json.loads(shell_output)
    except:
        return shell_output


async def bayfiles(file, url):
    try:
        uploaded = await jsonized(f"curl -F 'file=@{file}' {url}")
    except:
        uploaded = (Messages.ERROR_UP_BAYFILES)
    return uploaded
