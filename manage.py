import subprocess


def run_flask():
    try:
        subprocess.run(["flask", "run", "--debug"], check=True)

    except subprocess.CalledProcessError as e:
        print("Error occurred when running", e)


if __name__ == "__main__":
    run_flask()
