from dataclasses import dataclass
import re
from typing import Generator

@dataclass
class File:
    name: str
    size: int

@dataclass 
class Directory:
    name: str
    parent: 'Directory'
    dirs: 'list[Directory]'
    files: 'list[File]'

    def __init__(self, name: str, parent: 'Directory') -> None:
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def size(self) -> int:
        return sum([dir.size() for dir in self.dirs]) + sum([file.size for file in self.files])

    def filter(self, filter_func: 'function') -> 'Generator[Directory]':
        if filter_func(self) == True:
            yield self
        for child in self.dirs:
            if filter_func(child) == True:
                yield child

    def filter_deep(self, filter_func: 'function') -> 'Generator[Directory]':
        if filter_func(self) == True:
            yield self
        for child in self.dirs:
            yield from child.filter_deep(filter_func)

    def __contains__(self, name: str):
        return next(self.filter(lambda x: x.name == name), None) is not None

def fser(cli_log: str) -> int:
    file_tree = Directory('/', None)
    pwd = file_tree

    cmd_mode = None
    for line in cli_log.splitlines():
        # commands start with $, and mark the end of cmd_mode
        cmd_match = re.match(r'\$ (\w*)', line)
        if cmd_match is not None:
            cmd_mode = None
            if cmd_match.group(1) == 'cd':
                # assume the dir exists; document a dir
                dir_name = line[5:]
                if dir_name == '..':
                    if pwd.parent is not None:
                        pwd = pwd.parent
                else:
                    if dir_name not in pwd:
                        pwd.dirs.append(Directory(dir_name, pwd))
                    pwd = next(pwd.filter(lambda x: x.name == dir_name))
            elif cmd_match.group(1) == 'ls':
                cmd_mode = 'ls'
        elif cmd_mode == 'ls':
            ls_match = re.match(r'(.*) (.*)', line)
            [size, name] = ls_match.group(1, 2)
            # document files and dirs
            if size == 'dir':
                if dir_name not in pwd:
                    pwd.dirs.append(Directory(dir_name))
            else:
                # assume a file
                pwd.files.append(File(name, int(size)))
    # pprint(file_tree)
    # ok, now that we have a tree, get dirs with size < 100_000, and get their sizes
    return sum([dir.size() for dir in file_tree.filter_deep(lambda x: x.size() < 100_000)])
