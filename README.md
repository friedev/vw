# vw

vw (vim wiki) is yet another system for maintaining a simple personal wiki using vim and markdown.

vw is not a single piece of software, but rather a process and a small collection of tools.
A vw wiki is a collection of markdown files in a directory that link to one another.
Each file represents an article in the wiki.
The name of each file should be the article title converted to lowercase, with spaces converted to underscores, and with the `.md` file extension.

## Dependencies

- [lowdown](https://kristaps.bsd.lv/lowdown/)

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

Vim provides some useful built-in keybinds that you can use to navigate the wiki.
To open a link in a new buffer, move the cursor over it and type `gf`.
To open an external link in the proper program (like your browser), type `gx` instead.

## Link Generation

To speed up editing, you can use the following vim macro to insert the link corresponding to an article title.
For example, if you typed `[My Article]`, running the macro would yield `[My Article](my_article.md)`.

```
vi[yf]a(^[pa.md)^[vi(ugv:^U%s/\%V /_/g^Mgv^[:nohlsearch^M
```

You can use this macro as a macro:

```vim
let @i='vi[yf]a(^[pa.md)^[vi(ugv:^U%s/\%V /_/g^Mgv^[:nohlsearch^M'
```

Or, you can create a custom keybinding for it:

```vim
noremap <leader>i :normal! vi[yf]a(^[pa.md)^[vi(ugv:^U%s/\%V /_/g^Mgv^[:nohlsearch^M
```

**NOTE:** Every character pair starting with `^` (e.g. `^[`, `^M`) is an escape sequence.
To retype them yourself in insert mode, do `<C-V><C-[>` for `^[` (for example).

If you don't like this (admittedly disgusting) macro solution, check out the [vim-markdown-wiki](https://github.com/mmai/vim-markdown-wiki) plugin, which provides similar functionality in the form of a Vim script plugin.

## Alternatives

There are a lot of similar projects that attempt to solve the same problem as vw (ranked roughly in order of similarity to vw):

- [vim-markdown-wiki](https://github.com/mmai/vim-markdown-wiki)
- [wiki.vim](https://github.com/lervag/wiki.vim)
- [Vim-Waikiki](https://github.com/fcpg/vim-waikiki)
- [SoyWiki](https://github.com/danchoi/soywiki) (unmaintained)
- [vimwiki](https://vimwiki.github.io/)
