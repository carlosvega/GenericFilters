# GenericFilters

## Simple class with for some generic filtering

* By default checks if the strings from the conditions are contained in the given values.
* If the variables to be compared fail not having the *in* operator then checks with == operator. 


## Example:
```python
f = filter(alias='filtro', ip='192.168.2.1', method=['GET', 'POST'])
f.check_filter(ip='192.168.2.1', method='GET')  	# => TRUE
f.check_filter(ip='192.168.2.1', method='POST') 	# => TRUE

f.check_filter(ip='192.168.2.1') 					# => FALSE
f.check_filter(method='GET') 						# => FALSE
f.check_filter(ip='192.168.2.1', method='POTATO')	# => FALSE
f.check_filter() 									# => FALSE
```

## Installation

git clone https://github.com/carlosvega/GenericFilters.git gf
cd gf
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
py.test



```
       _~
    _~ )_)_~
    )_))_))_)
    _!__!__!_
    \_______/
  ~~~~~~~~~~~~~
   Carlos Vega
```
