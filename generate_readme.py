#!/usr/bin/env python

# %%
import pandas as pd
from yattag import Doc

# %%
corona_df = pd.read_excel(io="coronavirus.xlsx", header=0)

# %%
doc, tag, text = Doc().tagtext()

# %%
with tag("table", border=1):
    headers = list(corona_df)
    for header in headers:
        with tag("th"):
            text(str(header))

    rows = corona_df.values.tolist()
    for row in rows:
        with tag("tr"):
            if "зараженные" in row:
                for cell in row:
                    if isinstance(cell, str):
                        with tag("td", align="center"):
                            text(cell)
                    elif cell > 0:
                        with tag("td", align="right", bgcolor="red"):
                            text(cell)
                    elif cell == 0:
                        with tag("td", align="right", bgcolor="green"):
                            text(cell)
            else:
                for cell in row:
                    if isinstance(cell, str):
                        with tag("td", align="center"):
                            text(cell)
                    elif cell > 0:
                        with tag("td", align="right"):
                            text(cell)
                    elif cell == 0:
                        with tag("td", align="right"):
                            text(cell)

with open(file="test.html", mode="w") as f_html:
    print(doc.getvalue(), file=f_html)

# %%
row


# %%
