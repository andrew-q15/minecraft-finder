import requests


def main() -> None:
    while True:
        query = input("请输入你要查询的词或输入over以结束: ")
        if query == "over":
            print("谢谢使用,正在结束...")
            break
        print(f"正在查询: {query} ...")
        print("================================================================")
        response = requests.get(
            f"https://minecraft.wiki/rest.php/v1/search/page?format=json&limit=5&q={query}"
        )
        data = response.json()
        dataList = data.get("pages", [])
        for item in dataList:
            print("%-10s %s" % (item.get("id", ""), item.get("title", "")))
            print("____________________________________________________________")


if __name__ == "__main__":
    main()
