python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=.  ./data.proto
protoc ./*.proto --go_out=.
protoc ./*.proto --python_out=.