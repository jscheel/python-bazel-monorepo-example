load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "//third-party:requirements.txt",
    requirements_txt = "//third-party:requirements_lock.txt",
    visibility = ["//visibility:public"]
)
