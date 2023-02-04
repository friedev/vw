# vw

vw (vim wiki) is yet another system to create and manage a simple personal wiki using vim and markdown.

A vw wiki is a collection of markdown files in a directory that link to one another.

## Quick Start

Clone vw.

```
git clone https://frie.dev/vw.git
```

Create a new directory for your wiki.

```
mkdir my_wiki
cd my_wiki
```

Copy the build script `build.sh` into your wiki.

```
cp ../vw/build.sh .
```

Create and edit some markdown files.

```
mkdir md
vi md/home.md md/vw.md md/vim.md
```

Compile to HTML.

```
./build.sh
```

## Navigation

To create links between pages, use the normal markdown syntax.

```md
[vw](vw.md) is a tool for creating wikis.
```

To follow a link in vim, move the cursor over it and type `gf`.
