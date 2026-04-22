import mocklib


def main() -> None:
    result = mocklib.__name__
    expected = "mocklib"
    if result == expected:
        print("Smoke test: PASSED")
    else:
        raise RuntimeError("Smoke test: FAILED")


if __name__ == "__main__":
    main()
