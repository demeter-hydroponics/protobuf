#!/bin/sh

# protoc needs this to build go code
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
export PATH="$PATH:$(go env GOPATH)/bin"

# make the generated folder if it doesnt already exist
mkdir -p generated/go

protoc \
--proto_path=messages \
--go_out=generated/go \
--go_opt=paths=source_relative \
common.proto \
node/metrics.proto node/commands.proto \
column/pump_metrics.proto column/mixing_metrics.proto column/pump_manager_info.proto column/commands.proto \
panel/configs.proto

