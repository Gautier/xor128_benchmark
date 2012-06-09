import csv
import subprocess
import sys


TESTS = (("pypy_inline", ("pypy", "xor_inline.py")),
         ("pypy_idiomatic", ("pypy", "xor_idiomatic.py")),
         ("pypy_idiomatic2", ("pypy", "xor_idiomatic2.py")),

         ("python_inline", ("python", "xor_inline.py")),
         ("python_idiomatic", ("python", "xor_idiomatic.py")),
         ("python_idiomatic2", ("python", "xor_idiomatic2.py")),

         ("node_inline", ("node", "xor_inline.js")),
         ("node_idiomatic", ("node", "xor_idiomatic.js")),

         ("go_inline", ("./xor_inline_go",)),
         ("go_idiomatic", ("./xor_idiomatic_go",)),

         ("c_inline", ("./xor_inline_c",)),
         ("c_idiomatic", ("./xor_idiomatic_c",)),
)


def check_compilers_and_interpreters():
    for p in ["gcc --version",
              "python --version",
              "pypy --version",
              "go version"]:
        try:
            subprocess.call(p.split(" "),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        except OSError:
            print "This benchmark needs %s to return sucessfully " % p
            return False

    return True

def compile_go():
    subprocess.call("go build -o xor_inline_go xor_inline.go", shell=True)
    subprocess.call("go build -o xor_idiomatic_go xor_idiomatic.go", shell=True)

def compile_c():
    subprocess.call("gcc -O3 -o xor_inline_c xor_inline.c", shell=True)
    subprocess.call("gcc -O3 -o xor_idiomatic_c xor_idiomatic.c", shell=True)


def run_tests(test_values):
    tests = []

    for n in test_values:
        test_run = []
        for test_name, test_command in TESTS:
            test_result = subprocess.check_output(test_command + (n,))
            test_run.append(int(test_result.replace("\n", "")))
        tests.append(test_run)

    return tests


def display_results(test_values, tests):
    headers = [test_name for test_name, test_command in TESTS]

    print "%10s |" % "n",
    for header in headers:
        print "%10s |" % header[:10],
    print

    for n, results in zip(test_values, tests):
        print "%10d |" % int(n),
        for result in results:
            print "%10d |" % result,
        print


def save_results(test_values, tests):
    headers = [test_name for test_name, test_command in TESTS]

    with open("results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["n"] + headers)
        for n, results in zip(test_values, tests):
            writer.writerow([n] + results)


def main():
    if len(sys.argv) < 2:
        print "usage: python comparator.py TEST_N1 TEST_N2 ..."
        return

    test_values = sys.argv[1:]

    if not check_compilers_and_interpreters():
        return

    compile_go()
    compile_c()

    tests_results = run_tests(test_values)

    display_results(test_values, tests_results)
    save_results(test_values, tests_results)

if __name__  == "__main__":
    main()
