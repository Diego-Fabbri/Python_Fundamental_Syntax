### Install new modules with PIP
## PIP is a package manager

## check if you have PIP: pip --version  (in console)
## install PIP:  python get-pip.py

## check available packages at https://pypi.org/
## choose/search a package you want to install, click on it and use the suggested code

# for instance: use " pip install camelcase " to install camelcase package   (write it in console)

# use the downloaded package as a module
import camelcase

c = camelcase.CamelCase() # format statement with capital letter for every word

x = "i'm diego, hi!"

print(c.hump(x))


## if you want to uninstall a package write in console:    pip uninstall package_name 


## To verify installed packages on your device, write in console:      pip list 
