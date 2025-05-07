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

from arkane.core import Arkane
import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Arkane: Reverse and bind shell generator", add_help=False
    )

    connection = parser.add_argument_group("Connection Settings")
    connection.add_argument("host", help="IP address for the connection")
    connection.add_argument(
        "-p", "--port", default=4444, help="Port to use (default: 4444)"
    )

    shell = parser.add_argument_group("Shell Settings")
    shell.add_argument("-s", "--shell", type=str.lower, help="Shell type to generate")
    shell.add_argument(
        "-l", "--lang", type=str.lower, required=True, help="Shell language to generate"
    )

    protocol = parser.add_argument_group("Protocol")
    protocol.add_argument(
        "-c",
        "--connection",
        type=str.upper,
        default="TCP",
        help="Connection protocol (TCP or UDP)",
    )

    meta = parser.add_argument_group("Help & Version")
    meta.add_argument("-h", "--help", action="help", help="Show this menu")
    meta.add_argument(
        "-v",
        "--version",
        action="version",
        version="Arkane v1.0.0",
        help="Show program version",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    arkane = Arkane()

    arkane.generate_shell(
        args.lang,
        args.shell,
        args.connection,
        args.host,
        args.port,
    )
