#!/usr/bin/env python3
import os
import re
import urllib.parse
import sys

# Define root of the workspace
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# Directories to exclude from linting
EXCLUDED_DIRS = {".git", ".claude", "node_modules", ".gemini"}

def check_file_integrity(file_path):
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # State variables for character parsing
    in_block = False
    in_inline = False
    block_start_line = 0
    inline_start_line = 0

    lines = content.splitlines()
    for line_idx, line in enumerate(lines, 1):
        i = 0
        while i < len(line):
            # Handle escaped dollar signs
            if line[i:i+2] == '\\$':
                i += 2
                continue

            # Handle block math ($$)
            if line[i:i+2] == '$$':
                if in_inline:
                    errors.append(f"Line {line_idx}: Block math delimiter '$$' found inside inline math")
                in_block = not in_block
                if in_block:
                    block_start_line = line_idx
                i += 2
            # Handle inline math ($)
            elif line[i] == '$':
                # Check if this $ is acting as a currency symbol or template placeholder
                suffix = line[i:]
                is_currency = False
                
                # $ followed by digits (e.g. $50k)
                if re.match(r'\$\d', suffix):
                    is_currency = True
                # $ followed by underscores, backslashes, or spaces and then another underscore (e.g. $___, $\_____)
                elif re.match(r'\$[\s\\_]*_', suffix):
                    is_currency = True
                # $ followed by bracketed variables (e.g. $[Y] or $\[Y\])
                elif re.match(r'\$\\?\[[a-zA-Z]\\?\]', suffix):
                    is_currency = True

                if is_currency:
                    i += 1  # Skip currency symbol
                else:
                    if in_block:
                        errors.append(f"Line {line_idx}: Inline math delimiter '$' found inside block math")
                    in_inline = not in_inline
                    if in_inline:
                        inline_start_line = line_idx
                    i += 1
            else:
                i += 1
        
        # In this repository, inline math always closes on the same line.
        if in_inline:
            errors.append(f"Line {line_idx}: Unclosed inline math ($) on this line")
            in_inline = False  # Reset state to avoid cascading errors in the file

    if in_block:
        errors.append(f"Unclosed block math ($$) starting on line {block_start_line}")

    # 3. Link validity checks
    # Regex to find links like [text](destination)
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    for match in link_pattern.finditer(content):
        link_text = match.group(1)
        link_dest = match.group(2).strip()

        # Skip standard web URLs and mail links
        if link_dest.startswith(('http://', 'https://', 'mailto:', 'ftp:')):
            continue
        
        # Skip local document anchors
        if link_dest.startswith('#'):
            continue

        # Clean prefix and anchors
        clean_dest = link_dest
        
        # Handle absolute path prefixes
        if clean_dest.startswith(f'file://{WORKSPACE_DIR}'):
            clean_dest = clean_dest.replace(f'file://{WORKSPACE_DIR}', '')
        elif clean_dest.startswith('file://'):
            # Allow validation of other local files (like artifacts)
            clean_dest = clean_dest.replace('file://', '')

        # Remove trailing anchors
        if '#' in clean_dest:
            clean_dest = clean_dest.split('#')[0]

        # URL decode
        clean_dest = urllib.parse.unquote(clean_dest)

        # Skip validation if the target is purely empty or points to nothing
        if not clean_dest:
            continue

        # Resolve path
        if os.path.isabs(clean_dest) or clean_dest.startswith('/'):
            if os.path.exists(clean_dest):
                resolved_path = clean_dest
            else:
                resolved_path = os.path.join(WORKSPACE_DIR, clean_dest.lstrip('/'))
        else:
            # If relative, resolve relative to the file's current directory
            resolved_path = os.path.abspath(os.path.join(os.path.dirname(file_path), clean_dest))

        # Check if file exists
        if not os.path.exists(resolved_path):
            errors.append(f"Broken link: '{link_dest}' (resolved to '{resolved_path}')")

    return errors

def main():
    print("=" * 60)
    print("Starting Playbook Link & LaTeX Integrity Validator...")
    print(f"Workspace: {WORKSPACE_DIR}")
    print("=" * 60)

    total_files_scanned = 0
    files_with_errors = 0
    total_errors = 0

    for root, dirs, files in os.walk(WORKSPACE_DIR):
        # Prune excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, WORKSPACE_DIR)
                total_files_scanned += 1

                file_errors = check_file_integrity(file_path)
                if file_errors:
                    files_with_errors += 1
                    total_errors += len(file_errors)
                    print(f"\n❌ [ERROR] In {relative_path}:")
                    for err in file_errors:
                        print(f"   - {err}")

    print("\n" + "=" * 60)
    print("Scan Summary:")
    print(f"- Total files scanned: {total_files_scanned}")
    print(f"- Files with errors: {files_with_errors}")
    print(f"- Total error count: {total_errors}")
    print("=" * 60)

    if total_errors > 0:
        sys.exit(1)
    else:
        print("✅ All markdown files passed Link and LaTeX validation successfully!")
        sys.exit(0)

if __name__ == '__main__':
    main()
