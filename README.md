# extr4 2.0 (mod by qiaelel)
## About
extr4 - userbot for telegram. The userbot works because of modules.

More ideas was taken from [hikka](https://github.com/hikariatama/Hikka)

## Features
### Utils
Utils are files located in the `utils/` directory. They act like mini-libraries that help other developers. The standard ones are `utils.py` and `argutils.py`.
You also can write your own utils for make smth easier.

Short docs for utils.py and argutils.py:

- utils.py
  This file contains the `Config` class, it makes working with userbot\`s config more easier.

- argutils.py
  This file includes several helpers, such as the `is_args()` function or `Args` class for handling user command arguments.

### Handlers
In the 2.0 update of Extr4, I added the `@handler()` decorator in `loader.py`.

I\`d call it the next generation of the `@command()` decorator - previously, modules could only handle user command like `.info`, but now their capabilities are *unlimited*. They can handle any type of callback.

### Modules
For this Userbot, you can write modules yourself or use ready-made modules in the `/modules` folder.

## Setup
1. Install the requirements:

```pip install -r requirements.txt```

2. Run the setup.py file:

 - Windows:
      

    ```python setup.py```

  - Linux:  
      

    ```python3 setup.py```

3. Follow the instructions in the terminal.

## How it works?
This Usbot works with the Pyrogram library  ...

## Authors
Author: evryz4,
*Modified by qiaelel*
