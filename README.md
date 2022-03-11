
# Penlight

A micro library for tensor stuff on OpenCL using ArrayFire backend.

> Trying some OpenCL stuff on a "PyTorch" like thing (basically stealing with no idea what am doing).

## Running

```bash
git clone --recursive git@github.com:mrdvince/penlight.git

```

Then

```bash
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3-config --includes) -Iextern/pybind11/include bindings.cpp -o bindings$(python3-config --extension-suffix)
```

Probably going to switch to cmake.
