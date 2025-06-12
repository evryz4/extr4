# extr4
## What is this
extr4 - userbot for telegram. The userbot ~~supports~~ works because of modules.

P.S. More ideas was taken from [hikka](https://github.com/hikariatama/Hikka)

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

## Setup
1. Install the requirements:

```pip install -r requirements.txt```

2. Run the setup.py file:

 - Windows:
      

    ```python setup.py```

  - Linux:  
      

    ```python3 setup.py```


## Authors
Author: evryz4,
*Modified by qiaelel*
