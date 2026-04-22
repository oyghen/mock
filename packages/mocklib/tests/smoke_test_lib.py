import mocklib


def main() -> None:
    result = mocklib.__name__
    expected = "mocklib"
    if result == expected:
        print(f"Smoke test for {mocklib.__name__}: PASSED")
    else:
        raise RuntimeError(f"Smoke test for {mocklib.__name__}: FAILED")


if __name__ == "__main__":
    main()
