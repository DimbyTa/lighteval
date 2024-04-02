#!/usr/bin/env python

# MIT License

# Copyright (c) 2024 Taratra D. RAHARISON

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import importlib
import json
import os
import pkg_resources

def list_tasks_command():
    """
    List all the avalaible tasks in tasks_table.jsonl and the extended directory
    Assumes the existence of TASKS_TABLE in the main.py file for each extended 
    tasks in tasks/extended
    """
    try:
        tasks = []
        # Handling tasks_table.jsonl
        # Get the path to the resource file
        tasks_table_path = pkg_resources.resource_filename('lighteval', 'tasks/tasks_table.jsonl')
        print(tasks_table_path)
        #with open('./src/lighteval/tasks/tasks_table.jsonl') as jsonl_tasks_table:
        with open(tasks_table_path) as jsonl_tasks_table:
            for jline in jsonl_tasks_table.splitlines():
                tasks.append(json.loads(jline))
        
        # Handling extend tasks
        #root_dir = "./src/lighteval/tasks/extended"
        #tasks_extended = []
        #for root, dirs, files in os.walk(root_dir):
            #for file in files:
                #if file == 'main.py':
                    #main_path = os.path.join(root, file)
                    #module_name = os.path.basename(root)
                    #spec = importlib.util.spec_from_file_location(module_name, main_path)
                    #module = importlib.util.module_from_spec(spec)
                    #spec.loader.exec_module(module)
                    #if hasattr(module, 'TASKS_TABLE'):
                        #tasks_extended += module.TASKS_TABLE
        #tasks += tasks_extended
        if len(tasks) > 0:
            print("Avalaible tasks: ")
            for task in tasks:
                print("- " + task["name"])

    #except FileNotFoundError:
    except Exception as e:
        print('Error: tasks_table.jsonl file not found. ', e)


def main():
    parser = argparse.ArgumentParser(description='CLI tool for lighteval, a lightweight framework for LLM evaluation')
    parser.add_argument('--list-tasks', action='store_true', help='List available tasks')
    args = parser.parse_args()

    if args.list_tasks:
        list_tasks_command()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
