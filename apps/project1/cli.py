from libs.lib1.utils import lib_method
import humanize


def main():
    print("abc")
    print("in project1.cli")
    print(lib_method("my text in pig latin"))
    print(humanize.apnumber(1))


if __name__ == "__main__":
    main()
