scriptencoding utf-8

" Insert a vw wiki link for article title under the cursor
" For example: [My Article] -> [My Article](my_article.md)
" NOTE: Everything character pair starting with a ^ should be a control sequence
" If you need to retype them yourself in insert mode:
" <C-V><C-[> for ^[ (for example)
noremap <leader>i :normal! vi[yf]a(pa.md)vi(ugv:%s/\%V /_/ggv
