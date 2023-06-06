Any third-party python packages any lib or app package needs to use must be added to the `requirements.txt` here. You can the specify what dependency you need for your package in its own `BUILD` file.

Requirements are installed from `requirements_lock.txt` to ensure supply chain integrity. To generate a new `requirements_lock.txt` file, run:

```bash
bazel run //third-party:requirements.update
```

Finally, to install the packages locally (for intellisense, etc.) run:

```bash
# Be sure you have activated your virtualenv first! Using the legacy resolver because of https://github.com/pypa/pip/issues/9644
pip install -r third-party/requirements_lock.txt --use-deprecated=legacy-resolver
```
