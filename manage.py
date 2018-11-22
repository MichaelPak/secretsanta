#!/usr/bin/env python
from subprocess import call

import click

from app import app, storage

click.disable_unicode_literals_warning = True


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


@cli.command()
def loaddb():
    storage.load()
    click.echo(' * Database initialized')


@cli.command()
def tfinit():
    call(["terraform", "init", "iaac/"])


@cli.command()
def tfapply():
    call(["terraform", "apply", "-var-file=local.tfvars", "iaac/"])


@cli.command()
def tfdestroy():
    call(["terraform", "destroy", "-var-file=local.tfvars", "iaac/"])


@cli.command()
@click.option("--ip", required=True)
@click.option("--env")
def ansplay(ip, env):
    command = ["ansible-playbook", "-i", "{},".format(ip), "iaac/deploy.yml"]
    if env:
        command += ["-e", env]
    call(command)


if __name__ == '__main__':
    cli(obj={})
