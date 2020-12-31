# Digital land

This repo renders the [main (and some small) sections on the digital land site](https://digital-land.github.io/).

## Working with repo

Install dependencies (we recommend working in a virtualenv)

    make init

Render pages

    make render

### Helpful frontmatter properties

**`external_url`** - add a url to an external source. The page will redirect to this url. Useful if blog posts are hosted on another domain.

**`show_summaries`** - default False. Set to True if you'd like the list page to preview the content pages. The summary for each will be either the first sentence or the `summary` set in the page frontmatter.