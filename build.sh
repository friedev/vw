#!/bin/sh
set -eu
export PATH='/bin:/sbin:/usr/bin:/usr/local/bin'

md_dir=md
html_dir=html

cd "$(dirname "$0")" || exit 1

rm -rf "$html_dir"
mkdir -p "$html_dir"
for md_file in "$md_dir"/*; do
	md_filename=$(basename "$md_file")
	filename=${md_filename%.*}
	html_filename=$filename.html
	html_file=$html_dir/$html_filename
	sed 's/\.md)/\.html)/g' < "$md_file" | lowdown -o "$html_file"
done

exit 0
