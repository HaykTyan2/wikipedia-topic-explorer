import src.scraper as scraper
import src.parser as parser


def crawl(start_url, max_depth, max_pages):
  visited = set()
  to_visit = [(start_url, 0)]

  while to_visit and len(visited) <= max_pages:
    url, depth = to_visit.pop(0)
    
    if url in visited or depth > max_depth:
      continue

    visited.add(url)
    print(f"Visited URL: {url}")
    
    html = scraper.fetch_page(url)
    links = parser.extract_links(html)

    for link in links[:5]:
      full_url = "https://en.wikipedia.org" + link
      to_visit.append((full_url, depth + 1))

  return visited

# visited = ()
# to_visit = [(y,1),(z,1)]


















# def crawl(start_url, max_depth, max_pages):

#   visited = set()
#   to_visit = [(start_url, 0)]

#   while to_visit and len(visited) < max_pages:
#     url , depth = to_visit.pop(0)
#     #(x,1)
#     if url in visited or depth > max_depth:
#        continue
    
#     visited.add(url)
#     print(f"Depth: [{depth}] Visiting: {url}")
    
#     html = scraper.fetch_page(url)
#     links = parser.extract_links(html)

#     for link in links[:2]:
#         full_url = "https://en.wikipedia.org" + link
#         to_visit.append((full_url, depth + 1))