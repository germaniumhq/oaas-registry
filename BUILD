subinclude("//build/please:python.plz")

python_binary(
  name="registry",
  deps=[
    # external
    "//build/thirdparty/python:grpc-stubs",
    "//build/thirdparty/python:readerwriterlock",
    "//build/thirdparty/python:typing-extensions",

    # local
    "//oaas/oaas:oaas-lib",
    "//oaas/grpc:grpc-lib",
    "//oaas/simple:simple-lib",
    "//oaas/registry-api:registry-api-lib",
    "//oaas/countertype:countertype-lib",
  ],
  srcs=glob([
    "oaas_registry/**/*.py"
  ], exclude=[
    "oaas_registry/__main__.py",
  ]),
  main="oaas_registry/__main__.py",
)

ge_python_image(
  name="registry-image",
  deps=[
    # external
    "//build/thirdparty/gepython:grpc-stubs",
    "//build/thirdparty/gepython:readerwriterlock",
    "//build/thirdparty/gepython:typing-extensions",

    # local
    "//oaas/oaas",
    "//oaas/grpc",
    "//oaas/simple",
    "//oaas/registry-api",
    "//oaas/countertype",
  ],
  srcs=glob(["oaas_registry/**/*.py"]),
  main="oaas_registry/__main__.py",
)

