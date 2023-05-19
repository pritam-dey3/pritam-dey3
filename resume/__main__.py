from resume.contents.compile import compile
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a function name.")
        sys.exit(1)

    function_name = sys.argv[1]

    if function_name == "compile":
        compile()
    else:
        print(f"Function '{function_name}' not found.")
        sys.exit(1)
