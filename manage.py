#!/usr/bin/env python
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
    click.echo('Database initialized')


if __name__ == '__main__':
    cli(obj={})
