from itertools import count
from python_graphql_client import GraphqlClient
import csv
import feedparser
import httpx
import json
import pathlib
import re
import os
import time

root = pathlib.Path(__file__).parent.resolve()
client = GraphqlClient(endpoint="https://api.github.com/graphql")

TOKEN = os.environ.get("SIMONW_TOKEN", "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")


def replace_chunk(content, marker, chunk):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


def make_query(after_cursor=None):
    return """
query {
  search(first: 100, type: REPOSITORY, query: "topic:php stars:0", after: AFTER) {
    repositoryCount
    pageInfo {
      startCursor
      hasNextPage
      endCursor
    }
    nodes {
      ... on Repository {
        name
        url
        description
        stargazerCount
        forkCount
        
      }
    }
  }
}
""".replace(
        "AFTER", '"{}"'.format(after_cursor) if after_cursor else "null"
    )


def fetch_releases(oauth_token):
    repos = []
    releases = []
    repo_names = set()
    has_next_page = True
    after_cursor = None
    counter = 1

    while has_next_page:
        data = client.execute(query=make_query(after_cursor),headers={"Authorization": "Bearer {}".format(oauth_token)})
        for repo in data["data"]["search"]["nodes"]:
          repos.append(repo)
          repo_names.add(repo["name"])
          # releases.append("{},{},'{}',{},{}".format(repo["name"],repo["url"],repo["description"],repo["stargazerCount"],repo["forkCount"]))
          releases.append([repo["name"],repo["url"],repo["stargazerCount"],repo["forkCount"]])
        has_next_page = data["data"]["search"]["pageInfo"]["hasNextPage"]
        after_cursor = data["data"]["search"]["pageInfo"]["endCursor"]
        print(after_cursor)
        # if counter == 3:
        #   return releases
        # counter = counter + 1
    return releases


if __name__ == "__main__":
    releases = fetch_releases(TOKEN)
    # for line in releases:
    #   print(line)
    with open('php.csv', 'a', newline='') as f:
      wr = csv.writer(f, dialect='excel')
      for line in releases:
        wr.writerow(line)
      f.close()
    