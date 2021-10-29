"""
Command Line Interface
=======================
"""
import click
from .sample import SampleClass


@click.command()
def main():
    """Main CLI command"""
    sample = SampleClass()
    sample.print("Hola")
