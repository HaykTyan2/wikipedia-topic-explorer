def is_valid_article(href: str) -> bool:

    if not href.startswith("/wiki/"):
        return False

    # Exclude Main Page and special namespaces like File:, Help:, Category:
    invalid_prefixes = [
        "/wiki/Main_Page",
        "/wiki/File:",
        "/wiki/Help:",
        "/wiki/Category:",
        "/wiki/Special:",
        "/wiki/Talk:",
        "/wiki/Portal:",
        "/wiki/Template:",
    ]
    #so here we're basically utilizing "any" with the generator so that if the generator for the first time meets a "true" then we immediately return true.
    return not any(href.startswith(prefix) for prefix in invalid_prefixes)
