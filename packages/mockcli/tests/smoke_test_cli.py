import mockcli


def main():
    result = mockcli.__name__
    expected = "mockcli"
    if result == expected:
        print(f"Smoke test for {mockcli.__name__}: PASSED")
    else:
        raise RuntimeError(f"Smoke test for {mockcli.__name__}: FAILED")


if __name__ == "__main__":
    main()
