#!/bin/bash

(command -v python3 >/dev/null 2>&1 &&
python3 -c 'import sys; sys.exit(sys.hexversion < 0x03050000)') || {
	echo >&2 "Newer version of python not found"
	exit 1;
}

cd "$(dirname "$BASH_SOURCE")"
python3 boot.by