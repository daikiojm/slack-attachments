import urllib.request

def main():
    with urllib.request.urlopen("http://www.yoheim.net") as res:
        html = res.read().decode("utf-8")
        print(html)


if __name__ == '__main__':
    main()
