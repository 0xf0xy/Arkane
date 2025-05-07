"""
MIT License

Copyright (c) 2025 0xf0xy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from importlib.resources import files
from rich import print
import json


class Arkane:
    """
    Arkane: Reverse and bind shell generator.
    """

    def __init__(self):
        """Initialize Arkane and load the configuration."""
        self._load_config()

    def _load_config(self):
        """
        Load data from the JSON file.

        Sets payloads.
        """
        with files("arkane.data").joinpath("payloads.json").open("r") as f:
            self.payloads = json.load(f)

    def list_payloads(self):
        """
        List all available payloads.
        """
        print("[bold blue]*[/bold blue] Available Payloads:")

        for lang, shells in self.payloads.items():
            print(f"\n[bold blue]{lang.upper()}[/bold blue]:")
            for shell_type, protocols in shells.items():
                protocols_list = ", ".join(protocols.keys())
                print(
                    f"  [bold white]{shell_type.capitalize()}[/bold white] ➜ [green]{protocols_list}[/green]"
                )

    def generate_shell(self, lang: str, shell: str, protocol: str, ip: str, port: int):
        """
        Formats and displays payloads.
        """
        try:
            generated_shell = self.payloads[lang][shell][protocol].format(
                ip=ip, port=port
            )
            print(
                f"[bold blue]*[/bold blue] Payloads for: [bold blue]{lang}, {shell}, {protocol}[/bold blue]\n"
            )
            print(
                f"[bold green]+[/bold green] [bold white]{generated_shell}[/bold white]"
            )

        except KeyError:
            print(
                f"[bold red]-[/bold red] Payload not found for language: {lang}, shell: {shell}, protocol: {protocol}"
            )
            self.list_payloads()
