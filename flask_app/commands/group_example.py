import click

import click_utils


__all__ = ['group']


@click.group(invoke_without_command=True)
@click.pass_context
def group(ctx):
	""" Show help for the group. """
	if ctx.invoked_subcommand is None:
		click_utils.print_help(ctx, None, True)

@group.command()
@click_utils.help_option()
def sub():
	""" Basic sub command. """ 
	return "Group - Sub command"

