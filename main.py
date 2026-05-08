import os

def main():
    name = os.getenv("USERNAME")
    print(f"Hola ¿qué tal, {name}? Te saluda Python.")


if __name__ == "__main__":
    main()