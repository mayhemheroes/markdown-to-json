#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    import markdown_to_json

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)

    ast = markdown_to_json.CommonMark.DocParser().parse(fdp.ConsumeRemainingString())
    dictionary = markdown_to_json.CMarkASTNester().nest(ast)
    dict(markdown_to_json.Renderer().stringify_dict(dictionary))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
