import mockcli


def main():
    result = mockcli.__name__
    expected = "mockcli"
    if result == expected:
        print("Smoke test: PASSED")
    else:
        raise RuntimeError("Smoke test: FAILED")


if __name__ == "__main__":
    main()
