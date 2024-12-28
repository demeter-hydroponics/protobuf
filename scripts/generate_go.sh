#!/bin/sh

# Check if the system is macOS
if [ "$(uname)" = "Darwin" ]; then
    echo "you are on mac, run 'brew install protobuf'"
# Check if the system is Linux
elif [ "$(uname)" = "Linux" ]; then
    echo "on linux, installing protobuf compiler"
    apt install -y protobuf-compiler # this is protoc
else
    echo "You are on an unsupported OS"
fi

# protoc needs this to build go code
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
export PATH="$PATH:$(go env GOPATH)/bin"

# make the generated folder if it doesnt already exist
mkdir -p generated

protoc \
--proto_path=messages \
--go_out=generated \
--go_opt=paths=source_relative \
metrics/node_stats.proto common/common.proto pump/pump_stats.proto pump/mixing_stats.proto
