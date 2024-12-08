#!/usr/bin/env python3
'''
OPS445 Assignment 2
Program: assignment2.py 
Author: "Joy Otchere"
Semester: "Fall 2024"

The python code in this file is original work written by
"Joy Otchere". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

'''

import argparse
import os, sys


def parse_command_args() -> object:
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts", epilog="Copyright 2023")
    
    # Add argument for graph length
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    
    # Add argument for human-readable format
    parser.add_argument("-H", "--human-readable", action="store_true", help="Print memory usage in human-readable format (e.g., MB, GB).")
    
    # Optional argument for a specific program
    parser.add_argument("program", type=str, nargs="?", help="If a program is specified, show memory use of all associated processes. Show only total use if not.")
    
    # Parse arguments
    args = parser.parse_args()
    return args


def percent_to_graph(percent: float, length: int=20) -> str:
    """
    Converts a percentage value into a string representation of that percentage.
    The string will consist of "#" symbols for the percentage, and spaces for the remaining portion.
    
    Parameters:
    percent (float): The percentage to represent as a graph.
    length (int): The total length of the graph.

    Returns:
    str: A string representation of the percentage.
    """
    # Ensure percent is within the 0-100 range
    if percent < 0:
        percent = 0
    elif percent > 100:
        percent = 100

    # Calculate the number of '#' symbols, ensuring it fits within the given length
    hashes = int(percent * (length - 1) / 100)  # Use (length - 1) to leave space for the final character
    spaces = length - hashes  # The remaining characters are spaces

    # Return the graph
    return "#" * hashes + " " * spaces






# percent to graph function

def get_sys_mem() -> int:
    """
    Returns the entire system memory (used or available) in kB.
    
    Obtains the entire amount of system memory from /proc/meminfo.
    
    Returns:
        int: Entire system memory in kB.
    """
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemTotal:"):
                return int(line.split()[1])
    return 0

def get_avail_mem() -> int:
    """
    Returns the memory that is currently available.
    
    Obtains the system memory that is available from /proc/meminfo.
    
    Returns:
        int: Available system memory in kB.
    """
    with open("/proc/meminfo", "r") as meminfo:
        for line in meminfo:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1])
    return 0

def pids_of_prog(app_name: str) -> list:
    "Given an app name, return all pids associated with the app using pidof"
    pids = []
    try:
        # Use os.popen to call the pidof command
        result = os.popen(f"pidof {app_name}").read().strip()
        
        # Check if the result is not empty
        if result:
            pids = result.split()  # Split the result by spaces to get individual PIDs
    except Exception as e:
        print(f"Error retrieving PIDs for {app_name}: {e}")
    return pids

def rss_mem_of_pid(proc_id: str = '74168') -> int:
    try:
        smaps_file = f"/proc/{proc_id}/smaps"
        total_rss = 0
        with open(smaps_file, 'r') as file:
            for line in file:
                print(f"Processing line: {line.strip()}")  # Debugging
                if line.startswith("VmRSS:"):
                    parts = line.split()
                    if len(parts) >= 2 and parts[1].isdigit():
                        total_rss += int(parts[1])
                        print(f"Added {parts[1]} KB to total RSS.")
        print(f"Total RSS calculated: {total_rss}")
        return total_rss
    except Exception as e:
        print(f"Error: {e}")
        return 0









def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    if not args.program:
        ...
    else:
        ...
    # process args
    # if no parameter passed, 
    # open meminfo.
    # get used memory
    # get total memory
    # call percent to graph
    # print

    # if a parameter passed:
    # get pids from pidof
    # lookup each process id in /proc
    # read memory used
    # add to total used
    # percent to graph
    # take total our of total system memory? or total used memory? total used memory.
    # percent to graph.
