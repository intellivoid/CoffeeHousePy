import sys

from resource_fetch import ResourceFetch


def main():
    resource_fetcher = ResourceFetch()
    if len(sys.argv[1:]) > 0:
        resource_fetcher.define_pat(sys.argv[1])
    else:
        resource_fetcher.define_pat(input("Personal Access Token: "))
    print("The Personal Access Token has been successfully defined")


if __name__ == '__main__':
    main()
