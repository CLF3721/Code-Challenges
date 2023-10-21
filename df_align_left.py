#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
@File      :   df_left_align.py
@Time      :   2021/04/18 12:28:13
@Author    :   CLF
@CoAuthor  :   --
@Version   :   1.0
@Contact   :   https://www.linkedin.com/in/clf3721
@License   :   (C)Copyright 2021, CLF
@Desc      :   --
'''


###~~~~~~~~~~~~~~~~>
###~> Dependencies
###~~~~~~~~~~~~~~~~>
#*IPython HTML dependencies: pip install ipython jinja2



###~~~~~~~~~~~~~>
###~> Imports
###~~~~~~~~~~~~~>
from IPython.display import display, HTML



###~~~~~~~~~~~~~>
###~> Function
###~~~~~~~~~~~~~>
def align_dataframe_left(df):
    """
    Render the styled DataFrame to HTML, then display the HTML representation.
    """
    styler = df.style.set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'left')]},  #Style for header cells
        {'selector': 'td', 'props': [('text-align', 'left')]}   #Style for data cells
    ])
    styled_html = styler.to_html()
    display(HTML(styled_html))