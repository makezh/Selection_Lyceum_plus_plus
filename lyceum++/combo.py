def main():
    m, n = map(int, input().split(maxsplit=2))
    ans = (m - 2) * (m - 1) * m // 6 + m * n * (n - 1) // 2
    print(ans)


if __name__ == "__main__":
    main()
