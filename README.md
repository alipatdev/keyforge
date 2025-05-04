# KeyForge  
Secure Password Generator CLI Tool

KeyForge is a simple, cross-platform command-line utility for generating strong, random passwords. It is ideal for developers and users who need to quickly generate secure credentials from the terminal.

---

## ✨ Features

- Customizable password length
- Generate multiple passwords at once
- Choose which character types to include (uppercase, lowercase, digits, symbols)
- Lightweight – no external dependencies beyond Python 3.6+

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/youruser/keyforge.git
cd keyforge
```

### 2. Install in Editable Mode (Recommended for Developers)

This installs the tool locally and creates a globally accessible `keyforge` command.

```bash
pip3 install --user -e .
```

> The `--user` flag installs it to your user environment.  
> The `-e .` flag enables editable mode, so changes to the code take effect immediately.

---

## 🧭 Make Sure It's in Your PATH

After installation, the `keyforge` command is placed in:

- `~/.local/bin` (on macOS/Linux)
- `%APPDATA%\\Python\\PythonXY\\Scripts` (on Windows)

Ensure that directory is in your `PATH`.

To add `~/.local/bin` to your PATH on macOS/Linux:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

You can now run:

```bash
keyforge --help
```

---

## 🌐 Global Installation (Optional)

To install globally for all users (requires admin rights):

```bash
sudo pip3 install .
```

This places the `keyforge` binary in `/usr/local/bin`.

---

## 🚀 Usage

```bash
# Display help
keyforge --help

# Generate 3 passwords, each 20 characters long
keyforge -l 20 -n 3

# Generate 2 passwords without symbols
keyforge -l 12 -n 2 --no-symbols

# Generate passwords using only lowercase and digits
keyforge -l 16 --no-upper --no-symbols
```

---

## 🔧 Command Line Options

```
usage: keyforge [-h] [-l LENGTH] [-n COUNT] [--no-symbols] [--no-numbers]
                [--no-upper] [--no-lower] [--version]

KeyForge: Secure password generator CLI tool

optional arguments:
  -h, --help            Show this help message and exit
  -l LENGTH, --length LENGTH
                        Password length (default: 16)
  -n COUNT, --count COUNT
                        Number of passwords to generate (default: 1)
  --no-symbols          Exclude punctuation symbols
  --no-numbers          Exclude digits
  --no-upper            Exclude uppercase letters
  --no-lower            Exclude lowercase letters
  --version             Show the program's version number and exit
```

---

## 🧑‍💻 Development

If you want to contribute:

1. Create a new branch:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make your changes, then commit:
   ```bash
   git commit -am "Add my feature"
   ```

3. Push and open a Pull Request:
   ```bash
   git push origin feature/my-feature
   ```

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for more details.
