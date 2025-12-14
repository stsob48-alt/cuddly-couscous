from IPython.display import display, HTML


def side_by_side(*dfs, captions=None, margin_right="2em"):
    """
    Displays multiple pandas DataFrames side-by-side using HTML/CSS.

    *dfs: Variable number of DataFrames to display.
    captions: List of captions for each DataFrame (optional).
    margin_right: CSS margin for spacing between tables.
    """

    # Initialize the HTML string with a flex container
    html_str = '<div style="display:flex; justify-content:space-around;">'

    # Create an iterator for captions
    if captions is None:
        captions = [""] * len(dfs)

    # Iterate through DataFrames and captions
    for df, caption in zip(dfs, captions):
        # Convert DataFrame to HTML
        df_html = df.to_html()

        # Add an optional caption
        if caption:
            caption_tag = f'<figcaption style="text-align: center; font-weight: bold;">{caption}</figcaption>'
        else:
            caption_tag = ""

        # Wrap the caption and table in a div with a right margin for spacing
        html_str += f"""
            <figure style="margin: 0; margin-right: {margin_right};">
                {caption_tag}
                {df_html}
            </figure>
        """

    # Close the root div
    html_str += "</div>"

    # Display the HTML
    display(HTML(html_str))
