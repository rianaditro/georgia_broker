import typer

app = typer.Typer()

from scrap import get_html


@app.command("scrap", help="Scraping")
def generate_html(url):
    html = get_html(url=url)


