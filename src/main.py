import argparse

from search import searchFromWiki


def searchWithOutput(query: str):
    print(f"正在查询: {query} ...")
    print("================================================================")

    dataList = searchFromWiki(query)

    for item in dataList:
        print("%-10s %s" % (item.get("id", ""), item.get("title", "")))
        print("____________________________________________________________")


def main() -> None:
    parser = argparse.ArgumentParser(description="Search anything in minecraft")
    parser.add_argument(
        "--query",
        "-q",
        type=str,
        help="Your query.",
    )
    args = parser.parse_args()

    if not args.query:
        while True:
            query = input("请输入你要查询的词或输入 over 以结束: ")
            if query == "over":
                print("谢谢使用,正在结束...")
                break

            searchWithOutput(query)
    else:
        query = args.query
        searchWithOutput(query)


if __name__ == "__main__":
    main()
