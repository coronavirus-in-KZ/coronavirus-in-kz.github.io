#!/usr/bin/env python

# %%
import pandas as pd
from yattag import Doc, indent

# %%
corona_df = pd.read_excel(io="coronavirus.xlsx", header=0)

# %%
doc, tag, text = Doc().tagtext()

# %%
with tag("html"):
    with tag("head"):
        doc.stag(
            "link",
            rel="stylesheet",
            type="text/css",
            href="styles.css",
            media="screen",
        )

    with tag("body"):
        # TODO добавить <caption>
        with tag("table", border="1", klass="big_table"):
            headers = list(corona_df)
            for header in headers:
                with tag("th"):
                    text(str(header))

            rows = corona_df.values.tolist()
            for row in rows:
                with tag("tr"):
                    if "зараженные" in row:
                        for cell in row:
                            with tag("td"):
                                if isinstance(cell, str):
                                    if cell == "-":
                                        doc.attr(klass="center")
                                    else:
                                        doc.attr(klass="left")
                                elif cell > 0:
                                    doc.attr(klass="right red")
                                elif cell == 0:
                                    doc.attr(klass="right green")
                                text(cell)
                    else:
                        for cell in row:
                            with tag("td"):
                                if isinstance(cell, str):
                                    if cell == "-":
                                        doc.attr(klass="center")
                                    else:
                                        doc.attr(klass="left")
                                elif cell > 0:
                                    doc.attr(klass="right")
                                elif cell == 0:
                                    doc.attr(klass="right")
                                text(cell)

result_html = indent(doc.getvalue())
with open(file="index.html", mode="w") as f_html:
    print(result_html, file=f_html)

# %%
row


# %%
