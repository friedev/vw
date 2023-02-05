#!/bin/sh
export PATH='/bin:/sbin:/usr/bin:/usr/local/bin'

vw_help() {
	cat << EOF
usage: $0 <command>

commands:
incoming <file>  list articles that link to this article
outgoing <file>  list articles that this article links to
orphans          list articles with no incoming links
missing          list links leading to nonexistent pages
EOF
}

vw_incoming() {
	grep --color=auto -r "]($1)"
}

vw_outgoing() {
	grep --color=auto -E "\]\([^\)]+\.md\)" "$1"
}

vw_orphans() {
	for f in *; do
		if ! grep -q -r "]($f)"; then
			echo "$f"
		fi
	done
}

vw_missing() {
	for f in *; do
		grep -E -o "\]\([^\)]+\.md\)" "$f" |
			sed -E "s/\]\(([^\)]+\.md)\)/\1/" |
			while read -r link; do
				if [ ! -f "$link" ]; then
					echo "$f: $link"
				fi
			done
	done
}

if [ "$#" -lt 1 ]; then
	vw_help
	exit 1
fi

case "$1" in
	incoming)
		vw_incoming "${2:?usage: $0 incoming <file>}"
		;;
	outgoing)
		vw_outgoing "${2:?usage $0 outgoing <file>}"
		;;
	orphans)
		vw_orphans
		;;
	missing)
		vw_missing
		;;
	*)
		vw_help
		;;
esac

exit 0
