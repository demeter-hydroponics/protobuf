#!/bin/sh

# grab the latest protoc
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest

protoc --proto_path=src --go_out=out --go_opt=paths=source_relative foo.proto bar/baz.proto
