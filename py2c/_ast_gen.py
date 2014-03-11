#! /usr/bin/env python
"""AST nodes file generator

This file generates the ast that we use as the meduim to translate Python code.
It makes it possible to translate Python code to C code without multiple AST
systems.
"""
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

from textwrap import dedent
import ply.lex
import ply.yacc

_PREFIX = dedent("""
""").strip()


class Node(object):
    """Represents a definition in the AST definitions
    """
    def __init__(self, name, parent=None, attrs=None):
        super(Node, self).__init__()
        self.name = name
        self.parent = parent
        self.attrs = attrs


class Parser(object):
    """Parses the definitions in the configuration files
    """
    def __init__(self):
        super(Parser, self).__init__()

    def remove_comments(self, text):
        return text

    def parse(self, text):
        return []


class SourceGenerator(object):
    """Generates the code from the Parser's parsed data
    """
    def __init__(self):
        super(SourceGenerator, self).__init__()

    def generate_sources(self, data):
        """Generates source code from the data generated by :py:class:`Parser`
        """
        return ""


# API for dual_ast
def generate(base_dir, fname, files_to_convert):
    pass