# From Wishlist To Cart 

You can automate adding games from Steam wishlist to cart with specified parameters with Python Selenium library.

## Authors

- [@hyp3ri0nnn](https://www.github.com/hyp3ri0nnn)

## Run Locally

- Clone the Project
```
  git clone https://github.com/hyp3ri0nnn/wishlist-to-cart
```

<img height=100% src="https://media.giphy.com/media/mFSVn2yyD7J0SCXbsP/giphy.gif">

- Download the right driver according to browser that you use and replace with geckodriver.exe.

[Drivers](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference)

- Go to the project directory

```bash
  cd wishlist-to-cart
```

- Run the steamBuyer.py.

```bash
  python steamBuyer.py <steamId> <sort-type> <game-Count>
```

<img height=100% src="https://media.giphy.com/media/LlVFMw8atOFLZxflXc/giphy.gif">

## Features 

- Skip the age confirmation.
- Scroll to load more games. 
- Go to store page for games that have "View Details" instead of "Add Cart".

## Tech 

_Python_ == __3.8.5__ \
_Selenium_ == __4.1.0__
