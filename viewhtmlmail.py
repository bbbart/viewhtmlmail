"""Simple script to read a multipart email message from stdin and show the HTML
components in a graphical browser.

Meant to be called from mutt.
"""

import sys
import tempfile
import webbrowser
from email.parser import BytesParser
from email.policy import default as DefaultPolicy
from time import sleep

import click

@click.command()
def cli():
    """Entry point."""
    parser = BytesParser(policy=DefaultPolicy)
    stdin = click.get_binary_stream("stdin")
    message = parser.parse(stdin)

    if message.get_content_type() == "text/html":
        show_part(message)
        sys.exit()
    elif not message.is_multipart():
        sys.exit("Unexpected MIME type")

    # show the first part with content type HTML
    for part in message.walk():
        if part.get_content_type() == "text/html":
            show_part(part)
            break


def show_part(part):
    """Save the contents of the given email part to a temporary HTML file and
    open it in the default browser.
    """

    with tempfile.NamedTemporaryFile(
        suffix=".html", prefix="viewhtmlmail-", delete=True
    ) as partfile:
        partfile.write(part.get_content().encode(part.get_charset() or "utf-8"))
        webbrowser.open(partfile.name)

        # give the browser some time to open the HTML file before it gets
        # deleted
        sleep(0.25)
