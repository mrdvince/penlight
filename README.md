
# penlight

a micro library for tensor stuff on opencl using arrayfire backend.

> trying some opencl stuff on a "pytorch" like thing (basically stealing with no idea what am doing).

## running

```bash
git clone --recursive git@github.com:mrdvince/penlight.git

```

then

```bash
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3-config --includes) -Iextern/pybind11/include bindings.cpp -o bindings$(python3-config --extension-suffix)
```

probably going to switch to cmake.
