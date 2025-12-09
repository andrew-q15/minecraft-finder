from .search import searchFromWiki


def main() -> None:
    while True:
        query = input("请输入你要查询的词或输入over以结束: ")
        if query == "over":
            print("谢谢使用,正在结束...")
            break

        print(f"正在查询: {query} ...")
        print("================================================================")

        dataList = searchFromWiki(query)

        for item in dataList:
            print("%-10s %s" % (item.get("id", ""), item.get("title", "")))
            print("____________________________________________________________")


if __name__ == "__main__":
    main()
