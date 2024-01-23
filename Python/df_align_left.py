'''
Display dataframe content aligned left.

Dependencies:
pip install pandas numpy ipython jinja2

'''

###~~~~~~~~~~~>
###~> Imports
###~~~~~~~~~~~>
from IPython.display import display, HTML
import pandas as pd
import numpy as np



###~~~~~~~~~~~~>
###~> Function
###~~~~~~~~~~~~>
def align_dataframe_left(df):
    """
    Render the styled DataFrame to HTML
    Display the HTML representation.
    """
    styler = df.style.set_table_styles([
        {'selector': 'th', 'props': [('text-align', 'left')]}, #header
        {'selector': 'td', 'props': [('text-align', 'left')]}, #data
    ])
    styled_html = styler.to_html()
    display(HTML(styled_html))



###~~~~~~~~~~~>
###~> Example
###~~~~~~~~~~~>
# Create a 5x3 dataframe with random integers between 0 and 100
df = pd.DataFrame(np.random.randint(700000, 800000, size=(5, 3)), columns=["Col1", "Col2", "Col3"])

# Aligned right
print(df)

# Aligned left
print(align_dataframe_left(df))