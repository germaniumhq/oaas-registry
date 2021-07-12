load("//build/bazel:python.bzl", "ge_python_docker_image")
load("@pip//:requirements.bzl", "requirement")


ge_python_docker_image(
  name="registry",
  srcs=glob(["oaas_registry/**/*.py"]),
  deps=[
    "//oaas/grpc",
    "//oaas/countertype",
    requirement("readerwriterlock"),
  ],
  main="oaas_registry/__main__.py",
)
