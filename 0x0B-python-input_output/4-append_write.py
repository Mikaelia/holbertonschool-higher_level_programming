#!/usr/bin/python3
def append_write(filename="", text=""):
    """appends string to text file and returns characters added"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
