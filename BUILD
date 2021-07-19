subinclude("//build/please:python.plz")


ge_python_library(
  name="registry",
  deps=[
    # external
    "//build/thirdparty/python:grpc-stubs",
    "//build/thirdparty/python:readerwriterlock",

    # local
    "//oaas/oaas",
    "//oaas/grpc",
    "//oaas/simple",
    "//oaas/registry-api",
    "//oaas/countertype",
  ],
  srcs=glob(["oaas_registry/**/*.py"]),
)


ge_python_image(
  name="registry-image",
  deps=[
    ":registry",
  ],
  main="oaas_registry/__main__.py",
)
